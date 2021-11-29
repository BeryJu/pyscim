# pyscim.DiscoveryApi

All URIs are relative to *https://jenkins-ldap.jans.io/jans-scim/restv1/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_resource_type_by_id**](DiscoveryApi.md#get_resource_type_by_id) | **GET** /ResourceTypes/{resource} | 
[**get_resource_types**](DiscoveryApi.md#get_resource_types) | **GET** /ResourceTypes | 
[**get_schema_by_uri**](DiscoveryApi.md#get_schema_by_uri) | **GET** /Schemas/{uri} | 
[**get_schemas**](DiscoveryApi.md#get_schemas) | **GET** /Schemas | 
[**get_service_provider_config**](DiscoveryApi.md#get_service_provider_config) | **GET** /ServiceProviderConfig | 


# **get_resource_type_by_id**
> ResourceType get_resource_type_by_id(resource)



Describes the endpoint, schemas and extensions supported by a specific kind of resource. It returns a specific portion of the ouput of the more general /Resources endpoint   

### Example


```python
import time
import pyscim
from pyscim.api import discovery_api
from pyscim.model.resource_type import ResourceType
from pyscim.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://jenkins-ldap.jans.io/jans-scim/restv1/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pyscim.Configuration(
    host = "https://jenkins-ldap.jans.io/jans-scim/restv1/v2"
)


# Enter a context with an instance of the API client
with pyscim.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = discovery_api.DiscoveryApi(api_client)
    resource = "User" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_resource_type_by_id(resource)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling DiscoveryApi->get_resource_type_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  |

### Return type

[**ResourceType**](ResourceType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**500** | There was an unexpected failure executing the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_types**
> ResourceTypeListResponse get_resource_types()



This endpoint is used to discover the types of resources available (see section 4 of RFC 7644) 

### Example


```python
import time
import pyscim
from pyscim.api import discovery_api
from pyscim.model.resource_type_list_response import ResourceTypeListResponse
from pyscim.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://jenkins-ldap.jans.io/jans-scim/restv1/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pyscim.Configuration(
    host = "https://jenkins-ldap.jans.io/jans-scim/restv1/v2"
)


# Enter a context with an instance of the API client
with pyscim.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = discovery_api.DiscoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_resource_types()
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling DiscoveryApi->get_resource_types: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceTypeListResponse**](ResourceTypeListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**500** | There was an unexpected failure executing the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema_by_uri**
> SchemaResource get_schema_by_uri(uri)



Retrieves information about a specific resource

### Example


```python
import time
import pyscim
from pyscim.api import discovery_api
from pyscim.model.schema_resource import SchemaResource
from pyscim.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://jenkins-ldap.jans.io/jans-scim/restv1/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pyscim.Configuration(
    host = "https://jenkins-ldap.jans.io/jans-scim/restv1/v2"
)


# Enter a context with an instance of the API client
with pyscim.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = discovery_api.DiscoveryApi(api_client)
    uri = "urn:ietf:params:scim:schemas:core:2.0:User" # str | Schema URI of a particular resource type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_schema_by_uri(uri)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling DiscoveryApi->get_schema_by_uri: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Schema URI of a particular resource type |

### Return type

[**SchemaResource**](SchemaResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**500** | There was an unexpected failure executing the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schemas**
> SchemaListResponse get_schemas()



Endpoint used to retrieve information about schemas supported (see section  4 of RFC 7644) 

### Example


```python
import time
import pyscim
from pyscim.api import discovery_api
from pyscim.model.schema_list_response import SchemaListResponse
from pyscim.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://jenkins-ldap.jans.io/jans-scim/restv1/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pyscim.Configuration(
    host = "https://jenkins-ldap.jans.io/jans-scim/restv1/v2"
)


# Enter a context with an instance of the API client
with pyscim.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = discovery_api.DiscoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_schemas()
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling DiscoveryApi->get_schemas: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SchemaListResponse**](SchemaListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**500** | There was an unexpected failure executing the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_provider_config**
> ServiceProviderConfigResponse get_service_provider_config()



Describes the SCIM specification features available (see section 5 of RFC 7644)

### Example


```python
import time
import pyscim
from pyscim.api import discovery_api
from pyscim.model.service_provider_config_response import ServiceProviderConfigResponse
from pyscim.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://jenkins-ldap.jans.io/jans-scim/restv1/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pyscim.Configuration(
    host = "https://jenkins-ldap.jans.io/jans-scim/restv1/v2"
)


# Enter a context with an instance of the API client
with pyscim.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = discovery_api.DiscoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_service_provider_config()
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling DiscoveryApi->get_service_provider_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceProviderConfigResponse**](ServiceProviderConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**500** | There was an unexpected failure executing the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

