# Fido2DeviceResource

Represents a Fido 2 device enrollment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **[str]** | URIs that are used to indicate the namespaces of the SCIM schemas that define the attributes present in the current structure | [optional] 
**id** | **str** | A unique identifier for a SCIM resource. See section 3.1 of RFC 7643 | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**user_id** | **str** | Identifies the owner of the enrollment | [optional] 
**creation_date** | **datetime** | Date of enrollment in ISO format | [optional] 
**counter** | **int** | Value used in the Fido 2 endpoints | [optional] 
**status** | **str** |  | [optional] 
**display_name** | **str** | Device name suitable for display to end-users | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


