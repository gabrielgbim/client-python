# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_resource_quota_list import V1ResourceQuotaList


class TestV1ResourceQuotaList(unittest.TestCase):
    """ V1ResourceQuotaList unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1ResourceQuotaList(self):
        """
        Test V1ResourceQuotaList
        """
        model = kubernetes.client.models.v1_resource_quota_list.V1ResourceQuotaList()


if __name__ == '__main__':
    unittest.main()
