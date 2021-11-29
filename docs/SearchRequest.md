# SearchRequest

See section 3.4.3 of RFC 7644

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **[str]** |  | [optional] 
**attributes** | **[str]** | A list of attribute names to return in the response | [optional] 
**excluded_attributes** | **[str]** | When specified, the response will contain a default set of attributes minus those listed here | [optional] 
**filter** | **str** | An expression specifying the search criteria. See section 3.4.2.2 of RFC 7644 | [optional] 
**sort_by** | **str** | The attribute whose value will be used to order the returned responses | [optional] 
**sort_order** | **str** | Order in which the sortBy param is applied. Allowed values are \&quot;ascending\&quot; and \&quot;descending\&quot; | [optional] 
**start_index** | **int** | The 1-based index of the first query result | [optional] 
**count** | **int** | Specifies the desired maximum number of query results per page | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


