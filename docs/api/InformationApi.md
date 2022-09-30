# InformationApi

All URIs are relative to *https://api.ionos.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**get_info**](InformationApi.md#get_info) | **GET** /certificatemanager | Get the Service API Information |
| [**get_json_open_api_spec**](InformationApi.md#get_json_open_api_spec) | **GET** /certificatemanager/openapi.json | Get the Open API Documentation JSON |
| [**get_yaml_open_api_spec**](InformationApi.md#get_yaml_open_api_spec) | **GET** /certificatemanager/openapi.yaml | Get the Open API Documentation YAML |


# **get_info**
> ApiInfoDto get_info()

Get the Service API Information

Retrieves the service API information.

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
    api_instance = ionoscloud_cert_manager.InformationApi(api_client)
    try:
        # Get the Service API Information
        api_response = api_instance.get_info()
        print(api_response)
    except ApiException as e:
        print('Exception when calling InformationApi.get_info: %s\n' % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiInfoDto**](../models/ApiInfoDto.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **get_json_open_api_spec**
> file get_json_open_api_spec()

Get the Open API Documentation JSON

Displays the Open API documentation in the JSON format.

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
    api_instance = ionoscloud_cert_manager.InformationApi(api_client)
    try:
        # Get the Open API Documentation JSON
        api_response = api_instance.get_json_open_api_spec()
        print(api_response)
    except ApiException as e:
        print('Exception when calling InformationApi.get_json_open_api_spec: %s\n' % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**file**

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **get_yaml_open_api_spec**
> file get_yaml_open_api_spec()

Get the Open API Documentation YAML

Displays the Open API documentation in the YAML format.

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
    api_instance = ionoscloud_cert_manager.InformationApi(api_client)
    try:
        # Get the Open API Documentation YAML
        api_response = api_instance.get_yaml_open_api_spec()
        print(api_response)
    except ApiException as e:
        print('Exception when calling InformationApi.get_yaml_open_api_spec: %s\n' % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**file**

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yaml

