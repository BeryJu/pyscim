"""
    SCIM API

    Janssen SCIM 2.0 server API. Developers can think of SCIM as a REST API with endpoints exposing CRUD functionality (create, update, retrieve and delete) for identity management resources such as users, groups, and fido devices.   # noqa: E501

    The version of the OpenAPI document: 5.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pyscim.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from pyscim.exceptions import ApiAttributeError


def lazy_import():
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

    globals()["Address"] = Address
    globals()["BaseResource"] = BaseResource
    globals()["Email"] = Email
    globals()["Entitlement"] = Entitlement
    globals()["Group"] = Group
    globals()["InstantMessagingAddress"] = InstantMessagingAddress
    globals()["Meta"] = Meta
    globals()["Name"] = Name
    globals()["PhoneNumber"] = PhoneNumber
    globals()["Photo"] = Photo
    globals()["Role"] = Role
    globals()["UserResourceAllOf"] = UserResourceAllOf
    globals()["X509Certificate"] = X509Certificate


class UserResource(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {}

    validations = {}

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (
            bool,
            date,
            datetime,
            dict,
            float,
            int,
            list,
            str,
            none_type,
        )  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            "schemas": ([str],),  # noqa: E501
            "id": (str,),  # noqa: E501
            "meta": (Meta,),  # noqa: E501
            "external_id": (str,),  # noqa: E501
            "user_name": (str,),  # noqa: E501
            "name": (Name,),  # noqa: E501
            "display_name": (str,),  # noqa: E501
            "nick_name": (str,),  # noqa: E501
            "profile_url": (str,),  # noqa: E501
            "title": (str,),  # noqa: E501
            "user_type": (str,),  # noqa: E501
            "preferred_language": (str,),  # noqa: E501
            "locale": (str,),  # noqa: E501
            "timezone": (str,),  # noqa: E501
            "active": (bool,),  # noqa: E501
            "password": (str,),  # noqa: E501
            "emails": ([Email],),  # noqa: E501
            "phone_numbers": ([PhoneNumber],),  # noqa: E501
            "ims": ([InstantMessagingAddress],),  # noqa: E501
            "photos": ([Photo],),  # noqa: E501
            "addresses": ([Address],),  # noqa: E501
            "groups": ([Group],),  # noqa: E501
            "entitlements": ([Entitlement],),  # noqa: E501
            "roles": ([Role],),  # noqa: E501
            "x509_certificates": ([X509Certificate],),  # noqa: E501
            "urnietfparamsscimschemasextensiongluu2_0_user": (
                {str: (bool, date, datetime, dict, float, int, list, str, none_type)},
            ),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "schemas": "schemas",  # noqa: E501
        "id": "id",  # noqa: E501
        "meta": "meta",  # noqa: E501
        "external_id": "externalId",  # noqa: E501
        "user_name": "userName",  # noqa: E501
        "name": "name",  # noqa: E501
        "display_name": "displayName",  # noqa: E501
        "nick_name": "nickName",  # noqa: E501
        "profile_url": "profileUrl",  # noqa: E501
        "title": "title",  # noqa: E501
        "user_type": "userType",  # noqa: E501
        "preferred_language": "preferredLanguage",  # noqa: E501
        "locale": "locale",  # noqa: E501
        "timezone": "timezone",  # noqa: E501
        "active": "active",  # noqa: E501
        "password": "password",  # noqa: E501
        "emails": "emails",  # noqa: E501
        "phone_numbers": "phoneNumbers",  # noqa: E501
        "ims": "ims",  # noqa: E501
        "photos": "photos",  # noqa: E501
        "addresses": "addresses",  # noqa: E501
        "groups": "groups",  # noqa: E501
        "entitlements": "entitlements",  # noqa: E501
        "roles": "roles",  # noqa: E501
        "x509_certificates": "x509Certificates",  # noqa: E501
        "urnietfparamsscimschemasextensiongluu2_0_user": "urn:ietf:params:scim:schemas:extension:gluu:2.0:User",  # noqa: E501
    }

    read_only_vars = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """UserResource - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            schemas ([str]): URIs that are used to indicate the namespaces of the SCIM schemas that define the attributes present in the current structure. [optional]  # noqa: E501
            id (str): A unique identifier for a SCIM resource. See section 3.1 of RFC 7643. [optional]  # noqa: E501
            meta (Meta): [optional]  # noqa: E501
            external_id (str): Identifier of the resource useful from the perspective of the provisioning client. See section 3.1 of RFC 7643. [optional]  # noqa: E501
            user_name (str): Identifier for the user, typically used by the user to directly authenticate (id and externalId are opaque identifiers generally not known by users). [optional]  # noqa: E501
            name (Name): [optional]  # noqa: E501
            display_name (str): Name of the user suitable for display to end-users. [optional]  # noqa: E501
            nick_name (str): Casual way to address the user in real life. [optional]  # noqa: E501
            profile_url (str): URI pointing to a location representing the User's online profile. [optional]  # noqa: E501
            title (str): [optional]  # noqa: E501
            user_type (str): Used to identify the relationship between the organization and the user. [optional]  # noqa: E501
            preferred_language (str): Preferred language as used in the Accept-Language HTTP header. [optional]  # noqa: E501
            locale (str): Used for purposes of localizing items such as currency and dates. [optional]  # noqa: E501
            timezone (str): [optional]  # noqa: E501
            active (bool): [optional]  # noqa: E501
            password (str): [optional]  # noqa: E501
            emails ([Email]): [optional]  # noqa: E501
            phone_numbers ([PhoneNumber]): [optional]  # noqa: E501
            ims ([InstantMessagingAddress]): [optional]  # noqa: E501
            photos ([Photo]): [optional]  # noqa: E501
            addresses ([Address]): [optional]  # noqa: E501
            groups ([Group]): [optional]  # noqa: E501
            entitlements ([Entitlement]): [optional]  # noqa: E501
            roles ([Role]): [optional]  # noqa: E501
            x509_certificates ([X509Certificate]): [optional]  # noqa: E501
            urnietfparamsscimschemasextensiongluu2_0_user ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Extended attributes. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            "_check_type": _check_type,
            "_path_to_item": _path_to_item,
            "_spec_property_naming": _spec_property_naming,
            "_configuration": _configuration,
            "_visited_composed_classes": self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if (
                var_name in discarded_args
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self._additional_properties_model_instances
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)

        return self

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
            "_composed_instances",
            "_var_name_to_model_instances",
            "_additional_properties_model_instances",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """UserResource - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            schemas ([str]): URIs that are used to indicate the namespaces of the SCIM schemas that define the attributes present in the current structure. [optional]  # noqa: E501
            id (str): A unique identifier for a SCIM resource. See section 3.1 of RFC 7643. [optional]  # noqa: E501
            meta (Meta): [optional]  # noqa: E501
            external_id (str): Identifier of the resource useful from the perspective of the provisioning client. See section 3.1 of RFC 7643. [optional]  # noqa: E501
            user_name (str): Identifier for the user, typically used by the user to directly authenticate (id and externalId are opaque identifiers generally not known by users). [optional]  # noqa: E501
            name (Name): [optional]  # noqa: E501
            display_name (str): Name of the user suitable for display to end-users. [optional]  # noqa: E501
            nick_name (str): Casual way to address the user in real life. [optional]  # noqa: E501
            profile_url (str): URI pointing to a location representing the User's online profile. [optional]  # noqa: E501
            title (str): [optional]  # noqa: E501
            user_type (str): Used to identify the relationship between the organization and the user. [optional]  # noqa: E501
            preferred_language (str): Preferred language as used in the Accept-Language HTTP header. [optional]  # noqa: E501
            locale (str): Used for purposes of localizing items such as currency and dates. [optional]  # noqa: E501
            timezone (str): [optional]  # noqa: E501
            active (bool): [optional]  # noqa: E501
            password (str): [optional]  # noqa: E501
            emails ([Email]): [optional]  # noqa: E501
            phone_numbers ([PhoneNumber]): [optional]  # noqa: E501
            ims ([InstantMessagingAddress]): [optional]  # noqa: E501
            photos ([Photo]): [optional]  # noqa: E501
            addresses ([Address]): [optional]  # noqa: E501
            groups ([Group]): [optional]  # noqa: E501
            entitlements ([Entitlement]): [optional]  # noqa: E501
            roles ([Role]): [optional]  # noqa: E501
            x509_certificates ([X509Certificate]): [optional]  # noqa: E501
            urnietfparamsscimschemasextensiongluu2_0_user ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Extended attributes. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            "_check_type": _check_type,
            "_path_to_item": _path_to_item,
            "_spec_property_naming": _spec_property_naming,
            "_configuration": _configuration,
            "_visited_composed_classes": self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if (
                var_name in discarded_args
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self._additional_properties_model_instances
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(
                    f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                    f"class with read only attributes."
                )

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
            "anyOf": [],
            "allOf": [
                BaseResource,
                UserResourceAllOf,
            ],
            "oneOf": [],
        }
