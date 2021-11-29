"""
    SCIM API

    Janssen SCIM 2.0 server API. Developers can think of SCIM as a REST API with endpoints exposing CRUD functionality (create, update, retrieve and delete) for identity management resources such as users, groups, and fido devices.   # noqa: E501

    The version of the OpenAPI document: 5.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pyscim.api_client import ApiClient, Endpoint as _Endpoint
from pyscim.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from pyscim.model.error_response import ErrorResponse
from pyscim.model.patch_request import PatchRequest
from pyscim.model.search_request import SearchRequest
from pyscim.model.user_list_response import UserListResponse
from pyscim.model.user_resource import UserResource


class UserApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_user_endpoint = _Endpoint(
            settings={
                "response_type": (UserResource,),
                "auth": ["scim_oauth"],
                "endpoint_path": "/Users",
                "operation_id": "create_user",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "user",
                    "attributes",
                    "excluded_attributes",
                ],
                "required": [
                    "user",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "user": (UserResource,),
                    "attributes": (str,),
                    "excluded_attributes": (str,),
                },
                "attribute_map": {
                    "attributes": "attributes",
                    "excluded_attributes": "excludedAttributes",
                },
                "location_map": {
                    "user": "body",
                    "attributes": "query",
                    "excluded_attributes": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/scim+json", "application/json"],
                "content_type": ["application/scim+json", "application/json"],
            },
            api_client=api_client,
        )
        self.delete_user_by_id_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["scim_oauth"],
                "endpoint_path": "/Users/{id}",
                "operation_id": "delete_user_by_id",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "all": [
                    "id",
                ],
                "required": [
                    "id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "id": (str,),
                },
                "attribute_map": {
                    "id": "id",
                },
                "location_map": {
                    "id": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/scim+json", "application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.get_user_by_id_endpoint = _Endpoint(
            settings={
                "response_type": (UserResource,),
                "auth": ["scim_oauth"],
                "endpoint_path": "/Users/{id}",
                "operation_id": "get_user_by_id",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "id",
                    "attributes",
                    "excluded_attributes",
                ],
                "required": [
                    "id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "id": (str,),
                    "attributes": (str,),
                    "excluded_attributes": (str,),
                },
                "attribute_map": {
                    "id": "id",
                    "attributes": "attributes",
                    "excluded_attributes": "excludedAttributes",
                },
                "location_map": {
                    "id": "path",
                    "attributes": "query",
                    "excluded_attributes": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/scim+json", "application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.get_users_endpoint = _Endpoint(
            settings={
                "response_type": (UserListResponse,),
                "auth": ["scim_oauth"],
                "endpoint_path": "/Users",
                "operation_id": "get_users",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "attributes",
                    "excluded_attributes",
                    "filter",
                    "start_index",
                    "count",
                    "sort_by",
                    "sort_order",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "attributes": (str,),
                    "excluded_attributes": (str,),
                    "filter": (str,),
                    "start_index": (int,),
                    "count": (int,),
                    "sort_by": (str,),
                    "sort_order": (str,),
                },
                "attribute_map": {
                    "attributes": "attributes",
                    "excluded_attributes": "excludedAttributes",
                    "filter": "filter",
                    "start_index": "startIndex",
                    "count": "count",
                    "sort_by": "sortBy",
                    "sort_order": "sortOrder",
                },
                "location_map": {
                    "attributes": "query",
                    "excluded_attributes": "query",
                    "filter": "query",
                    "start_index": "query",
                    "count": "query",
                    "sort_by": "query",
                    "sort_order": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/scim+json", "application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.patch_user_by_id_endpoint = _Endpoint(
            settings={
                "response_type": (UserResource,),
                "auth": ["scim_oauth"],
                "endpoint_path": "/Users/{id}",
                "operation_id": "patch_user_by_id",
                "http_method": "PATCH",
                "servers": None,
            },
            params_map={
                "all": [
                    "id",
                    "request",
                    "attributes",
                    "excluded_attributes",
                ],
                "required": [
                    "id",
                    "request",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "id": (str,),
                    "request": (PatchRequest,),
                    "attributes": (str,),
                    "excluded_attributes": (str,),
                },
                "attribute_map": {
                    "id": "id",
                    "attributes": "attributes",
                    "excluded_attributes": "excludedAttributes",
                },
                "location_map": {
                    "id": "path",
                    "request": "body",
                    "attributes": "query",
                    "excluded_attributes": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/scim+json", "application/json"],
                "content_type": ["application/scim+json", "application/json"],
            },
            api_client=api_client,
        )
        self.search_user_endpoint = _Endpoint(
            settings={
                "response_type": (UserListResponse,),
                "auth": ["scim_oauth"],
                "endpoint_path": "/Users/.search",
                "operation_id": "search_user",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "search_request",
                ],
                "required": [
                    "search_request",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "search_request": (SearchRequest,),
                },
                "attribute_map": {},
                "location_map": {
                    "search_request": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/scim+json", "application/json"],
                "content_type": ["application/scim+json", "application/json"],
            },
            api_client=api_client,
        )
        self.update_user_by_id_endpoint = _Endpoint(
            settings={
                "response_type": (UserResource,),
                "auth": ["scim_oauth"],
                "endpoint_path": "/Users/{id}",
                "operation_id": "update_user_by_id",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "all": [
                    "id",
                    "user",
                    "attributes",
                    "excluded_attributes",
                ],
                "required": [
                    "id",
                    "user",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "id": (str,),
                    "user": (UserResource,),
                    "attributes": (str,),
                    "excluded_attributes": (str,),
                },
                "attribute_map": {
                    "id": "id",
                    "attributes": "attributes",
                    "excluded_attributes": "excludedAttributes",
                },
                "location_map": {
                    "id": "path",
                    "user": "body",
                    "attributes": "query",
                    "excluded_attributes": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/scim+json", "application/json"],
                "content_type": ["application/scim+json", "application/json"],
            },
            api_client=api_client,
        )

    def create_user(self, user, **kwargs):
        """create_user  # noqa: E501

        Allows creating a User resource via POST (see section 3.3 of RFC 7644)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_user(user, async_req=True)
        >>> result = thread.get()

        Args:
            user (UserResource): Payload that represents the Group to create

        Keyword Args:
            attributes (str): A comma-separated list of attribute names to return in the response. [optional]
            excluded_attributes (str): When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list). [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UserResource
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["user"] = user
        return self.create_user_endpoint.call_with_http_info(**kwargs)

    def delete_user_by_id(self, id, **kwargs):
        """delete_user_by_id  # noqa: E501

        Deletes a user resource  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_user_by_id(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): Identifier of the resource to delete

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["id"] = id
        return self.delete_user_by_id_endpoint.call_with_http_info(**kwargs)

    def get_user_by_id(self, id, **kwargs):
        """get_user_by_id  # noqa: E501

        Retrieves a User resource by Id (see section 3.4.1 of RFC 7644)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_user_by_id(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str):

        Keyword Args:
            attributes (str): A comma-separated list of attribute names to return in the response. [optional]
            excluded_attributes (str): When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list). [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UserResource
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["id"] = id
        return self.get_user_by_id_endpoint.call_with_http_info(**kwargs)

    def get_users(self, **kwargs):
        """get_users  # noqa: E501

        Query User resources (see section 3.4.2 of RFC 7644)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_users(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            attributes (str): A comma-separated list of attribute names to return in the response. [optional]
            excluded_attributes (str): When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list). [optional]
            filter (str): An expression specifying the search criteria. See section 3.4.2.2 of RFC 7644. [optional]
            start_index (int): The 1-based index of the first query result. [optional]
            count (int): Specifies the desired maximum number of query results per page. [optional]
            sort_by (str): The attribute whose value will be used to order the returned responses. [optional]
            sort_order (str): Order in which the sortBy param is applied. Allowed values are \"ascending\" and \"descending\". [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UserListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        return self.get_users_endpoint.call_with_http_info(**kwargs)

    def patch_user_by_id(self, id, request, **kwargs):
        """patch_user_by_id  # noqa: E501

        Updates one or more attributes of a User resource using a sequence of additions, removals, and  replacements operations. See section 3.5.2 of RFC 7644   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_user_by_id(id, request, async_req=True)
        >>> result = thread.get()

        Args:
            id (str):
            request (PatchRequest): Payload describing the patch operations to apply upon the resource identified by param id

        Keyword Args:
            attributes (str): A comma-separated list of attribute names to return in the response. [optional]
            excluded_attributes (str): When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list). [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UserResource
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["id"] = id
        kwargs["request"] = request
        return self.patch_user_by_id_endpoint.call_with_http_info(**kwargs)

    def search_user(self, search_request, **kwargs):
        """search_user  # noqa: E501

        Query User resources (see section 3.4.2 of RFC 7644)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_user(search_request, async_req=True)
        >>> result = thread.get()

        Args:
            search_request (SearchRequest): Payload that represents the search criteria

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UserListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["search_request"] = search_request
        return self.search_user_endpoint.call_with_http_info(**kwargs)

    def update_user_by_id(self, id, user, **kwargs):
        """update_user_by_id  # noqa: E501

        Updates a User resource (see section 3.5.1 of RFC 7644). Update works in a replacement fashion&amp;#58; every attribute value found in the payload sent will replace the one in the existing resource representation. Attributes  not passed in the payload will be left intact.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_user_by_id(id, user, async_req=True)
        >>> result = thread.get()

        Args:
            id (str):
            user (UserResource): Payload with the data to replace in the existing user identified by the id param

        Keyword Args:
            attributes (str): A comma-separated list of attribute names to return in the response. [optional]
            excluded_attributes (str): When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list). [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UserResource
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["id"] = id
        kwargs["user"] = user
        return self.update_user_by_id_endpoint.call_with_http_info(**kwargs)
