"""
    SCIM API

    Janssen SCIM 2.0 server API. Developers can think of SCIM as a REST API with endpoints exposing CRUD functionality (create, update, retrieve and delete) for identity management resources such as users, groups, and fido devices.   # noqa: E501

    The version of the OpenAPI document: 5.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pyscim
from pyscim.model.basic_list_response import BasicListResponse
from pyscim.model.user_list_response_all_of import UserListResponseAllOf
from pyscim.model.user_resource import UserResource
globals()['BasicListResponse'] = BasicListResponse
globals()['UserListResponseAllOf'] = UserListResponseAllOf
globals()['UserResource'] = UserResource
from pyscim.model.user_list_response import UserListResponse


class TestUserListResponse(unittest.TestCase):
    """UserListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserListResponse(self):
        """Test UserListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserListResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
