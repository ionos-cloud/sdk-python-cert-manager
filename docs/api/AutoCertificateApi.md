# AutoCertificateApi

All URIs are relative to *https://certificate-manager.de-fra.ionos.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**auto_certificates_delete**](AutoCertificateApi.md#auto_certificates_delete) | **DELETE** /auto-certificates/{autoCertificateId} | Delete AutoCertificate |
| [**auto_certificates_find_by_id**](AutoCertificateApi.md#auto_certificates_find_by_id) | **GET** /auto-certificates/{autoCertificateId} | Retrieve AutoCertificate |
| [**auto_certificates_get**](AutoCertificateApi.md#auto_certificates_get) | **GET** /auto-certificates | Retrieve all AutoCertificate |
| [**auto_certificates_patch**](AutoCertificateApi.md#auto_certificates_patch) | **PATCH** /auto-certificates/{autoCertificateId} | Updates AutoCertificate |
| [**auto_certificates_post**](AutoCertificateApi.md#auto_certificates_post) | **POST** /auto-certificates | Create AutoCertificate |


# **auto_certificates_delete**
> auto_certificates_delete(auto_certificate_id)

Delete AutoCertificate

Deletes the specified AutoCertificate.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **auto_certificate_id** | **str**| The ID (UUID) of the AutoCertificate. |  |

### Return type

void (empty response body)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **auto_certificates_find_by_id**
> AutoCertificateRead auto_certificates_find_by_id(auto_certificate_id)

Retrieve AutoCertificate

Returns the AutoCertificate by ID.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **auto_certificate_id** | **str**| The ID (UUID) of the AutoCertificate. |  |

### Return type

[**AutoCertificateRead**](../models/AutoCertificateRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **auto_certificates_get**
> AutoCertificateReadList auto_certificates_get(offset=offset, limit=limit, filter_common_name=filter_common_name)

Retrieve all AutoCertificate

This endpoint enables retrieving all AutoCertificate using pagination and optional filters. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100] |
| **filter_common_name** | **str**| Filter by the common name (DNS).  | [optional]  |

### Return type

[**AutoCertificateReadList**](../models/AutoCertificateReadList.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **auto_certificates_patch**
> AutoCertificateRead auto_certificates_patch(auto_certificate_id, auto_certificate_patch)

Updates AutoCertificate

Changes AutoCertificate with the provided ID. Values provides will replace the existing data. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **auto_certificate_id** | **str**| The ID (UUID) of the AutoCertificate. |  |
| **auto_certificate_patch** | [**AutoCertificatePatch**](../models/AutoCertificatePatch.md)| patch AutoCertificate |  |

### Return type

[**AutoCertificateRead**](../models/AutoCertificateRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **auto_certificates_post**
> AutoCertificateRead auto_certificates_post(auto_certificate_create)

Create AutoCertificate

Creates a new AutoCertificate.  The full AutoCertificate needs to be provided to create the object. Optional data will be filled with defaults or left empty. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **auto_certificate_create** | [**AutoCertificateCreate**](../models/AutoCertificateCreate.md)| AutoCertificate to create. |  |

### Return type

[**AutoCertificateRead**](../models/AutoCertificateRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

