# GenericResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **[str]** | URIs that are used to indicate the namespaces of the SCIM schemas that define the attributes present in the current structure | [optional] 
**id** | **str** | A unique identifier for a SCIM resource. See section 3.1 of RFC 7643 | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**display_name** | **str** | Device name suitable for display to end-users | [optional] 
**members** | [**[Member]**](Member.md) |  | [optional] 
**external_id** | **str** | Identifier of the resource useful from the perspective of the provisioning client. See section 3.1 of RFC 7643 | [optional] 
**user_name** | **str** | Identifier for the user, typically used by the user to directly authenticate (id and externalId are opaque identifiers generally not known by users) | [optional] 
**name** | [**Name**](Name.md) |  | [optional] 
**nick_name** | **str** | Casual way to address the user in real life | [optional] 
**profile_url** | **str** | URI pointing to a location representing the User&#39;s online profile | [optional] 
**title** | **str** |  | [optional] 
**user_type** | **str** | Used to identify the relationship between the organization and the user | [optional] 
**preferred_language** | **str** | Preferred language as used in the Accept-Language HTTP header | [optional] 
**locale** | **str** | Used for purposes of localizing items such as currency and dates | [optional] 
**timezone** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**password** | **str** |  | [optional] 
**emails** | [**[Email]**](Email.md) |  | [optional] 
**phone_numbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**ims** | [**[InstantMessagingAddress]**](InstantMessagingAddress.md) |  | [optional] 
**photos** | [**[Photo]**](Photo.md) |  | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**groups** | [**[Group]**](Group.md) |  | [optional] 
**entitlements** | [**[Entitlement]**](Entitlement.md) |  | [optional] 
**roles** | [**[Role]**](Role.md) |  | [optional] 
**x509_certificates** | [**[X509Certificate]**](X509Certificate.md) |  | [optional] 
**urnietfparamsscimschemasextensiongluu2_0_user** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Extended attributes | [optional] 
**user_id** | **str** | Identifies the owner of the enrollment | [optional] 
**creation_date** | **datetime** | Date of enrollment in ISO format | [optional] 
**application** | **str** | Associated U2F application ID | [optional] 
**counter** | **int** | Value used in the Fido 2 endpoints | [optional] 
**device_data** | **str** | A Json representation of low-level attributes of this enrollment | [optional] 
**device_hash_code** | **int** |  | [optional] 
**device_key_handle** | **str** |  | [optional] 
**device_registration_conf** | **str** |  | [optional] 
**last_access_time** | **datetime** | When this device was last used (eg. in order to log into an application) | [optional] 
**status** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


