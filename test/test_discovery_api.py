"""
    SCIM API

    Janssen SCIM 2.0 server API. Developers can think of SCIM as a REST API with endpoints exposing CRUD functionality (create, update, retrieve and delete) for identity management resources such as users, groups, and fido devices.   # noqa: E501

    The version of the OpenAPI document: 5.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import pyscim
from pyscim.api.discovery_api import DiscoveryApi  # noqa: E501


class TestDiscoveryApi(unittest.TestCase):
    """DiscoveryApi unit test stubs"""

    def setUp(self):
        self.api = DiscoveryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_resource_type_by_id(self):
        """Test case for get_resource_type_by_id"""
        pass

    def test_get_resource_types(self):
        """Test case for get_resource_types"""
        pass

    def test_get_schema_by_uri(self):
        """Test case for get_schema_by_uri"""
        pass

    def test_get_schemas(self):
        """Test case for get_schemas"""
        pass

    def test_get_service_provider_config(self):
        """Test case for get_service_provider_config"""
        pass


if __name__ == "__main__":
    unittest.main()
