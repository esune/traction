# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class RawEncoded(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RawEncoded - a model defined in OpenAPI

        encoded: The encoded of this RawEncoded [Optional].
        raw: The raw of this RawEncoded [Optional].
    """

    encoded: Optional[str] = None
    raw: Optional[str] = None

    @validator("encoded")
    def encoded_pattern(cls, value):
        assert value is not None and re.match(r"^-?[0-9]*$", value)
        return value


RawEncoded.update_forward_refs()
