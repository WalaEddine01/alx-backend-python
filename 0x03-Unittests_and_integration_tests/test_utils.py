#!/usr/bin/env python3
"""
This module contains test cases for the access_nested_map function.
"""
from utils import access_nested_map, get_json
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
from unittest import TestCase
from unittest.mock import Mock, patch
from parameterized import parameterized
from fixtures import TEST_PAYLOAD


class TestAccessNestedMap(TestCase):
    """
    Test cases for access_nested_map function.
    """
    @parameterized.expand([(({"a": 1}, "a"), 1),
                           (({"a": {"b": 2}}, "a"), {"b": 2}),
                           (({"a": {"b": 2}}, ["a", "b"]), 2)])
    def test_access_nested_map(self, input: tuple, expe_output: Any) -> None:
        """
        Test access_nested_map function with various inputs.
        Parameters
        ----------
        input: tuple
            A tuple containing a nested map and a key or a sequence of keys.
        expe_output: Any
            The expected output for the given input.
        Example
        -------
        >>> nested_map = {"a": {"b": {"c": 1}}}
        >>> access_nested_map(nested_map, "a")
        {"b": {"c": 1}}
        >>> access_nested_map(nested_map, ["a", "b", "c"])
        1
        """
        self.assertEqual(access_nested_map(input[0], input[1]), expe_output)

    @parameterized.expand([(({}, "a")),
                           (({"a": 1}, ["a", "b"]))])
    def test_access_nested_map_exception(self,
                                         input: tuple,
                                         expe_output: Any) -> None:
        """
        Test access_nested_map function with inputs that should raise KeyError.
        """
        with self.assertRaises(KeyError):
            access_nested_map(input[0], input[0])

    @patch("requests.get")
    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})])
    def TestGetJson(self, test_url: str, test_payload: dict) -> None:
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch("requests.get", return_value=mock_response) as mock_get:
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
