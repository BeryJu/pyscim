# pyscim.UserApi

All URIs are relative to *https://jenkins-ldap.jans.io/jans-scim/restv1/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UserApi.md#create_user) | **POST** /Users | 
[**delete_user_by_id**](UserApi.md#delete_user_by_id) | **DELETE** /Users/{id} | 
[**get_user_by_id**](UserApi.md#get_user_by_id) | **GET** /Users/{id} | 
[**get_users**](UserApi.md#get_users) | **GET** /Users | 
[**patch_user_by_id**](UserApi.md#patch_user_by_id) | **PATCH** /Users/{id} | 
[**search_user**](UserApi.md#search_user) | **POST** /Users/.search | 
[**update_user_by_id**](UserApi.md#update_user_by_id) | **PUT** /Users/{id} | 


# **create_user**
> UserResource create_user(user)



Allows creating a User resource via POST (see section 3.3 of RFC 7644)

### Example

* OAuth Authentication (scim_oauth):

```python
import time
import pyscim
from pyscim.api import user_api
from pyscim.model.user_resource import UserResource
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
    api_instance = user_api.UserApi(api_client)
    user = UserResource(None) # UserResource | Payload that represents the Group to create
    attributes = "attributes_example" # str | A comma-separated list of attribute names to return in the response (optional)
    excluded_attributes = "excludedAttributes_example" # str | When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list) (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_user(user)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling UserApi->create_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_user(user, attributes=attributes, excluded_attributes=excluded_attributes)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling UserApi->create_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**UserResource**](UserResource.md)| Payload that represents the Group to create |
 **attributes** | **str**| A comma-separated list of attribute names to return in the response | [optional]
 **excluded_attributes** | **str**| When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list) | [optional]

### Return type

[**UserResource**](UserResource.md)

### Authorization

[scim_oauth](../README.md#scim_oauth)

### HTTP request headers

 - **Content-Type**: application/scim+json, application/json
 - **Accept**: application/scim+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | An invalid value was passed in the payload |  -  |
**409** | There is a conflict with an already existing user. Uniqueness is assumed over userName |  -  |
**500** | There was an unexpected failure executing the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_by_id**
> delete_user_by_id(id)



Deletes a user resource

### Example

* OAuth Authentication (scim_oauth):

```python
import time
import pyscim
from pyscim.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    id = "id_example" # str | Identifier of the resource to delete

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_user_by_id(id)
    except pyscim.ApiException as e:
        print("Exception when calling UserApi->delete_user_by_id: %s\n" % e)
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

# **get_user_by_id**
> UserResource get_user_by_id(id)



Retrieves a User resource by Id (see section 3.4.1 of RFC 7644)

### Example

* OAuth Authentication (scim_oauth):

```python
import time
import pyscim
from pyscim.api import user_api
from pyscim.model.user_resource import UserResource
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
    api_instance = user_api.UserApi(api_client)
    id = "id_example" # str | 
    attributes = "attributes_example" # str | A comma-separated list of attribute names to return in the response (optional)
    excluded_attributes = "excludedAttributes_example" # str | When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list) (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_user_by_id(id)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling UserApi->get_user_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_user_by_id(id, attributes=attributes, excluded_attributes=excluded_attributes)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling UserApi->get_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **attributes** | **str**| A comma-separated list of attribute names to return in the response | [optional]
 **excluded_attributes** | **str**| When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list) | [optional]

### Return type

[**UserResource**](UserResource.md)

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

# **get_users**
> UserListResponse get_users()



Query User resources (see section 3.4.2 of RFC 7644)

### Example

* OAuth Authentication (scim_oauth):

```python
import time
import pyscim
from pyscim.api import user_api
from pyscim.model.user_list_response import UserListResponse
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
    api_instance = user_api.UserApi(api_client)
    attributes = "attributes_example" # str | A comma-separated list of attribute names to return in the response (optional)
    excluded_attributes = "excludedAttributes_example" # str | When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list) (optional)
    filter = "userName eq "jhon" and meta.lastModified gt "2011-05-13T04:42:34Z"" # str | An expression specifying the search criteria. See section 3.4.2.2 of RFC 7644 (optional)
    start_index = 1 # int | The 1-based index of the first query result (optional)
    count = 1 # int | Specifies the desired maximum number of query results per page (optional)
    sort_by = "sortBy_example" # str | The attribute whose value will be used to order the returned responses (optional)
    sort_order = "sortOrder_example" # str | Order in which the sortBy param is applied. Allowed values are \"ascending\" and \"descending\" (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_users(attributes=attributes, excluded_attributes=excluded_attributes, filter=filter, start_index=start_index, count=count, sort_by=sort_by, sort_order=sort_order)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling UserApi->get_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attributes** | **str**| A comma-separated list of attribute names to return in the response | [optional]
 **excluded_attributes** | **str**| When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list) | [optional]
 **filter** | **str**| An expression specifying the search criteria. See section 3.4.2.2 of RFC 7644 | [optional]
 **start_index** | **int**| The 1-based index of the first query result | [optional]
 **count** | **int**| Specifies the desired maximum number of query results per page | [optional]
 **sort_by** | **str**| The attribute whose value will be used to order the returned responses | [optional]
 **sort_order** | **str**| Order in which the sortBy param is applied. Allowed values are \&quot;ascending\&quot; and \&quot;descending\&quot; | [optional]

### Return type

[**UserListResponse**](UserListResponse.md)

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
**500** | There was an unexpected failure executing the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_user_by_id**
> UserResource patch_user_by_id(id, request)



Updates one or more attributes of a User resource using a sequence of additions, removals, and  replacements operations. See section 3.5.2 of RFC 7644 

### Example

* OAuth Authentication (scim_oauth):

```python
import time
import pyscim
from pyscim.api import user_api
from pyscim.model.patch_request import PatchRequest
from pyscim.model.user_resource import UserResource
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
    api_instance = user_api.UserApi(api_client)
    id = "id_example" # str | 
    request = PatchRequest(
        schemas=[
            "urn:ietf:params:scim:api:messages:2.0:PatchOp",
        ],
        operations=[
            PatchOperation(
                op="add",
                path="path_example",
                value=None,
            ),
        ],
    ) # PatchRequest | Payload describing the patch operations to apply upon the resource identified by param id
    attributes = "attributes_example" # str | A comma-separated list of attribute names to return in the response (optional)
    excluded_attributes = "excludedAttributes_example" # str | When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list) (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_user_by_id(id, request)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling UserApi->patch_user_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_user_by_id(id, request, attributes=attributes, excluded_attributes=excluded_attributes)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling UserApi->patch_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **request** | [**PatchRequest**](PatchRequest.md)| Payload describing the patch operations to apply upon the resource identified by param id |
 **attributes** | **str**| A comma-separated list of attribute names to return in the response | [optional]
 **excluded_attributes** | **str**| When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list) | [optional]

### Return type

[**UserResource**](UserResource.md)

### Authorization

[scim_oauth](../README.md#scim_oauth)

### HTTP request headers

 - **Content-Type**: application/scim+json, application/json
 - **Accept**: application/scim+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | One or more operations supplied in the request are specified incorrectly, there were attempts to modify immutable attributes, or the resulting resource cannot pass intrinsic validations  |  -  |
**500** | There was an unexpected failure executing the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_user**
> UserListResponse search_user(search_request)



Query User resources (see section 3.4.2 of RFC 7644)

### Example

* OAuth Authentication (scim_oauth):

```python
import time
import pyscim
from pyscim.api import user_api
from pyscim.model.search_request import SearchRequest
from pyscim.model.user_list_response import UserListResponse
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
    api_instance = user_api.UserApi(api_client)
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

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.search_user(search_request)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling UserApi->search_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**SearchRequest**](SearchRequest.md)| Payload that represents the search criteria |

### Return type

[**UserListResponse**](UserListResponse.md)

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
**500** | There was an unexpected failure executing the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_by_id**
> UserResource update_user_by_id(id, user)



Updates a User resource (see section 3.5.1 of RFC 7644). Update works in a replacement fashion&amp;#58; every attribute value found in the payload sent will replace the one in the existing resource representation. Attributes  not passed in the payload will be left intact. 

### Example

* OAuth Authentication (scim_oauth):

```python
import time
import pyscim
from pyscim.api import user_api
from pyscim.model.user_resource import UserResource
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
    api_instance = user_api.UserApi(api_client)
    id = "id_example" # str | 
    user = UserResource(None) # UserResource | Payload with the data to replace in the existing user identified by the id param
    attributes = "attributes_example" # str | A comma-separated list of attribute names to return in the response (optional)
    excluded_attributes = "excludedAttributes_example" # str | When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list) (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_user_by_id(id, user)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling UserApi->update_user_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_user_by_id(id, user, attributes=attributes, excluded_attributes=excluded_attributes)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling UserApi->update_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **user** | [**UserResource**](UserResource.md)| Payload with the data to replace in the existing user identified by the id param |
 **attributes** | **str**| A comma-separated list of attribute names to return in the response | [optional]
 **excluded_attributes** | **str**| When specified, the response will contain a default set of attributes minus those listed here (as a comma-separated list) | [optional]

### Return type

[**UserResource**](UserResource.md)

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
**409** | There is a conflict with an already existing group. Uniqueness is assumed over displayName |  -  |
**500** | There was an unexpected failure executing the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

