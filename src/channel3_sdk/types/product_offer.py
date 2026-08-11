# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .price import Price
from .._models import BaseModel

__all__ = ["ProductOffer", "Dimensions", "DimensionsHeight", "DimensionsLength", "DimensionsWeight", "DimensionsWidth"]


class DimensionsHeight(BaseModel):
    """A length measurement, in one of the supported length units."""

    number: float

    unit: Literal["mm", "cm", "m", "in", "ft"]
    """
    The unit from the request's dimension filters when one was given (the value is
    converted to it); otherwise the unit the merchant stated.
    """


class DimensionsLength(BaseModel):
    """A length measurement, in one of the supported length units."""

    number: float

    unit: Literal["mm", "cm", "m", "in", "ft"]
    """
    The unit from the request's dimension filters when one was given (the value is
    converted to it); otherwise the unit the merchant stated.
    """


class DimensionsWeight(BaseModel):
    """A weight measurement, in one of the supported weight units."""

    number: float

    unit: Literal["mg", "g", "kg", "oz", "lb"]
    """
    The unit from the request's dimension filters when one was given (the value is
    converted to it); otherwise the unit the merchant stated.
    """


class DimensionsWidth(BaseModel):
    """A length measurement, in one of the supported length units."""

    number: float

    unit: Literal["mm", "cm", "m", "in", "ft"]
    """
    The unit from the request's dimension filters when one was given (the value is
    converted to it); otherwise the unit the merchant stated.
    """


class Dimensions(BaseModel):
    """Physical dimensions of a product offer. Members are null when unknown.

    Values are standardized to the supported unit set; a merchant-stated value
    whose unit is not one of those units is omitted rather than shown.
    """

    height: Optional[DimensionsHeight] = None
    """A length measurement, in one of the supported length units."""

    length: Optional[DimensionsLength] = None
    """A length measurement, in one of the supported length units."""

    weight: Optional[DimensionsWeight] = None
    """A weight measurement, in one of the supported weight units."""

    width: Optional[DimensionsWidth] = None
    """A length measurement, in one of the supported length units."""


class ProductOffer(BaseModel):
    availability: Literal["InStock", "OutOfStock"]
    """The two availability values the public API emits on offers.

    Internal `AvailabilityStatus` values are collapsed to these via
    `AvailabilityStatus.to_api()`.
    """

    domain: str

    price: Price

    url: str

    condition: Optional[Literal["new", "used"]] = None
    """Offer condition.

    'refurbished' is deprecated: rejected as a filter value, coerced to None on
    responses.
    """

    dimensions: Optional[Dimensions] = None
    """Physical dimensions of a product offer. Members are null when unknown.

    Values are standardized to the supported unit set; a merchant-stated value whose
    unit is not one of those units is omitted rather than shown.
    """

    max_commission_rate: Optional[float] = None
    """
    The maximum commission rate for the merchant, as a decimal fraction: 0 is no
    commission, 0.5 is 50% commission. 'Max' because the actual commission rate may
    be lower due to vendor-specific affiliate rules.
    """
