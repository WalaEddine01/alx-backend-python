#!/usr/bin/env python3
"""
This module contains test cases
"""
import unittest
from unittest.mock import PropertyMock, patch
from typing import (
    Any,
)
from parameterized import parameterized_class
from fixtures import TEST_PAYLOAD

from client import GithubOrgClient
from parameterized import parameterized
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases.
    """
    @parameterized.expand([("google", {'TEST_PAYLOAD': True}),
                           ("abc", {'TEST_PAYLOAD': False})])
    @patch("client.get_json")
    def test_org(self, input: tuple, test_payload: Any, mock_get: Any) -> None:
        """
        Test GithubOrgClient.org method.
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
    def test_public_repos_url(self, org_name: tuple, repos_url: str) -> None:
        """
        Test GithubOrgClient._public_repos_url property.
        """
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_prop:
            mock_prop.return_value = {"repos_url": repos_url}
            githuborgclient = GithubOrgClient(org_name)
            result = githuborgclient._public_repos_url
            self.assertEqual(result, repos_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        Test GithubOrgClient.public_repos method.
        """
        payload = [{"name": "repo1"}, {"name": "repo2"}]
        url = "https://api.github.com/orgs/testorg/repos"
        mock_get_json.return_value = payload

        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock) as mock_repos:
            mock_repos.return_value = url
            githuborgclient = GithubOrgClient("testorg")
            repos = githuborgclient.public_repos()
            self.assertEqual(repos, ["repo1", "repo2"])
            mock_repos.assert_called_once()
            mock_get_json.assert_called_once_with(url)

    @parameterized.expand([({"license": {"key": "my_license"}},
                            "my_license", True), (
                                {"license": {"key": "other_license"}},
                                "my_license", False)])
    def test_has_license(self, license_obj, license_key, expected_output):
        """
        """
        self.assertEqual(GithubOrgClient.has_license(license_obj, license_key),
                         expected_output)
