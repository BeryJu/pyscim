# pyscim.DefaultApi

All URIs are relative to *https://jenkins-ldap.jans.io/jans-scim/restv1/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_post**](DefaultApi.md#bulk_post) | **POST** /Bulk | 


# **bulk_post**
> BulkData bulk_post(request)



Send several resource operations in a single request (see section 3.7 of RFC 7644)

### Example

* OAuth Authentication (scim_oauth):

```python
import time
import pyscim
from pyscim.api import default_api
from pyscim.model.bulk_data import BulkData
from pyscim.model.bulk_request import BulkRequest
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
    api_instance = default_api.DefaultApi(api_client)
    request = BulkRequest(None) # BulkRequest | Payload describing the operations to perform

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_post(request)
        pprint(api_response)
    except pyscim.ApiException as e:
        print("Exception when calling DefaultApi->bulk_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BulkRequest**](BulkRequest.md)| Payload describing the operations to perform |

### Return type

[**BulkData**](BulkData.md)

### Authorization

[scim_oauth](../README.md#scim_oauth)

### HTTP request headers

 - **Content-Type**: application/scim+json, application/json
 - **Accept**: application/scim+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. Every individual operation will report its own output status. Reponses are only included for failed operations.  |  -  |
**500** | There was an unexpected failure executing the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

