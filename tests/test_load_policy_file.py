import unittest

import os
import sys
# Add the parent directory to sys.path so that the `main` module can be found
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main.is_policy_resource_asterisk_free import load_policy_file

class TestLoadPolicyFile(unittest.TestCase):
    
    def test_load_valid_policy_file(self):
        """Test reading a valid policy file."""
        policy = load_policy_file("fixtures/valid_policy.json")
        self.assertIn("Statement", policy["PolicyDocument"])


    def test_file_not_found_error(self):
        """Test the function raises FileNotFoundError for non-existent files."""
        with self.assertRaises(FileNotFoundError):
            load_policy_file("non_existent_file.json")

    def test_invalid_json_error(self):
        """Test the function raises ValueError for files with invalid JSON."""
        with self.assertRaises(ValueError):
            load_policy_file("fixtures/invalid_json_policy.json")

    def test_invalid_policy_format_error(self):
        """Test the function raises ValueError for valid JSON that doesn't match the policy format."""
        with self.assertRaises(ValueError):
            load_policy_file("fixtures/invalid_format_policy.json")

    def test_no_statement_key_error(self):
        """Test the function raises ValueError for JSON objects without 'Statement'."""
        with self.assertRaises(ValueError):
            load_policy_file("fixtures/no_statement_key.json")