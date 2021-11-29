"""
    SCIM API

    Janssen SCIM 2.0 server API. Developers can think of SCIM as a REST API with endpoints exposing CRUD functionality (create, update, retrieve and delete) for identity management resources such as users, groups, and fido devices.   # noqa: E501

    The version of the OpenAPI document: 5.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pyscim
from pyscim.model.base_resource import BaseResource
from pyscim.model.fido2_device_resource_all_of import Fido2DeviceResourceAllOf
from pyscim.model.meta import Meta

globals()["BaseResource"] = BaseResource
globals()["Fido2DeviceResourceAllOf"] = Fido2DeviceResourceAllOf
globals()["Meta"] = Meta
from pyscim.model.fido2_device_resource import Fido2DeviceResource


class TestFido2DeviceResource(unittest.TestCase):
    """Fido2DeviceResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFido2DeviceResource(self):
        """Test Fido2DeviceResource"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Fido2DeviceResource()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
