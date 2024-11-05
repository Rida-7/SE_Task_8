import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from add import add

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(1.4, 2) == 3.4


def test_add_valid():
    assert add(2, 3) == 5

def test_add_invalid_string():
    with pytest.raises(TypeError, match="Both arguments must be int or float."):
        add(2, "three")

def test_add_invalid_list():
    with pytest.raises(TypeError, match="Both arguments must be int or float."):
        add([1, 2], 3)

def test_add_invalid_none():
    with pytest.raises(TypeError, match="Both arguments must be int or float."):
        add(None, 3)
