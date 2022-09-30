# coding: utf-8

"""
    Certificate Manager Service API

    Using the Certificate Manager Service, you can conveniently provision and manage SSL certificates with IONOS services and your internal connected resources. For the [Application Load Balancer](https://api.ionos.com/docs/cloud/v6/#Application-Load-Balancers-get-datacenters-datacenterId-applicationloadbalancers), you usually need a certificate to encrypt your HTTPS traffic.  The service provides the basic functions of uploading and deleting your certificates for this purpose.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud_cert_manager.configuration import Configuration


class CertificatePropertiesDto(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {

        'name': 'str',

        'certificate': 'str',

        'certificate_chain': 'str',
    }

    attribute_map = {

        'name': 'name',

        'certificate': 'certificate',

        'certificate_chain': 'certificateChain',
    }

    def __init__(self, name=None, certificate=None, certificate_chain=None, local_vars_configuration=None):  # noqa: E501
        """CertificatePropertiesDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._certificate = None
        self._certificate_chain = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if certificate is not None:
            self.certificate = certificate
        if certificate_chain is not None:
            self.certificate_chain = certificate_chain


    @property
    def name(self):
        """Gets the name of this CertificatePropertiesDto.  # noqa: E501

        The certificate name.  # noqa: E501

        :return: The name of this CertificatePropertiesDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CertificatePropertiesDto.

        The certificate name.  # noqa: E501

        :param name: The name of this CertificatePropertiesDto.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def certificate(self):
        """Gets the certificate of this CertificatePropertiesDto.  # noqa: E501

        The certificate body.  # noqa: E501

        :return: The certificate of this CertificatePropertiesDto.  # noqa: E501
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this CertificatePropertiesDto.

        The certificate body.  # noqa: E501

        :param certificate: The certificate of this CertificatePropertiesDto.  # noqa: E501
        :type certificate: str
        """

        self._certificate = certificate

    @property
    def certificate_chain(self):
        """Gets the certificate_chain of this CertificatePropertiesDto.  # noqa: E501

        Optional. The certificate chain.  # noqa: E501

        :return: The certificate_chain of this CertificatePropertiesDto.  # noqa: E501
        :rtype: str
        """
        return self._certificate_chain

    @certificate_chain.setter
    def certificate_chain(self, certificate_chain):
        """Sets the certificate_chain of this CertificatePropertiesDto.

        Optional. The certificate chain.  # noqa: E501

        :param certificate_chain: The certificate_chain of this CertificatePropertiesDto.  # noqa: E501
        :type certificate_chain: str
        """

        self._certificate_chain = certificate_chain
    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CertificatePropertiesDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CertificatePropertiesDto):
            return True

        return self.to_dict() != other.to_dict()
