# CertificatesApi

All URIs are relative to *https://api.ionos.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**certificates_delete**](CertificatesApi.md#certificates_delete) | **DELETE** /certificatemanager/certificates/{certificateId} | Delete a Certificate by ID |
| [**certificates_get**](CertificatesApi.md#certificates_get) | **GET** /certificatemanager/certificates | Get Certificates |
| [**certificates_get_by_id**](CertificatesApi.md#certificates_get_by_id) | **GET** /certificatemanager/certificates/{certificateId} | Get a Certificate by ID |
| [**certificates_patch**](CertificatesApi.md#certificates_patch) | **PATCH** /certificatemanager/certificates/{certificateId} | Update a Certificate Name by ID |
| [**certificates_post**](CertificatesApi.md#certificates_post) | **POST** /certificatemanager/certificates | Add a New Certificate |


# **certificates_delete**
> certificates_delete(certificate_id)

Delete a Certificate by ID

Deletes a certificate specified by its ID.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_cert_manager
from ionoscloud_cert_manager.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com
configuration = ionoscloud_cert_manager.Configuration(
    host = 'https://api.ionos.com',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_cert_manager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_cert_manager.CertificatesApi(api_client)
    certificate_id = 'certificate_id_example' # str | 
    try:
        # Delete a Certificate by ID
        api_instance.certificates_delete(certificate_id)
    except ApiException as e:
        print('Exception when calling CertificatesApi.certificates_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **certificate_id** | **str**|  |  |

### Return type

void (empty response body)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

# **certificates_get**
> CertificateCollectionDto certificates_get(offset=offset, limit=limit)

Get Certificates

Retrieves all available certificates.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_cert_manager
from ionoscloud_cert_manager.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com
configuration = ionoscloud_cert_manager.Configuration(
    host = 'https://api.ionos.com',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_cert_manager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_cert_manager.CertificatesApi(api_client)
    try:
        # Get Certificates
        api_response = api_instance.certificates_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling CertificatesApi.certificates_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **offset** | **str**| &#39;Limit&#39; and &#39;Offset&#39; are optional; you can use these filter parameters to retrieve only part of the results obtained by a request.  Offset is the first element (from the complete list of elements) to be included in the response. | [optional]  |
| **limit** | **str**| &#39;Limit&#39; and &#39;Offset&#39; are optional; you can use these filter parameters to retrieve only part of the results of a query.  If both &#39;Offset&#39; and &#39;Limit&#39;are specified, the offset lines are skipped before counting the returned limit lines. | [optional]  |

### Return type

[**CertificateCollectionDto**](../models/CertificateCollectionDto.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **certificates_get_by_id**
> CertificateDto certificates_get_by_id(certificate_id)

Get a Certificate by ID

Retrieves a certificate specified by its ID.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_cert_manager
from ionoscloud_cert_manager.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com
configuration = ionoscloud_cert_manager.Configuration(
    host = 'https://api.ionos.com',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_cert_manager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_cert_manager.CertificatesApi(api_client)
    certificate_id = 'certificate_id_example' # str | 
    try:
        # Get a Certificate by ID
        api_response = api_instance.certificates_get_by_id(certificate_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling CertificatesApi.certificates_get_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **certificate_id** | **str**|  |  |

### Return type

[**CertificateDto**](../models/CertificateDto.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **certificates_patch**
> CertificateDto certificates_patch(certificate_id, certificate_patch_dto)

Update a Certificate Name by ID

Updates the name of the specified certificate.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_cert_manager
from ionoscloud_cert_manager.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com
configuration = ionoscloud_cert_manager.Configuration(
    host = 'https://api.ionos.com',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_cert_manager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_cert_manager.CertificatesApi(api_client)
    certificate_id = 'certificate_id_example' # str | 
    certificate_patch_dto = ionoscloud_cert_manager.CertificatePatchDto() # CertificatePatchDto | 
    try:
        # Update a Certificate Name by ID
        api_response = api_instance.certificates_patch(certificate_id, certificate_patch_dto)
        print(api_response)
    except ApiException as e:
        print('Exception when calling CertificatesApi.certificates_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **certificate_id** | **str**|  |  |
| **certificate_patch_dto** | [**CertificatePatchDto**](CertificatePatchDto.md)|  |  |

### Return type

[**CertificateDto**](../models/CertificateDto.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **certificates_post**
> CertificateDto certificates_post(certificate_post_dto)

Add a New Certificate

Adds a new PEM (Privacy Enhanced Mail) file that is used to store SSL certificates and their associated private keys.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_cert_manager
from ionoscloud_cert_manager.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com
configuration = ionoscloud_cert_manager.Configuration(
    host = 'https://api.ionos.com',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_cert_manager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_cert_manager.CertificatesApi(api_client)
    certificate_post_dto = ionoscloud_cert_manager.CertificatePostDto() # CertificatePostDto | 
    try:
        # Add a New Certificate
        api_response = api_instance.certificates_post(certificate_post_dto)
        print(api_response)
    except ApiException as e:
        print('Exception when calling CertificatesApi.certificates_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **certificate_post_dto** | [**CertificatePostDto**](CertificatePostDto.md)|  |  |

### Return type

[**CertificateDto**](../models/CertificateDto.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

