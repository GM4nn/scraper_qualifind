import json
import unittest
import requests


class TestScraper(unittest.TestCase):
    host = "http://localhost"
    path_larder = "/api/v1/scraper/larder"
    path_products = "/api/v1/scraper/products"

    def test_larder(self):
        request = requests.request(url=f"{self.host}{self.path_larder}", method="GET")

        response = request.json()

        self.assertTrue(len(response) >= 1)
        self.assertEqual(request.status_code, 200)

    def test_products(self):
        url = "https://www.tiendasjumbo.co/ropa-y-accesorios/mujer/blusas-y-camisas"
        request = requests.request(
            url=f"{self.host}{self.path_products}",
            method="POST",
            data=json.dumps({"url": url}),
        )

        response = request.json()

        self.assertTrue(len(response) >= 1)
        self.assertEqual(request.status_code, 200)


# validate test
def validate_test():
    test_classes_to_run = [TestScraper]
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
    big_suite = unittest.TestSuite(suites_list)
    return big_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(validate_test())
