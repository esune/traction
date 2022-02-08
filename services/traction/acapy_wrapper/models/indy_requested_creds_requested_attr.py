# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class IndyRequestedCredsRequestedAttr(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyRequestedCredsRequestedAttr - a model defined in OpenAPI

        cred_id: The cred_id of this IndyRequestedCredsRequestedAttr.
        revealed: The revealed of this IndyRequestedCredsRequestedAttr [Optional].
    """

    cred_id: str
    revealed: Optional[bool] = None


IndyRequestedCredsRequestedAttr.update_forward_refs()
