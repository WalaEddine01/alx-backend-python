#!/usr/bin/env python3
"""
This module contains test cases for the access_nested_map function.
"""
from utils import access_nested_map, get_json, memoize
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
import requests


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


class TestGetJson(TestCase):
    """
    Test cases for get_json function.
    This function retrieves JSON data from a given URL.
    """
    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})])
    @patch('requests.get')
    def test_get_json(self, test_url: str,
                      test_payload: dict, mock_get: Any) -> None:
        """
        Test get_json function with various URLs and payloads.
        Parameters
        ----------
        test_url: str
            The URL to fetch JSON data from.
        test_payload: dict
            The expected JSON payload to be returned.
        mock_get: Mock
            Mock object to simulate requests.get behavior.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_with(test_url)


class TestMemoize(TestCase):
    """
    Test cases for memoize decorator.
    This decorator caches the result of a method
    to avoid redundant calculations.
    """
    def test_memoize(self) -> None:
        """
        Test memoize decorator with a simple class method.
        This test checks if the method is called only once
        and the result is cached.
        """
        class TestClass:
            """
            A simple class to test the memoize decorator.
            """
            def a_method(self):
                """
                A method that returns a constant value.
                """
                return 42

            @memoize
            def a_property(self):
                """
                A property that uses the memoize decorator.
                """
                return self.a_method()

        testClassInstance = TestClass()
        with patch.object(testClassInstance, "a_method",
                          return_value=200) as mock_method:
            result = testClassInstance.a_property

            self.assertEqual(result, 200)
            mock_method.assert_called_once()
