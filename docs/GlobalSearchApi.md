# pyscim.GlobalSearchApi

All URIs are relative to *https://jenkins-ldap.jans.io/jans-scim/restv1/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_resources**](GlobalSearchApi.md#search_resources) | **POST** /.search | 


# **search_resources**
> GenericListResponse search_resources(search_request)



Search (from system root) for one or more resource (see section 3.4.3 of RFC 7644) 

### Example

* OAuth Authentication (scim_oauth):

```python
import time
import pyscim
from pyscim.api import global_search_api
from pyscim.model.search_request import SearchRequest
from pyscim.model.generic_list_response import GenericListResponse
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
    api_instance = global_search_api.GlobalSearchApi(api_client)
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
        api_response = api_instance.search_resources(search_request)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling GlobalSearchApi->search_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**SearchRequest**](SearchRequest.md)| Payload that represents the search criteria |

### Return type

[**GenericListResponse**](GenericListResponse.md)

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

