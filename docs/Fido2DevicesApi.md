# pyscim.Fido2DevicesApi

All URIs are relative to *https://jenkins-ldap.jans.io/jans-scim/restv1/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_fido2_device_by_id**](Fido2DevicesApi.md#delete_fido2_device_by_id) | **DELETE** /Fido2Devices/{id} | 
[**get_fido2_device_by_id**](Fido2DevicesApi.md#get_fido2_device_by_id) | **GET** /Fido2Devices/{id} | 
[**get_fido2_devices**](Fido2DevicesApi.md#get_fido2_devices) | **GET** /Fido2Devices | 
[**search_fido2_device**](Fido2DevicesApi.md#search_fido2_device) | **POST** /Fido2Devices/.search | 
[**update_fido2_device_by_id**](Fido2DevicesApi.md#update_fido2_device_by_id) | **PUT** /Fido2Devices/{id} | 


# **delete_fido2_device_by_id**
> delete_fido2_device_by_id(id)



Deletes a Fido 2 resource

### Example

* OAuth Authentication (scim_oauth):

```python
import time
import pyscim
from pyscim.api import fido2_devices_api
from pyscim.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://jenkins-ldap.jans.io/jans-scim/restv1/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pyscim.Configuration(
    host = "https://jenkins-ldap.jans.io/jans-scim/restv1/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: scim_oauth
configuration = pyscim.Configuration(
    host = "https://jenkins-ldap.jans.io/jans-scim/restv1/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pyscim.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fido2_devices_api.Fido2DevicesApi(api_client)
    id = "id_example" # str | Identifier of the resource to delete

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_fido2_device_by_id(id)
    except pyscim.ApiException as e:
        print("Exception when calling Fido2DevicesApi->delete_fido2_device_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the resource to delete |

### Return type

void (empty response body)

### Authorization

[scim_oauth](../README.md#scim_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful operation. Empty response |  -  |
**404** | Id passed unknown |  -  |
**500** | There was an unexpected failure executing the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fido2_device_by_id**
> Fido2DeviceResource get_fido2_device_by_id(id)



Retrieves a Fido 2 device by Id

### Example

* OAuth Authentication (scim_oauth):

```python
import time
import pyscim
from pyscim.api import fido2_devices_api
from pyscim.model.fido2_device_resource import Fido2DeviceResource
from pyscim.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://jenkins-ldap.jans.io/jans-scim/restv1/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pyscim.Configuration(
    host = "https://jenkins-ldap.jans.io/jans-scim/restv1/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: scim_oauth
configuration = pyscim.Configuration(
    host = "https://jenkins-ldap.jans.io/jans-scim/restv1/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pyscim.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fido2_devices_api.Fido2DevicesApi(api_client)
    id = "id_example" # str | 
    attributes = "attributes_example" # str | A comma-separated list of attribute names to return in the response (optional)
    excluded_attributes = "excludedAttributes_example" # str | When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list) (optional)
    user_id = "userId_example" # str | Identifier (inum) of the device owner. This param is not required when underlying database is LDAP (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_fido2_device_by_id(id)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling Fido2DevicesApi->get_fido2_device_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_fido2_device_by_id(id, attributes=attributes, excluded_attributes=excluded_attributes, user_id=user_id)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling Fido2DevicesApi->get_fido2_device_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **attributes** | **str**| A comma-separated list of attribute names to return in the response | [optional]
 **excluded_attributes** | **str**| When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list) | [optional]
 **user_id** | **str**| Identifier (inum) of the device owner. This param is not required when underlying database is LDAP | [optional]

### Return type

[**Fido2DeviceResource**](Fido2DeviceResource.md)

### Authorization

[scim_oauth](../README.md#scim_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | Id passed unknown |  -  |
**500** | There was an unexpected failure executing the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fido2_devices**
> Fido2ListResponse get_fido2_devices()



Query Fido 2 resources

### Example

* OAuth Authentication (scim_oauth):

```python
import time
import pyscim
from pyscim.api import fido2_devices_api
from pyscim.model.fido2_list_response import Fido2ListResponse
from pyscim.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://jenkins-ldap.jans.io/jans-scim/restv1/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pyscim.Configuration(
    host = "https://jenkins-ldap.jans.io/jans-scim/restv1/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: scim_oauth
configuration = pyscim.Configuration(
    host = "https://jenkins-ldap.jans.io/jans-scim/restv1/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pyscim.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fido2_devices_api.Fido2DevicesApi(api_client)
    attributes = "attributes_example" # str | A comma-separated list of attribute names to return in the response (optional)
    excluded_attributes = "excludedAttributes_example" # str | When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list) (optional)
    user_id = "userId_example" # str | Used to restrict the search to fido 2 resources owned by a specific user (optional)
    filter = "userId sw "123-abcde-qwerty"" # str | An expression specifying the search criteria. See section 3.4.2.2 of RFC 7644 (optional)
    start_index = 1 # int | The 1-based index of the first query result (optional)
    count = 1 # int | Specifies the desired maximum number of query results per page (optional)
    sort_by = "sortBy_example" # str | The attribute whose value will be used to order the returned responses (optional)
    sort_order = "sortOrder_example" # str | Order in which the sortBy param is applied. Allowed values are \"ascending\" and \"descending\" (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_fido2_devices(attributes=attributes, excluded_attributes=excluded_attributes, user_id=user_id, filter=filter, start_index=start_index, count=count, sort_by=sort_by, sort_order=sort_order)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling Fido2DevicesApi->get_fido2_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attributes** | **str**| A comma-separated list of attribute names to return in the response | [optional]
 **excluded_attributes** | **str**| When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list) | [optional]
 **user_id** | **str**| Used to restrict the search to fido 2 resources owned by a specific user | [optional]
 **filter** | **str**| An expression specifying the search criteria. See section 3.4.2.2 of RFC 7644 | [optional]
 **start_index** | **int**| The 1-based index of the first query result | [optional]
 **count** | **int**| Specifies the desired maximum number of query results per page | [optional]
 **sort_by** | **str**| The attribute whose value will be used to order the returned responses | [optional]
 **sort_order** | **str**| Order in which the sortBy param is applied. Allowed values are \&quot;ascending\&quot; and \&quot;descending\&quot; | [optional]

### Return type

[**Fido2ListResponse**](Fido2ListResponse.md)

### Authorization

[scim_oauth](../README.md#scim_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Parameter count exceeds the maximum allowed value or the filter supplied was unparsable |  -  |
**404** | If userId param was supplied and the user is not known |  -  |
**500** | There was an unexpected failure executing the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_fido2_device**
> Fido2ListResponse search_fido2_device(search_request)



Query Fido 2 resources

### Example

* OAuth Authentication (scim_oauth):

```python
import time
import pyscim
from pyscim.api import fido2_devices_api
from pyscim.model.search_request import SearchRequest
from pyscim.model.fido2_list_response import Fido2ListResponse
from pyscim.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://jenkins-ldap.jans.io/jans-scim/restv1/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pyscim.Configuration(
    host = "https://jenkins-ldap.jans.io/jans-scim/restv1/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: scim_oauth
configuration = pyscim.Configuration(
    host = "https://jenkins-ldap.jans.io/jans-scim/restv1/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pyscim.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fido2_devices_api.Fido2DevicesApi(api_client)
    search_request = SearchRequest(
        schemas=[
            "urn:ietf:params:scim:api:messages:2.0:SearchRequest",
        ],
        attributes=[
            "attributes_example",
        ],
        excluded_attributes=[
            "excluded_attributes_example",
        ],
        filter="userName eq "jhon" and meta.lastModified gt "2011-05-13T04:42:34Z"",
        sort_by="sort_by_example",
        sort_order="sort_order_example",
        start_index=1,
        count=1,
    ) # SearchRequest | Payload that represents the search criteria
    user_id = "userId_example" # str | Used to restrict the search to fido 2 resources owned by a specific user (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.search_fido2_device(search_request)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling Fido2DevicesApi->search_fido2_device: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_fido2_device(search_request, user_id=user_id)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling Fido2DevicesApi->search_fido2_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**SearchRequest**](SearchRequest.md)| Payload that represents the search criteria |
 **user_id** | **str**| Used to restrict the search to fido 2 resources owned by a specific user | [optional]

### Return type

[**Fido2ListResponse**](Fido2ListResponse.md)

### Authorization

[scim_oauth](../README.md#scim_oauth)

### HTTP request headers

 - **Content-Type**: application/scim+json, application/json
 - **Accept**: application/scim+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Parameter count exceeds the maximum allowed value, the filter supplied was unparsable, or invalid schema in search request  |  -  |
**404** | If userId param was supplied and the user is not known |  -  |
**500** | There was an unexpected failure executing the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fido2_device_by_id**
> Fido2DeviceResource update_fido2_device_by_id(id, fido_device_resource)



Updates a Fido 2 resource. Update works in a replacement fashion&amp;#58; every attribute value found in the payload sent will replace the one in the existing resource representation. Attributes  not passed in the payload will be left intact. 

### Example

* OAuth Authentication (scim_oauth):

```python
import time
import pyscim
from pyscim.api import fido2_devices_api
from pyscim.model.fido2_device_resource import Fido2DeviceResource
from pyscim.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://jenkins-ldap.jans.io/jans-scim/restv1/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pyscim.Configuration(
    host = "https://jenkins-ldap.jans.io/jans-scim/restv1/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: scim_oauth
configuration = pyscim.Configuration(
    host = "https://jenkins-ldap.jans.io/jans-scim/restv1/v2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pyscim.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fido2_devices_api.Fido2DevicesApi(api_client)
    id = "id_example" # str | 
    fido_device_resource = Fido2DeviceResource(None) # Fido2DeviceResource | Payload with the data to replace in the existing device identified by the id param
    attributes = "attributes_example" # str | A comma-separated list of attribute names to return in the response (optional)
    excluded_attributes = "excludedAttributes_example" # str | When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list) (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_fido2_device_by_id(id, fido_device_resource)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling Fido2DevicesApi->update_fido2_device_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_fido2_device_by_id(id, fido_device_resource, attributes=attributes, excluded_attributes=excluded_attributes)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling Fido2DevicesApi->update_fido2_device_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **fido_device_resource** | [**Fido2DeviceResource**](Fido2DeviceResource.md)| Payload with the data to replace in the existing device identified by the id param |
 **attributes** | **str**| A comma-separated list of attribute names to return in the response | [optional]
 **excluded_attributes** | **str**| When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list) | [optional]

### Return type

[**Fido2DeviceResource**](Fido2DeviceResource.md)

### Authorization

[scim_oauth](../README.md#scim_oauth)

### HTTP request headers

 - **Content-Type**: application/scim+json, application/json
 - **Accept**: application/scim+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | An invalid value was passed in the payload or there was an attempt to update an immutable attribute  |  -  |
**404** | Id passed unknown |  -  |
**500** | There was an unexpected failure executing the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

