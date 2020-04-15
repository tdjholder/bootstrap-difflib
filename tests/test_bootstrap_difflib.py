import unittest

from bootstrap_difflib.bootstrap_difflib import BootstrapHtmlDiff


class TestBootstrapDiffLib(unittest.TestCase):

    def setUp(self):
        self.differ = BootstrapHtmlDiff(bootstrap_source='/my_path')

    def test_make_table(self):
        self.assertIn('class="diff table"', self.differ.make_table(fromlines=['xyz'], tolines=['abc']))
