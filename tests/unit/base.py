from plugins.module_utils.linode_common import LinodeModuleBase
from unittest import TestCase
from typing import List


class LinodeModuleBaseCase(TestCase):
    def setUp(self) -> None:
        self.module = LinodeModuleBase(module_arg_spec={'api_token': 'testing', 'api_url': '/', 'ca_path': 'foobar'})