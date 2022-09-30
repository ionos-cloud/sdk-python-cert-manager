[![Gitter](https://img.shields.io/gitter/room/ionos-cloud/sdk-general)](https://gitter.im/ionos-cloud/sdk-general)
[![PyPI version](https://img.shields.io/pypi/v/ionoscloud-cert-manager)](https://pypi.org/project/ionoscloud-cert-manager/)

# ionoscloud
Using the Certificate Manager Service, you can conveniently provision and manage SSL certificates with IONOS services and your internal connected resources. For the [Application Load Balancer](https://api.ionos.com/docs/cloud/v6/#Application-Load-Balancers-get-datacenters-datacenterId-applicationloadbalancers), you usually need a certificate to encrypt your HTTPS traffic. The service provides the basic functions of uploading and deleting your certificates for this purpose.

## Requirements.

- Python >= 3.5

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/ionos-cloud/sdk-python-cert-manager.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ionos-cloud/sdk-python-cert-manager.git`)

Then import the package:
```python
import ionoscloud_cert_manager
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ionoscloud_cert_manager
```
## Our latest, most up to date documentation is available [here](https://github.com/ionos-cloud/ionos-cloud-sdk-python-cert-manager/blob/master/README.md)
