from schematics.models import Model
from schematics.types import StringType, ListType, ModelType, IntType, BooleanType


# 'https://webtools.realestate.com.au/configuring-widgets-included-via-javascript/'


class Locality(Model):
    """
    Models the locality object.
    """
    SUBDIVISION_ACT = 'ACT'
    SUBDIVISION_NSW = 'NSW'
    SUBDIVISION_VIC = 'VIC'
    SUBDIVISION_QLD = 'QLD'
    SUBDIVISION_NT = 'NT'
    SUBDIVISION_SA = 'SA'
    SUBDIVISION_TAS = 'TAS'
    SUBDIVISION_CHOICES = (
        SUBDIVISION_ACT,
        SUBDIVISION_NSW,
        SUBDIVISION_VIC,
        SUBDIVISION_QLD,
        SUBDIVISION_NT,
        SUBDIVISION_SA,
        SUBDIVISION_TAS,
    )

    locality = StringType(required=False, serialize_when_none=False)
    subdivision = StringType(required=False, choices=SUBDIVISION_CHOICES, serialize_when_none=False)
    postcode = StringType(required=False, serialize_when_none=False)


class PriceRange(Model):
    """
    Models a price range.
    """
    minimum = IntType(required=False, serialize_when_none=False)
    maximum = IntType(required=False, serialize_when_none=False)


class Filters(Model):
    """
    Models filters.
    """
    PROPERTY_TYPE_HOUSE = 'house'
    PROPERTY_TYPE_UNIT = 'unit'
    PROPERTY_TYPE_APARTMENT = 'apartment'
    PROPERTY_TYPE_UNIT_APARTMENT = 'unit apartment'  # Not sure about this one
    PROPERTY_TYPE_TOWNHOUSE = 'townhouse'
    PROPERTY_TYPE_VILLA = 'villa'
    PROPERTY_TYPE_LAND = 'land'
    PROPERTY_TYPE_ACREAGE = 'acreage'
    PROPERTY_TYPE_RURAL = 'rural'
    PROPERTY_TYPE_CHOICES = (
        PROPERTY_TYPE_HOUSE,
        PROPERTY_TYPE_UNIT,
        PROPERTY_TYPE_APARTMENT,
        PROPERTY_TYPE_UNIT_APARTMENT,
        PROPERTY_TYPE_TOWNHOUSE,
        PROPERTY_TYPE_VILLA,
        PROPERTY_TYPE_LAND,
        PROPERTY_TYPE_ACREAGE,
        PROPERTY_TYPE_RURAL,
    )

    PRODUCT_TYPE_FEATURE = 'feature-only'
    PRODUCT_TYPE_PERMIERE = 'premiere-only'
    PRODUCT_TYPE_FEATURE_AND_PREMIERE = 'feature-and-premiere'
    PRODUCT_TYPE_CHOICES = (
        PRODUCT_TYPE_FEATURE,
        PRODUCT_TYPE_PERMIERE,
        PRODUCT_TYPE_FEATURE_AND_PREMIERE,
    )

    property_types = ListType(StringType(choices=PROPERTY_TYPE_CHOICES), required=False,
                              serialized_name='property-types', serialize_when_none=False)
    minimum_bedrooms = IntType(required=False, serialized_name='minimum-bedrooms', serialize_when_none=False)
    minimum_bathrooms = IntType(required=False, serialized_name='minimum-bathrooms', serialize_when_none=False)
    minimum_parking_spaces = IntType(required=False, serialized_name='minimum-parking-spaces',
                                     serialize_when_none=False)
    surrounding_suburbs = BooleanType(required=False, serialized_name='surrounding-suburbs', serialize_when_none=False)
    upgrade_product_type = StringType(required=False, choices=PRODUCT_TYPE_CHOICES,
                                      serialized_name='upgrade-product-type', serialize_when_none=False)
    agency_id = StringType(required=False, serialized_name='agency-id', serialize_when_none=False)
    price_range = ModelType(PriceRange, required=False, serialized_name='price-range', serialize_when_none=False)


class Search(Model):
    """
    Models the search object.
    """
    CHANNEL_BUY = 'buy'
    CHANNEL_SOLD = 'sold'
    CHANNEL_RENT = 'rent'
    CHANNEL_CHOICES = (
        CHANNEL_BUY,
        CHANNEL_SOLD,
        CHANNEL_RENT,
    )

    channel = StringType(required=True, choices=CHANNEL_CHOICES, default=CHANNEL_BUY)
    localities = ListType(ModelType(Locality), required=False, serialize_when_none=False)
    filters = ModelType(Filters, required=False, serialize_when_none=False)
