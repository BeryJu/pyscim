# GroupResource

Represents a group resource. See section 4.2 of RFC 7643

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **[str]** | URIs that are used to indicate the namespaces of the SCIM schemas that define the attributes present in the current structure | [optional] 
**id** | **str** | A unique identifier for a SCIM resource. See section 3.1 of RFC 7643 | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**display_name** | **str** | Group name suitable for display to end-users | [optional] 
**members** | [**[Member]**](Member.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


