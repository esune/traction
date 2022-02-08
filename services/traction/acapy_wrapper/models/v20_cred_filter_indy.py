# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class V20CredFilterIndy(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredFilterIndy - a model defined in OpenAPI

        cred_def_id: The cred_def_id of this V20CredFilterIndy [Optional].
        issuer_did: The issuer_did of this V20CredFilterIndy [Optional].
        schema_id: The schema_id of this V20CredFilterIndy [Optional].
        schema_issuer_did: The schema_issuer_did of this V20CredFilterIndy [Optional].
        schema_name: The schema_name of this V20CredFilterIndy [Optional].
        schema_version: The schema_version of this V20CredFilterIndy [Optional].
    """

    cred_def_id: Optional[str] = None
    issuer_did: Optional[str] = None
    schema_id: Optional[str] = None
    schema_issuer_did: Optional[str] = None
    schema_name: Optional[str] = None
    schema_version: Optional[str] = None

    @validator("cred_def_id")
    def cred_def_id_pattern(cls, value):
        assert value is not None and re.match(
            r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$",
            value,
        )
        return value

    @validator("issuer_did")
    def issuer_did_pattern(cls, value):
        assert value is not None and re.match(
            r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$",
            value,
        )
        return value

    @validator("schema_id")
    def schema_id_pattern(cls, value):
        assert value is not None and re.match(
            r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$",
            value,
        )
        return value

    @validator("schema_issuer_did")
    def schema_issuer_did_pattern(cls, value):
        assert value is not None and re.match(
            r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$",
            value,
        )
        return value

    @validator("schema_version")
    def schema_version_pattern(cls, value):
        assert value is not None and re.match(r"^[0-9.]+$", value)
        return value


V20CredFilterIndy.update_forward_refs()
