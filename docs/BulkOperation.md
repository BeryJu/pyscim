# BulkOperation

See section 3.7 of RFC 7644

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | [optional] 
**bulk_id** | **str** | Used to bind the id generated for a created resource (via POST) to a named variable for later reuse  | [optional] 
**path** | **str** | Path of the endpoint the operation uses relative to the server root, eg. /Users | [optional] 
**data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Payload associated to this operation | [optional] 
**location** | **str** | Used in responses of POST operations | [optional] 
**response** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**status** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


