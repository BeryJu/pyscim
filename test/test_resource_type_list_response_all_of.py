"""
    SCIM API

    Janssen SCIM 2.0 server API. Developers can think of SCIM as a REST API with endpoints exposing CRUD functionality (create, update, retrieve and delete) for identity management resources such as users, groups, and fido devices.   # noqa: E501

    The version of the OpenAPI document: 5.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pyscim
from pyscim.model.resource_type import ResourceType

globals()["ResourceType"] = ResourceType
from pyscim.model.resource_type_list_response_all_of import (
    ResourceTypeListResponseAllOf,
)


class TestResourceTypeListResponseAllOf(unittest.TestCase):
    """ResourceTypeListResponseAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResourceTypeListResponseAllOf(self):
        """Test ResourceTypeListResponseAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ResourceTypeListResponseAllOf()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
