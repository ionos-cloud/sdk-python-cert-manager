# AutoCertificate

Auto certificates create new certificates based on a certificate provider. 
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **provider** | **str** | The certificate provider used to issue the certificates. |  |
| **common_name** | **str** | The common name (DNS) of the certificate to issue. The common name needs to be part of a zone in IONOS Cloud DNS.  |  |
| **key_algorithm** | **str** | The key algorithm used to generate the certificate. |  |
| **name** | **str** | A certificate name used for management purposes. |  |
| **subject_alternative_names** | **list[str]** | Optional additional names to be added to the issued certificate. The additional names needs to be part of a zone in IONOS Cloud DNS.  | [optional]  |


