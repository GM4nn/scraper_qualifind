from __future__ import annotations
from pydantic import BaseModel, validator
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Base(BaseModel):
    class Config:
        validate_assignment = True


class ClickThrough(Base):
    value: Optional[str]


class CtaItem(Base):
    link_text: Optional[str] = Field("", alias="linkText")
    title: Optional[str]
    click_through: Optional[ClickThrough] = Field(
        default=ClickThrough(), alias="clickThrough"
    )
    uid: Optional[str]

    @validator("click_through", pre=True, always=True)
    def set_clickThrough(cls, click_through):
        return click_through or ClickThrough()


class ClickThrough1(Base):
    value: Optional[str]


class SubCategoryLink(Base):
    link_text: Optional[str] = Field("", alias="linkText")
    title: Optional[str]
    click_through: Optional[ClickThrough1] = Field(
        ClickThrough1(), alias="clickThrough"
    )
    uid: Optional[str]

    @validator("click_through", pre=True, always=True)
    def set_click_through(cls, sub_category_link):
        return sub_category_link or ClickThrough1()


class SubCategoryLinksGroupItem(Base):
    sub_category_link: Optional[SubCategoryLink] = Field(
        default=SubCategoryLink(), alias="subCategoryLink"
    )
    open_in_new_tab: Optional[str] = Field("", alias="openInNewTab")

    @validator("sub_category_link", pre=True, always=True)
    def set_sub_category_link(cls, sub_category_link):
        return sub_category_link or SubCategoryLink()


class SubCategoryGroupItem(Base):
    sub_category_heading: Optional[str] = Field("", alias="subCategoryHeading")
    sub_category_links_group: Optional[List[SubCategoryLinksGroupItem]] = Field(
        [], alias="subCategoryLinksGroup"
    )


class Department(Base):
    name: Optional[str]
    cta: Optional[CtaItem] = Field(default=CtaItem())
    heading: Optional[str]
    description: Optional[str]
    sub_category_group: Optional[List[SubCategoryGroupItem]] = Field(
        [], alias="subCategoryGroup"
    )

    @validator("cta", pre=True, always=True)
    def set_cta(cls, cta):
        return cta or CtaItem()


class Configs(Base):
    departments: Optional[List[Department]] = []


class Module(Base):
    configs: Optional[Configs] = Configs()


class ContentLayout(Base):
    modules: Optional[List[Module]] = []


class Data(Base):
    content_layout: Optional[ContentLayout] = Field(
        ContentLayout(), alias="contentLayout"
    )


class ResponseInputData(Base):
    data: Optional[Data] = Data()
