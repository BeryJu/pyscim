"""
    SCIM API

    Janssen SCIM 2.0 server API. Developers can think of SCIM as a REST API with endpoints exposing CRUD functionality (create, update, retrieve and delete) for identity management resources such as users, groups, and fido devices.   # noqa: E501

    The version of the OpenAPI document: 5.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import pyscim
from pyscim.api.fido_devices_api import FidoDevicesApi  # noqa: E501


class TestFidoDevicesApi(unittest.TestCase):
    """FidoDevicesApi unit test stubs"""

    def setUp(self):
        self.api = FidoDevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_fido_device_by_id(self):
        """Test case for delete_fido_device_by_id"""
        pass

    def test_get_fido_device_by_id(self):
        """Test case for get_fido_device_by_id"""
        pass

    def test_get_fido_devices(self):
        """Test case for get_fido_devices"""
        pass

    def test_search_fido_device(self):
        """Test case for search_fido_device"""
        pass

    def test_update_fido_device_by_id(self):
        """Test case for update_fido_device_by_id"""
        pass


if __name__ == "__main__":
    unittest.main()
