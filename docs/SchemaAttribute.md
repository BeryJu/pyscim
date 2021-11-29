# SchemaAttribute

A recursive definition. Note how property subAttributes reuses SchemaAttribute for its definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**sub_attributes** | [**[SchemaAttribute]**](SchemaAttribute.md) |  | [optional] 
**multi_valued** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**required** | **str** |  | [optional] 
**canonical_values** | **[str]** |  | [optional] 
**case_exact** | **bool** |  | [optional] 
**mutability** | **str** |  | [optional] 
**returned** | **str** |  | [optional] 
**uniqueness** | **str** |  | [optional] 
**reference_types** | **[str]** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


