import unittest

import os
import sys
# Add the parent directory to sys.path so that the `main` module can be found
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main.is_policy_resource_asterisk_free import load_policy_file

class TestLoadPolicyFile(unittest.TestCase):
    

    def test_missing_policy_name_key_error(self):
        with self.assertRaises(ValueError):
            load_policy_file("fixtures/missing_policy_name.json")

    def test_policy_name_not_string_error(self):
        with self.assertRaises(ValueError):
            load_policy_file("fixtures/policy_name_not_string.json")

    def test_load_valid_policy_file(self):
        policy = load_policy_file("fixtures/valid_policy.json")
        self.assertIn("Statement", policy["PolicyDocument"])


    def test_file_not_found_error(self):
        with self.assertRaises(FileNotFoundError):
            load_policy_file("non_existent_file.json")

    def test_invalid_json_error(self):
        with self.assertRaises(ValueError):
            load_policy_file("fixtures/invalid_json_policy.json")

    def test_invalid_policy_format_error(self):
        with self.assertRaises(ValueError):
            load_policy_file("fixtures/invalid_format_policy.json")

    def test_missing_policy_document_key_error(self):
        with self.assertRaises(ValueError):
            load_policy_file("fixtures/missing_policy_document.json")

    def test_no_statement_key_error(self):
        with self.assertRaises(ValueError):
            load_policy_file("fixtures/no_statement_key.json")

    
  