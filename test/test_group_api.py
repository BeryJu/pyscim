"""
    SCIM API

    Janssen SCIM 2.0 server API. Developers can think of SCIM as a REST API with endpoints exposing CRUD functionality (create, update, retrieve and delete) for identity management resources such as users, groups, and fido devices.   # noqa: E501

    The version of the OpenAPI document: 5.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import pyscim
from pyscim.api.group_api import GroupApi  # noqa: E501


class TestGroupApi(unittest.TestCase):
    """GroupApi unit test stubs"""

    def setUp(self):
        self.api = GroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_group(self):
        """Test case for create_group"""
        pass

    def test_delete_group_by_id(self):
        """Test case for delete_group_by_id"""
        pass

    def test_get_group_by_id(self):
        """Test case for get_group_by_id"""
        pass

    def test_get_groups(self):
        """Test case for get_groups"""
        pass

    def test_patch_group_by_id(self):
        """Test case for patch_group_by_id"""
        pass

    def test_search_group(self):
        """Test case for search_group"""
        pass

    def test_update_group_by_id(self):
        """Test case for update_group_by_id"""
        pass


if __name__ == "__main__":
    unittest.main()
