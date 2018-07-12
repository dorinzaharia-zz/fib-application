"""
Fibonacci sequence
"""

def calculate_fibonacci():
    """
    Generator for Fibonacci sequence up to number_if_terms
    """

    first_number = 0
    second_number = 1
    count = 0

    while True:
        yield first_number
        # calculate next number
        temporar_number = first_number
        first_number = second_number
        second_number = temporar_number + first_number
        count += 1
