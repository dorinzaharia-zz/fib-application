"""
Fibonacci sequence
"""

from fibonacci.fibonacci import calculate_fibonacci

def main():
    """
    Main method to display fibonacci sequence up to given number
    """

    number_of_terms = 8

    fibonacci_number = calculate_fibonacci()

    for i in range(number_of_terms):
        print(next(fibonacci_number))


if __name__ == "__main__":
    main()
