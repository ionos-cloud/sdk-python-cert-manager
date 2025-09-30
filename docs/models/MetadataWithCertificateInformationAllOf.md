# MetadataWithCertificateInformationAllOf

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **auto_certificate** | **str** | The ID of the auto-certificate that caused issuing of the certificate. | [optional]  |
| **last_issued_certificate** | **str** | The ID of the last issued certificate that belongs to the same auto-certificate. | [optional]  |
| **expired** | **bool** | Indicates if the certificate is expired. |  |
| **not_before** | **datetime** | The start date of the certificate. |  |
| **not_after** | **datetime** | The end date of the certificate. |  |
| **serial_number** | **str** | The serial number of the certificate in hex. |  |
| **common_name** | **str** | The common name (DNS) of the certificate. |  |
| **subject_alternative_names** | **list[str]** | Optional additional names added to the issued certificate. The additional names needs to be part of a zone in IONOS Cloud DNS.  |  |


