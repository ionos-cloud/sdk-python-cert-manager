# MetadataWithCertificateInformation

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **created_date** | **datetime** | The ISO 8601 creation timestamp. | [optional] [readonly]  |
| **created_by** | **str** | Unique name of the identity that created the resource. | [optional] [readonly]  |
| **created_by_user_id** | **str** | Unique id of the identity that created the resource. | [optional] [readonly]  |
| **last_modified_date** | **datetime** | The ISO 8601 modified timestamp. | [optional] [readonly]  |
| **last_modified_by** | **str** | Unique name of the identity that last modified the resource. | [optional] [readonly]  |
| **last_modified_by_user_id** | **str** | Unique id of the identity that last modified the resource. | [optional] [readonly]  |
| **resource_urn** | **str** | Unique name of the resource. | [optional] [readonly]  |
| **state** | **str** | The resource state. |  |
| **message** | **str** | A human readable message describing the current state. In case of an error, the message will contain a detailed error message.  |  |
| **auto_certificate** | **str** | The ID of the auto-certificate that caused issuing of the certificate. | [optional]  |
| **last_issued_certificate** | **str** | The ID of the last issued certificate that belongs to the same auto-certificate. | [optional]  |
| **expired** | **bool** | Indicates if the certificate is expired. |  |
| **not_before** | **datetime** | The start date of the certificate. |  |
| **not_after** | **datetime** | The end date of the certificate. |  |
| **serial_number** | **str** | The serial number of the certificate in hex. |  |
| **common_name** | **str** | The common name (DNS) of the certificate. |  |
| **subject_alternative_names** | **list[str]** | Optional additional names added to the issued certificate. The additional names needs to be part of a zone in IONOS Cloud DNS.  |  |


