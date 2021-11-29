# PatchOperation

See section 3.5.2 of RFC 7644

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | The kind of operation to perform | 
**path** | **str** | Required when op is remove, optional otherwise | [optional] 
**value** | **bool, date, datetime, dict, float, int, list, str, none_type** | Can be any value - string, number, boolean, array or object | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


