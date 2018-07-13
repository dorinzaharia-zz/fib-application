"""
Test
"""

from fibonacci.fibonacci import calculate_fibonacci

def test_calculate_fibonacci(fibonacci_list):
    """
    Calculate 7 number of fib sequence and assert with 8
    """

    result = calculate_fibonacci()

    is_equal = True

    for i in range(6):
        if fibonacci_list[i] != next(result):
            is_equal = False

    assert(is_equal)
