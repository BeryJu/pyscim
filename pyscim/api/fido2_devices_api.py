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
    validate_and_convert_types
)
from pyscim.model.error_response import ErrorResponse
from pyscim.model.fido2_device_resource import Fido2DeviceResource
from pyscim.model.fido2_list_response import Fido2ListResponse
from pyscim.model.search_request import SearchRequest


class Fido2DevicesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.delete_fido2_device_by_id_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'scim_oauth'
                ],
                'endpoint_path': '/Fido2Devices/{id}',
                'operation_id': 'delete_fido2_device_by_id',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/scim+json',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_fido2_device_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (Fido2DeviceResource,),
                'auth': [
                    'scim_oauth'
                ],
                'endpoint_path': '/Fido2Devices/{id}',
                'operation_id': 'get_fido2_device_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'attributes',
                    'excluded_attributes',
                    'user_id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'attributes':
                        (str,),
                    'excluded_attributes':
                        (str,),
                    'user_id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'attributes': 'attributes',
                    'excluded_attributes': 'excludedAttributes',
                    'user_id': 'userId',
                },
                'location_map': {
                    'id': 'path',
                    'attributes': 'query',
                    'excluded_attributes': 'query',
                    'user_id': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/scim+json',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_fido2_devices_endpoint = _Endpoint(
            settings={
                'response_type': (Fido2ListResponse,),
                'auth': [
                    'scim_oauth'
                ],
                'endpoint_path': '/Fido2Devices',
                'operation_id': 'get_fido2_devices',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'attributes',
                    'excluded_attributes',
                    'user_id',
                    'filter',
                    'start_index',
                    'count',
                    'sort_by',
                    'sort_order',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'attributes':
                        (str,),
                    'excluded_attributes':
                        (str,),
                    'user_id':
                        (str,),
                    'filter':
                        (str,),
                    'start_index':
                        (int,),
                    'count':
                        (int,),
                    'sort_by':
                        (str,),
                    'sort_order':
                        (str,),
                },
                'attribute_map': {
                    'attributes': 'attributes',
                    'excluded_attributes': 'excludedAttributes',
                    'user_id': 'userId',
                    'filter': 'filter',
                    'start_index': 'startIndex',
                    'count': 'count',
                    'sort_by': 'sortBy',
                    'sort_order': 'sortOrder',
                },
                'location_map': {
                    'attributes': 'query',
                    'excluded_attributes': 'query',
                    'user_id': 'query',
                    'filter': 'query',
                    'start_index': 'query',
                    'count': 'query',
                    'sort_by': 'query',
                    'sort_order': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/scim+json',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.search_fido2_device_endpoint = _Endpoint(
            settings={
                'response_type': (Fido2ListResponse,),
                'auth': [
                    'scim_oauth'
                ],
                'endpoint_path': '/Fido2Devices/.search',
                'operation_id': 'search_fido2_device',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'search_request',
                    'user_id',
                ],
                'required': [
                    'search_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'search_request':
                        (SearchRequest,),
                    'user_id':
                        (str,),
                },
                'attribute_map': {
                    'user_id': 'userId',
                },
                'location_map': {
                    'search_request': 'body',
                    'user_id': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/scim+json',
                    'application/json'
                ],
                'content_type': [
                    'application/scim+json',
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.update_fido2_device_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (Fido2DeviceResource,),
                'auth': [
                    'scim_oauth'
                ],
                'endpoint_path': '/Fido2Devices/{id}',
                'operation_id': 'update_fido2_device_by_id',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'fido_device_resource',
                    'attributes',
                    'excluded_attributes',
                ],
                'required': [
                    'id',
                    'fido_device_resource',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'fido_device_resource':
                        (Fido2DeviceResource,),
                    'attributes':
                        (str,),
                    'excluded_attributes':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'attributes': 'attributes',
                    'excluded_attributes': 'excludedAttributes',
                },
                'location_map': {
                    'id': 'path',
                    'fido_device_resource': 'body',
                    'attributes': 'query',
                    'excluded_attributes': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/scim+json',
                    'application/json'
                ],
                'content_type': [
                    'application/scim+json',
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def delete_fido2_device_by_id(
        self,
        id,
        **kwargs
    ):
        """delete_fido2_device_by_id  # noqa: E501

        Deletes a Fido 2 resource  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_fido2_device_by_id(id, async_req=True)
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
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        return self.delete_fido2_device_by_id_endpoint.call_with_http_info(**kwargs)

    def get_fido2_device_by_id(
        self,
        id,
        **kwargs
    ):
        """get_fido2_device_by_id  # noqa: E501

        Retrieves a Fido 2 device by Id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_fido2_device_by_id(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str):

        Keyword Args:
            attributes (str): A comma-separated list of attribute names to return in the response. [optional]
            excluded_attributes (str): When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list). [optional]
            user_id (str): Identifier (inum) of the device owner. This param is not required when underlying database is LDAP. [optional]
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
            Fido2DeviceResource
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        return self.get_fido2_device_by_id_endpoint.call_with_http_info(**kwargs)

    def get_fido2_devices(
        self,
        **kwargs
    ):
        """get_fido2_devices  # noqa: E501

        Query Fido 2 resources  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_fido2_devices(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            attributes (str): A comma-separated list of attribute names to return in the response. [optional]
            excluded_attributes (str): When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list). [optional]
            user_id (str): Used to restrict the search to fido 2 resources owned by a specific user. [optional]
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
            Fido2ListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.get_fido2_devices_endpoint.call_with_http_info(**kwargs)

    def search_fido2_device(
        self,
        search_request,
        **kwargs
    ):
        """search_fido2_device  # noqa: E501

        Query Fido 2 resources  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_fido2_device(search_request, async_req=True)
        >>> result = thread.get()

        Args:
            search_request (SearchRequest): Payload that represents the search criteria

        Keyword Args:
            user_id (str): Used to restrict the search to fido 2 resources owned by a specific user. [optional]
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
            Fido2ListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['search_request'] = \
            search_request
        return self.search_fido2_device_endpoint.call_with_http_info(**kwargs)

    def update_fido2_device_by_id(
        self,
        id,
        fido_device_resource,
        **kwargs
    ):
        """update_fido2_device_by_id  # noqa: E501

        Updates a Fido 2 resource. Update works in a replacement fashion&amp;#58; every attribute value found in the payload sent will replace the one in the existing resource representation. Attributes  not passed in the payload will be left intact.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_fido2_device_by_id(id, fido_device_resource, async_req=True)
        >>> result = thread.get()

        Args:
            id (str):
            fido_device_resource (Fido2DeviceResource): Payload with the data to replace in the existing device identified by the id param

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
            Fido2DeviceResource
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        kwargs['fido_device_resource'] = \
            fido_device_resource
        return self.update_fido2_device_by_id_endpoint.call_with_http_info(**kwargs)

