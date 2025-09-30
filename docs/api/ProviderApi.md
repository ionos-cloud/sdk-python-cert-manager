# ProviderApi

All URIs are relative to *https://certificate-manager.de-fra.ionos.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**providers_delete**](ProviderApi.md#providers_delete) | **DELETE** /providers/{providerId} | Delete Provider |
| [**providers_find_by_id**](ProviderApi.md#providers_find_by_id) | **GET** /providers/{providerId} | Retrieve Provider |
| [**providers_get**](ProviderApi.md#providers_get) | **GET** /providers | Retrieve all Provider |
| [**providers_patch**](ProviderApi.md#providers_patch) | **PATCH** /providers/{providerId} | Updates Provider |
| [**providers_post**](ProviderApi.md#providers_post) | **POST** /providers | Create Provider |


# **providers_delete**
> providers_delete(provider_id)

Delete Provider

Deletes the specified Provider.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider_id** | **str**| The ID (UUID) of the Provider. |  |

### Return type

void (empty response body)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **providers_find_by_id**
> ProviderRead providers_find_by_id(provider_id)

Retrieve Provider

Returns the Provider by ID.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider_id** | **str**| The ID (UUID) of the Provider. |  |

### Return type

[**ProviderRead**](../models/ProviderRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **providers_get**
> ProviderReadList providers_get(offset=offset, limit=limit)

Retrieve all Provider

This endpoint enables retrieving all Provider using pagination and optional filters. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100] |

### Return type

[**ProviderReadList**](../models/ProviderReadList.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **providers_patch**
> ProviderRead providers_patch(provider_id, provider_patch)

Updates Provider

Changes Provider with the provided ID. Values provides will replace the existing data. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider_id** | **str**| The ID (UUID) of the Provider. |  |
| **provider_patch** | [**ProviderPatch**](../models/ProviderPatch.md)| patch Provider |  |

### Return type

[**ProviderRead**](../models/ProviderRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **providers_post**
> ProviderRead providers_post(provider_create)

Create Provider

Creates a new Provider.  The full Provider needs to be provided to create the object. Optional data will be filled with defaults or left empty. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider_create** | [**ProviderCreate**](../models/ProviderCreate.md)| Provider to create. |  |

### Return type

[**ProviderRead**](../models/ProviderRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

