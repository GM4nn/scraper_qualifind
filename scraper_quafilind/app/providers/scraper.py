# lib
from bs4 import BeautifulSoup
from typing import Dict, List
import requests
import time
import json

# selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver

# app
from app.schemas.departments_output import Department as DepartmentOutput
from app.schemas.departments_input import Department as DepartmentInput
from app.schemas.departments_input import ResponseInputData
from app.schemas.departments_output import Subcategory
from app.schemas.product_input import ProductResponse
from app.schemas.departments_output import Category
from app.schemas.extract_product import Url
from app.const import DEFAULT_HEADERS
from app.const import PAYLOAD
from app.const import URL


class ScraperQuaFind:
    def send_request(
        self,
        method: str,
        path: str,
        headers={},
        query_params: Dict = {},
        payload: Dict = {},
    ):
        request = requests.request(
            url=path,
            method=method,
            data=json.dumps(payload),
            params=query_params,
            headers=DEFAULT_HEADERS,
        )

        return request

    def process_data(self, data: list[DepartmentInput]):
        departments_output: List[DepartmentOutput] = []

        for dto_in in data:
            categories = [
                Category(
                    name=sub_category_group_item.sub_category_heading,
                    subcategories=[
                        Subcategory(
                            name=sub_category_links_group.sub_category_link.title,
                            url=sub_category_links_group.sub_category_link.click_through.value,
                        )
                        for sub_category_links_group in sub_category_group_item.sub_category_links_group
                    ],
                )
                for sub_category_group_item in dto_in.sub_category_group
            ]

            departments_output.append(
                DepartmentOutput(
                    department=dto_in.name,
                    url=dto_in.cta.click_through.value,
                    categories=categories,
                )
            )

        return departments_output

    def extract(self):
        response = ""

        try:
            response = self.send_request(
                method="POST",
                path=URL,
                payload=PAYLOAD,
            )
        except Exception:
            pass

        response_departments = ResponseInputData(**response.json())

        departments = self.process_data(
            response_departments.data.content_layout.modules[0].configs.departments
        )

        return departments

    def extract_products(self, data: Url):
        # Launch the web browser
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=chrome_options)

        # Load the web page
        driver.get(data.url)

        # Scroll down using JavaScript
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        select = driver.find_element(
            By.XPATH,
            "//select[@class='o-0 absolute top-0 left-0 h-100 w-100 bottom-0 t-body pointer']",
        )

        select = Select(select)

        select.select_by_value(str(data.page))
        time.sleep(5)

        # Get the updated HTML source after scrolling
        html = driver.page_source

        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")

        # Close the web browser
        driver.quit()

        products_found: ProductResponse

        for x in soup.find_all("script"):
            try:
                json_result = json.loads(x.string)

                if json_result.get("@type") == "ItemList":
                    products_found = ProductResponse(
                        itemListElement=json_result.get("itemListElement")
                    )

                    break
            except Exception:
                pass

        products = {"url": data.url, "products": []}

        for product in products_found.itemListElement:
            products["products"].append(
                {
                    "name": product.item.name,
                    "price": product.item.offers.lowPrice,
                }
            )

        return products


scraper_provider = ScraperQuaFind()
