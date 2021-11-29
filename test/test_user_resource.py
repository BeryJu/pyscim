"""
    SCIM API

    Janssen SCIM 2.0 server API. Developers can think of SCIM as a REST API with endpoints exposing CRUD functionality (create, update, retrieve and delete) for identity management resources such as users, groups, and fido devices.   # noqa: E501

    The version of the OpenAPI document: 5.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pyscim
from pyscim.model.address import Address
from pyscim.model.base_resource import BaseResource
from pyscim.model.email import Email
from pyscim.model.entitlement import Entitlement
from pyscim.model.group import Group
from pyscim.model.instant_messaging_address import InstantMessagingAddress
from pyscim.model.meta import Meta
from pyscim.model.name import Name
from pyscim.model.phone_number import PhoneNumber
from pyscim.model.photo import Photo
from pyscim.model.role import Role
from pyscim.model.user_resource_all_of import UserResourceAllOf
from pyscim.model.x509_certificate import X509Certificate
globals()['Address'] = Address
globals()['BaseResource'] = BaseResource
globals()['Email'] = Email
globals()['Entitlement'] = Entitlement
globals()['Group'] = Group
globals()['InstantMessagingAddress'] = InstantMessagingAddress
globals()['Meta'] = Meta
globals()['Name'] = Name
globals()['PhoneNumber'] = PhoneNumber
globals()['Photo'] = Photo
globals()['Role'] = Role
globals()['UserResourceAllOf'] = UserResourceAllOf
globals()['X509Certificate'] = X509Certificate
from pyscim.model.user_resource import UserResource


class TestUserResource(unittest.TestCase):
    """UserResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserResource(self):
        """Test UserResource"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserResource()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
