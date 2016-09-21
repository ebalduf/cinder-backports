# Copyright (c) 2015 - 2016 Huawei Technologies Co., Ltd.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import webob

from cinder.api import versions
from cinder import test


class VersionsTest(test.TestCase):

    """Test the version information returned from the API service."""
    def override_config(self, name, override, group=None):
        """Cleanly override CONF variables."""
        test.CONF.set_override(name, override, group)
        self.addCleanup(test.CONF.clear_override, name, group)

    def test_get_version_list_public_endpoint(self):
        req = webob.Request.blank('/', base_url='http://127.0.0.1:8776/')
        req.accept = 'application/json'
        self.override_config('public_endpoint', 'https://example.com:8776')
        res = versions.Versions().index(req)
        results = res['versions']
        expected = [
            {
                'id': 'v1.0',
                'status': 'SUPPORTED',
                'updated': '2014-06-28T12:20:21Z',
                'links': [{'rel': 'self',
                           'href': 'https://example.com:8776/v1/'}],
            },
            {
                'id': 'v2.0',
                'status': 'CURRENT',
                'updated': '2012-11-21T11:33:21Z',
                'links': [{'rel': 'self',
                           'href': 'https://example.com:8776/v2/'}],
            },
        ]
        self.assertEqual(expected, results)

    def test_get_version_list(self):
        req = webob.Request.blank('/', base_url='http://127.0.0.1:8776/')
        req.accept = 'application/json'
        res = versions.Versions().index(req)
        results = res['versions']
        expected = [
            {
                'id': 'v1.0',
                'status': 'SUPPORTED',
                'updated': '2014-06-28T12:20:21Z',
                'links': [{'rel': 'self',
                           'href': 'http://127.0.0.1:8776/v1/'}],
            },
            {
                'id': 'v2.0',
                'status': 'CURRENT',
                'updated': '2012-11-21T11:33:21Z',
                'links': [{'rel': 'self',
                           'href': 'http://127.0.0.1:8776/v2/'}],
            },
        ]
        self.assertEqual(expected, results)