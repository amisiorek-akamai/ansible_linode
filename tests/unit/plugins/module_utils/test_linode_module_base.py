from tests.unit.base import LinodeModuleBaseCase
from plugins.module_utils.linode_common import LinodeModuleBase
from unittest import TestCase
from typing import List, Dict, Any

class LinodeCommonTest(LinodeModuleBaseCase):

    def test_override_ca_path(self):
        self.assertEqual(self.module.client.base_url, "foobar")