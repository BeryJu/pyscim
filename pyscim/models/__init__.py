# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from pyscim.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from pyscim.model.address import Address
from pyscim.model.base_resource import BaseResource
from pyscim.model.basic_list_response import BasicListResponse
from pyscim.model.bulk_data import BulkData
from pyscim.model.bulk_operation import BulkOperation
from pyscim.model.bulk_request import BulkRequest
from pyscim.model.bulk_request_all_of import BulkRequestAllOf
from pyscim.model.email import Email
from pyscim.model.entitlement import Entitlement
from pyscim.model.error_response import ErrorResponse
from pyscim.model.fido2_device_resource import Fido2DeviceResource
from pyscim.model.fido2_device_resource_all_of import Fido2DeviceResourceAllOf
from pyscim.model.fido2_list_response import Fido2ListResponse
from pyscim.model.fido2_list_response_all_of import Fido2ListResponseAllOf
from pyscim.model.fido_device_resource import FidoDeviceResource
from pyscim.model.fido_device_resource_all_of import FidoDeviceResourceAllOf
from pyscim.model.fido_list_response import FidoListResponse
from pyscim.model.fido_list_response_all_of import FidoListResponseAllOf
from pyscim.model.generic_list_response import GenericListResponse
from pyscim.model.generic_list_response_all_of import GenericListResponseAllOf
from pyscim.model.generic_resource import GenericResource
from pyscim.model.group import Group
from pyscim.model.group_list_response import GroupListResponse
from pyscim.model.group_list_response_all_of import GroupListResponseAllOf
from pyscim.model.group_resource import GroupResource
from pyscim.model.group_resource_all_of import GroupResourceAllOf
from pyscim.model.instant_messaging_address import InstantMessagingAddress
from pyscim.model.member import Member
from pyscim.model.meta import Meta
from pyscim.model.name import Name
from pyscim.model.patch_operation import PatchOperation
from pyscim.model.patch_request import PatchRequest
from pyscim.model.phone_number import PhoneNumber
from pyscim.model.photo import Photo
from pyscim.model.resource_type import ResourceType
from pyscim.model.resource_type_list_response import ResourceTypeListResponse
from pyscim.model.resource_type_list_response_all_of import (
    ResourceTypeListResponseAllOf,
)
from pyscim.model.resource_type_schema_extensions import ResourceTypeSchemaExtensions
from pyscim.model.role import Role
from pyscim.model.schema_attribute import SchemaAttribute
from pyscim.model.schema_list_response import SchemaListResponse
from pyscim.model.schema_list_response_all_of import SchemaListResponseAllOf
from pyscim.model.schema_resource import SchemaResource
from pyscim.model.search_request import SearchRequest
from pyscim.model.service_provider_config_response import ServiceProviderConfigResponse
from pyscim.model.service_provider_config_response_authentication_schemes import (
    ServiceProviderConfigResponseAuthenticationSchemes,
)
from pyscim.model.service_provider_config_response_bulk import (
    ServiceProviderConfigResponseBulk,
)
from pyscim.model.service_provider_config_response_filter import (
    ServiceProviderConfigResponseFilter,
)
from pyscim.model.service_provider_config_response_meta import (
    ServiceProviderConfigResponseMeta,
)
from pyscim.model.service_provider_config_response_patch import (
    ServiceProviderConfigResponsePatch,
)
from pyscim.model.user_list_response import UserListResponse
from pyscim.model.user_list_response_all_of import UserListResponseAllOf
from pyscim.model.user_resource import UserResource
from pyscim.model.user_resource_all_of import UserResourceAllOf
from pyscim.model.x509_certificate import X509Certificate
