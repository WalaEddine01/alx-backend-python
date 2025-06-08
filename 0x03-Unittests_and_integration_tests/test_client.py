#!/usr/bin/env python3
"""
This module contains test cases
"""
import unittest
from unittest.mock import Mock, PropertyMock
from utils import access_nested_map, get_json, memoize
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
from unittest import TestCase
from unittest.mock import patch, MagicMock
from parameterized import parameterized_class
from fixtures import TEST_PAYLOAD
import json
import requests

from client import GithubOrgClient
from unittest.mock import Mock, patch
from parameterized import parameterized
from fixtures import TEST_PAYLOAD
import requests


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases.
    """
    @parameterized.expand([("google", {'TEST_PAYLOAD': True}),
                           ("abc", {'TEST_PAYLOAD': False})])
    @patch("client.get_json")
    def test_org(self, input: tuple, test_payload: Any, mock_get: Any) -> None:
        """
        """
        githuborgclient = GithubOrgClient(input)
        mock_get.return_value = test_payload

        result = githuborgclient.org
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(
            f"https://api.github.com/orgs/{input}")

    @parameterized.expand([("google",
                            "https://api.github.com/orgs/google/repos"),
                           ("abc", "https://api.github.com/orgs/abc/repos")])
    def test_public_repos_url(self, org_name: tuple, repos_url: Any) -> None:
        """
        """
        with patch.object(GithubOrgClient, 'GithubOrgClient.org ',
                          new_callable=PropertyMock) as mock_prop:
            mock_prop.return_value = repos_url
            githuborgclient = GithubOrgClient(input)
            result = githuborgclient._public_repos_url
            self.assertEqual(result, repos_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        Test GithubOrgClient.public_repos method.
        """
        fake_repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = fake_repos_payload

        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "https://fake.url/repos"

            client = GithubOrgClient("some_org")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://fake.url/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that has_license returns correct boolean result
        depending on the license key.
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)

@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD["org_payload"],
        "repos_payload": TEST_PAYLOAD["repos_payload"],
        "expected_repos": TEST_PAYLOAD["expected_repos"],
        "apache2_repos": TEST_PAYLOAD["apache2_repos"],
    }
])
@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD["org_payload"],
        "repos_payload": TEST_PAYLOAD["repos_payload"],
        "expected_repos": TEST_PAYLOAD["expected_repos"],
        "apache2_repos": TEST_PAYLOAD["apache2_repos"],
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient using real logic but mocked HTTP."""

    @classmethod
    def setUpClass(cls):
        """Patch requests.get to return fixture payloads."""
        cls.get_patcher = patch("requests.get")
        mock_get = cls.get_patcher.start()

        def side_effect(url, *args, **kwargs):
            if url == cls.org_payload["url"]:  # likely something like .../orgs/google
                return MagicMock(json=lambda: cls.org_payload)
            elif url == cls.repos_payload[0]["url"]:
                # repos_payload is list of dicts with a "url" key maybe
                return MagicMock(json=lambda: cls.repos_payload)
            else:
                return MagicMock(json=lambda: [])

        mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patching requests.get."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Integration test: public_repos should return expected_repos."""
        client = GithubOrgClient(self.org_payload["login"])
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Integration test: public_repos with license="apache-2.0"
        should return only repos with that license.
        """
        client = GithubOrgClient(self.org_payload["login"])
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )