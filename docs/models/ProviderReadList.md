# ProviderReadList

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **id** | **str** | ID of the list of Provider resources. |  |
| **type** | **str** | The type of the resource. |  |
| **href** | **str** | The URL of the list of Provider resources. |  |
| **items** | [**list[ProviderRead]**](ProviderRead.md) | The list of Provider resources. | [optional]  |
| **offset** | **int** | The offset specified in the request (if none was specified, the default offset is 0).  | [readonly]  |
| **limit** | **int** | The limit specified in the request (if none was specified, use the endpoint&#39;s default pagination limit).  | [readonly]  |
| **links** | [**Links**](Links.md) |  |  |


