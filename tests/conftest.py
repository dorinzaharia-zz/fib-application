"""
Pytest
"""

import pytest

@pytest.fixture
def fibonacci_list():
    """
    Returning a list
    """

    return [0, 1, 1, 2, 3, 5, 8]
