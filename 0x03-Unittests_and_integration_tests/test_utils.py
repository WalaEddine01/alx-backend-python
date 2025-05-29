#!/usr/bin/python3
"""
"""
from utils import access_nested_map
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
from unittest import TestCase
from parameterized import parameterized


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

    

