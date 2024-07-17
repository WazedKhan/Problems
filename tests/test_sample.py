# tests/test_your_script.py

import pytest


def add(num_1, num_2):
    return num_1 + num_2


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
