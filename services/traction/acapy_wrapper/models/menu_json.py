# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from acapy_wrapper.models.menu_option import MenuOption


class MenuJson(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    MenuJson - a model defined in OpenAPI

        description: The description of this MenuJson [Optional].
        errormsg: The errormsg of this MenuJson [Optional].
        options: The options of this MenuJson.
        title: The title of this MenuJson [Optional].
    """

    description: Optional[str] = None
    errormsg: Optional[str] = None
    options: List[MenuOption]
    title: Optional[str] = None


MenuJson.update_forward_refs()
