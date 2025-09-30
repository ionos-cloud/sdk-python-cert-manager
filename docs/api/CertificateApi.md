# CertificateApi

All URIs are relative to *https://certificate-manager.de-fra.ionos.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**certificates_delete**](CertificateApi.md#certificates_delete) | **DELETE** /certificates/{certificateId} | Delete Certificate |
| [**certificates_find_by_id**](CertificateApi.md#certificates_find_by_id) | **GET** /certificates/{certificateId} | Retrieve Certificate |
| [**certificates_get**](CertificateApi.md#certificates_get) | **GET** /certificates | Retrieve all Certificate |
| [**certificates_patch**](CertificateApi.md#certificates_patch) | **PATCH** /certificates/{certificateId} | Updates Certificate |
| [**certificates_post**](CertificateApi.md#certificates_post) | **POST** /certificates | Create Certificate |


# **certificates_delete**
> certificates_delete(certificate_id)

Delete Certificate

Deletes the specified Certificate.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **certificate_id** | **str**| The ID (UUID) of the Certificate. |  |

### Return type

void (empty response body)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **certificates_find_by_id**
> CertificateRead certificates_find_by_id(certificate_id)

Retrieve Certificate

Returns the Certificate by ID.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **certificate_id** | **str**| The ID (UUID) of the Certificate. |  |

### Return type

[**CertificateRead**](../models/CertificateRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **certificates_get**
> CertificateReadList certificates_get(offset=offset, limit=limit, filter_common_name=filter_common_name, filter_auto_certificate=filter_auto_certificate)

Retrieve all Certificate

This endpoint enables retrieving all Certificate using pagination and optional filters. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100] |
| **filter_common_name** | **str**| Filter by the common name (DNS).  | [optional]  |
| **filter_auto_certificate** | **str**| Filter by autoCertificateID.  | [optional]  |

### Return type

[**CertificateReadList**](../models/CertificateReadList.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **certificates_patch**
> CertificateRead certificates_patch(certificate_id, certificate_patch)

Updates Certificate

Changes Certificate with the provided ID. Values provides will replace the existing data. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **certificate_id** | **str**| The ID (UUID) of the Certificate. |  |
| **certificate_patch** | [**CertificatePatch**](../models/CertificatePatch.md)| patch Certificate |  |

### Return type

[**CertificateRead**](../models/CertificateRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **certificates_post**
> CertificateRead certificates_post(certificate_create)

Create Certificate

Creates a new Certificate.  The full Certificate needs to be provided to create the object. Optional data will be filled with defaults or left empty. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **certificate_create** | [**CertificateCreate**](../models/CertificateCreate.md)| Certificate to create. |  |

### Return type

[**CertificateRead**](../models/CertificateRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

