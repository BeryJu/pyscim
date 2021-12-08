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
from pyscim.model.resource_type import ResourceType
from pyscim.model.resource_type_list_response import ResourceTypeListResponse
from pyscim.model.schema_list_response import SchemaListResponse
from pyscim.model.schema_resource import SchemaResource
from pyscim.model.service_provider_config_response import ServiceProviderConfigResponse


class DiscoveryApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_resource_type_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (ResourceType,),
                'auth': [],
                'endpoint_path': '/ResourceTypes/{resource}',
                'operation_id': 'get_resource_type_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'resource',
                ],
                'required': [
                    'resource',
                ],
                'nullable': [
                ],
                'enum': [
                    'resource',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('resource',): {

                        "USER": "User",
                        "GROUP": "Group",
                        "FIDODEVICE": "FidoDevice",
                        "FIDO2DEVICE": "Fido2Device"
                    },
                },
                'openapi_types': {
                    'resource':
                        (str,),
                },
                'attribute_map': {
                    'resource': 'resource',
                },
                'location_map': {
                    'resource': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/scim+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_resource_types_endpoint = _Endpoint(
            settings={
                'response_type': (ResourceTypeListResponse,),
                'auth': [],
                'endpoint_path': '/ResourceTypes',
                'operation_id': 'get_resource_types',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
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
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/scim+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_schema_by_uri_endpoint = _Endpoint(
            settings={
                'response_type': (SchemaResource,),
                'auth': [],
                'endpoint_path': '/Schemas/{uri}',
                'operation_id': 'get_schema_by_uri',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'uri',
                ],
                'required': [
                    'uri',
                ],
                'nullable': [
                ],
                'enum': [
                    'uri',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('uri',): {

                        "CORE:2.0:USER": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "EXTENSION:GLUU:2.0:USER": "urn:ietf:params:scim:schemas:extension:gluu:2.0:User",
                        "CORE:2.0:GROUP": "urn:ietf:params:scim:schemas:core:2.0:Group",
                        "CORE:2.0:FIDO2DEVICE": "urn:ietf:params:scim:schemas:core:2.0:Fido2Device",
                        "CORE:2.0:FIDODEVICE": "urn:ietf:params:scim:schemas:core:2.0:FidoDevice"
                    },
                },
                'openapi_types': {
                    'uri':
                        (str,),
                },
                'attribute_map': {
                    'uri': 'uri',
                },
                'location_map': {
                    'uri': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/scim+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_schemas_endpoint = _Endpoint(
            settings={
                'response_type': (SchemaListResponse,),
                'auth': [],
                'endpoint_path': '/Schemas',
                'operation_id': 'get_schemas',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
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
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/scim+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_service_provider_config_endpoint = _Endpoint(
            settings={
                'response_type': (ServiceProviderConfigResponse,),
                'auth': [],
                'endpoint_path': '/ServiceProviderConfig',
                'operation_id': 'get_service_provider_config',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
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
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/scim+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_resource_type_by_id(
        self,
        resource,
        **kwargs
    ):
        """get_resource_type_by_id  # noqa: E501

        Describes the endpoint, schemas and extensions supported by a specific kind of resource. It returns a specific portion of the ouput of the more general /Resources endpoint     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_resource_type_by_id(resource, async_req=True)
        >>> result = thread.get()

        Args:
            resource (str):

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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ResourceType
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['resource'] = \
            resource
        return self.get_resource_type_by_id_endpoint.call_with_http_info(**kwargs)

    def get_resource_types(
        self,
        **kwargs
    ):
        """get_resource_types  # noqa: E501

        This endpoint is used to discover the types of resources available (see section 4 of RFC 7644)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_resource_types(async_req=True)
        >>> result = thread.get()


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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ResourceTypeListResponse
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.get_resource_types_endpoint.call_with_http_info(**kwargs)

    def get_schema_by_uri(
        self,
        uri,
        **kwargs
    ):
        """get_schema_by_uri  # noqa: E501

        Retrieves information about a specific resource  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_schema_by_uri(uri, async_req=True)
        >>> result = thread.get()

        Args:
            uri (str): Schema URI of a particular resource type

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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            SchemaResource
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['uri'] = \
            uri
        return self.get_schema_by_uri_endpoint.call_with_http_info(**kwargs)

    def get_schemas(
        self,
        **kwargs
    ):
        """get_schemas  # noqa: E501

        Endpoint used to retrieve information about schemas supported (see section  4 of RFC 7644)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_schemas(async_req=True)
        >>> result = thread.get()


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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            SchemaListResponse
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.get_schemas_endpoint.call_with_http_info(**kwargs)

    def get_service_provider_config(
        self,
        **kwargs
    ):
        """get_service_provider_config  # noqa: E501

        Describes the SCIM specification features available (see section 5 of RFC 7644)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_service_provider_config(async_req=True)
        >>> result = thread.get()


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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ServiceProviderConfigResponse
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.get_service_provider_config_endpoint.call_with_http_info(**kwargs)

