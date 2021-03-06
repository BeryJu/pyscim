"""
    SCIM API

    Janssen SCIM 2.0 server API. Developers can think of SCIM as a REST API with endpoints exposing CRUD functionality (create, update, retrieve and delete) for identity management resources such as users, groups, and fido devices.   # noqa: E501

    The version of the OpenAPI document: 5.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pyscim
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

globals()[
    "ServiceProviderConfigResponseAuthenticationSchemes"
] = ServiceProviderConfigResponseAuthenticationSchemes
globals()["ServiceProviderConfigResponseBulk"] = ServiceProviderConfigResponseBulk
globals()["ServiceProviderConfigResponseFilter"] = ServiceProviderConfigResponseFilter
globals()["ServiceProviderConfigResponseMeta"] = ServiceProviderConfigResponseMeta
globals()["ServiceProviderConfigResponsePatch"] = ServiceProviderConfigResponsePatch
from pyscim.model.service_provider_config_response import ServiceProviderConfigResponse


class TestServiceProviderConfigResponse(unittest.TestCase):
    """ServiceProviderConfigResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServiceProviderConfigResponse(self):
        """Test ServiceProviderConfigResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServiceProviderConfigResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
