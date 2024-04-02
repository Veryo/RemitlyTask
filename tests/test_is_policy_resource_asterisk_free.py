import unittest

import os
import sys
# Add the parent directory to sys.path so that the `main` module can be found
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main.is_policy_resource_asterisk_free import is_policy_resource_asterisk_free 

class TestIsPolicyResourceAsteriskFree(unittest.TestCase):

    def test_policy_with_wildcard(self):
        policy = is_policy_resource_asterisk_free("fixtures/policy_with_asterisk.json")
        self.assertFalse(policy)

    def test_policy_without_wildcard(self):
        policy = is_policy_resource_asterisk_free("fixtures/policy_without_asterisk.json")
        self.assertTrue(policy)

    def test_policy_mixed_resources(self):
        policy = is_policy_resource_asterisk_free("fixtures/policy_mixed_resources.json")
        self.assertFalse(policy)