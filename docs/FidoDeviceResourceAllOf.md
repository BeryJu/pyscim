# FidoDeviceResourceAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Identifies the owner of the enrollment | [optional] 
**creation_date** | **datetime** | Date of enrollment in ISO format | [optional] 
**application** | **str** | Associated U2F application ID | [optional] 
**counter** | **int** | Value used in the Fido U2F endpoints | [optional] 
**device_data** | **str** | A Json representation of low-level attributes of this enrollment | [optional] 
**device_hash_code** | **int** |  | [optional] 
**device_key_handle** | **str** |  | [optional] 
**device_registration_conf** | **str** |  | [optional] 
**last_access_time** | **datetime** | When this device was last used (eg. in order to log into an application) | [optional] 
**status** | **str** |  | [optional] 
**display_name** | **str** | Device name suitable for display to end-users | [optional] 
**description** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


