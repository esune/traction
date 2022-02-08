# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from acapy_wrapper.models.credential_proposal import CredentialProposal


class V10CredentialBoundOfferRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V10CredentialBoundOfferRequest - a model defined in OpenAPI

        counter_proposal: The counter_proposal of this V10CredentialBoundOfferRequest [Optional].
    """

    counter_proposal: Optional[CredentialProposal] = None


V10CredentialBoundOfferRequest.update_forward_refs()
