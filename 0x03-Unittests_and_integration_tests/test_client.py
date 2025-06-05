#!/usr/bin/env python3
"""
This module contains test cases
"""
import unittest
from utils import access_nested_map, get_json, memoize
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)

from client import GithubOrgClient
from unittest.mock import Mock, patch
from parameterized import parameterized
from fixtures import TEST_PAYLOAD
import requests


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases.
    """
    @parameterized.expand([("google", {'TEST_PAYLOAD': True,}),
                           ("abc", {'TEST_PAYLOAD': False,})])
    @patch("client.get_json")
    def test_org(self, input: tuple, test_payload: Any, mock_get: Any) -> None:
        """
        """
        githuborgclient = GithubOrgClient(input)
        mock_get.return_value = test_payload

        result = githuborgclient.org
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(f"https://api.github.com/orgs/{input}")
