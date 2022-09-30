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


class ResourceMetadataDto(object):
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

        'etag': 'str',

        'created_date': 'str',

        'created_by': 'str',

        'created_by_user_id': 'str',

        'last_modified_date': 'str',

        'last_modified_by': 'str',

        'last_modified_by_user_id': 'str',

        'state': 'str',
    }

    attribute_map = {

        'etag': 'etag',

        'created_date': 'createdDate',

        'created_by': 'createdBy',

        'created_by_user_id': 'createdByUserId',

        'last_modified_date': 'lastModifiedDate',

        'last_modified_by': 'lastModifiedBy',

        'last_modified_by_user_id': 'lastModifiedByUserId',

        'state': 'state',
    }

    def __init__(self, etag=None, created_date=None, created_by=None, created_by_user_id=None, last_modified_date=None, last_modified_by=None, last_modified_by_user_id=None, state=None, local_vars_configuration=None):  # noqa: E501
        """ResourceMetadataDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._etag = None
        self._created_date = None
        self._created_by = None
        self._created_by_user_id = None
        self._last_modified_date = None
        self._last_modified_by = None
        self._last_modified_by_user_id = None
        self._state = None
        self.discriminator = None

        if etag is not None:
            self.etag = etag
        if created_date is not None:
            self.created_date = created_date
        if created_by is not None:
            self.created_by = created_by
        if created_by_user_id is not None:
            self.created_by_user_id = created_by_user_id
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if last_modified_by_user_id is not None:
            self.last_modified_by_user_id = last_modified_by_user_id
        if state is not None:
            self.state = state


    @property
    def etag(self):
        """Gets the etag of this ResourceMetadataDto.  # noqa: E501

        The entity tag of the resource, as defined in http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.11. The entity tag is also added as an 'ETag' response header to requests that do not use the 'depth' parameter.  # noqa: E501

        :return: The etag of this ResourceMetadataDto.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this ResourceMetadataDto.

        The entity tag of the resource, as defined in http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.11. The entity tag is also added as an 'ETag' response header to requests that do not use the 'depth' parameter.  # noqa: E501

        :param etag: The etag of this ResourceMetadataDto.  # noqa: E501
        :type etag: str
        """

        self._etag = etag

    @property
    def created_date(self):
        """Gets the created_date of this ResourceMetadataDto.  # noqa: E501

        The date the resource was created.  # noqa: E501

        :return: The created_date of this ResourceMetadataDto.  # noqa: E501
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this ResourceMetadataDto.

        The date the resource was created.  # noqa: E501

        :param created_date: The created_date of this ResourceMetadataDto.  # noqa: E501
        :type created_date: str
        """

        self._created_date = created_date

    @property
    def created_by(self):
        """Gets the created_by of this ResourceMetadataDto.  # noqa: E501

        The user who created the resource.  # noqa: E501

        :return: The created_by of this ResourceMetadataDto.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ResourceMetadataDto.

        The user who created the resource.  # noqa: E501

        :param created_by: The created_by of this ResourceMetadataDto.  # noqa: E501
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def created_by_user_id(self):
        """Gets the created_by_user_id of this ResourceMetadataDto.  # noqa: E501

        The ID of the user who created the resource.  # noqa: E501

        :return: The created_by_user_id of this ResourceMetadataDto.  # noqa: E501
        :rtype: str
        """
        return self._created_by_user_id

    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id):
        """Sets the created_by_user_id of this ResourceMetadataDto.

        The ID of the user who created the resource.  # noqa: E501

        :param created_by_user_id: The created_by_user_id of this ResourceMetadataDto.  # noqa: E501
        :type created_by_user_id: str
        """

        self._created_by_user_id = created_by_user_id

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this ResourceMetadataDto.  # noqa: E501

        The date when the resource was last modified.  # noqa: E501

        :return: The last_modified_date of this ResourceMetadataDto.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this ResourceMetadataDto.

        The date when the resource was last modified.  # noqa: E501

        :param last_modified_date: The last_modified_date of this ResourceMetadataDto.  # noqa: E501
        :type last_modified_date: str
        """

        self._last_modified_date = last_modified_date

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this ResourceMetadataDto.  # noqa: E501

        The user who last modified the resource.  # noqa: E501

        :return: The last_modified_by of this ResourceMetadataDto.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this ResourceMetadataDto.

        The user who last modified the resource.  # noqa: E501

        :param last_modified_by: The last_modified_by of this ResourceMetadataDto.  # noqa: E501
        :type last_modified_by: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_by_user_id(self):
        """Gets the last_modified_by_user_id of this ResourceMetadataDto.  # noqa: E501

        The ID of the user who last modified the resource.  # noqa: E501

        :return: The last_modified_by_user_id of this ResourceMetadataDto.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by_user_id

    @last_modified_by_user_id.setter
    def last_modified_by_user_id(self, last_modified_by_user_id):
        """Sets the last_modified_by_user_id of this ResourceMetadataDto.

        The ID of the user who last modified the resource.  # noqa: E501

        :param last_modified_by_user_id: The last_modified_by_user_id of this ResourceMetadataDto.  # noqa: E501
        :type last_modified_by_user_id: str
        """

        self._last_modified_by_user_id = last_modified_by_user_id

    @property
    def state(self):
        """Gets the state of this ResourceMetadataDto.  # noqa: E501

        The resource state.  # noqa: E501

        :return: The state of this ResourceMetadataDto.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ResourceMetadataDto.

        The resource state.  # noqa: E501

        :param state: The state of this ResourceMetadataDto.  # noqa: E501
        :type state: str
        """

        self._state = state
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
        if not isinstance(other, ResourceMetadataDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResourceMetadataDto):
            return True

        return self.to_dict() != other.to_dict()