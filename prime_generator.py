"""
A function that takes one argument and returns a list of prime numbers from 
0 to that argument.
"""


def prime_number_generator(n):
    # Check if argument is an integer
    if isinstance(n, int):
        # Check if argument is positive integer
        if n > 0:
            number_set = set(range(n, 1, -1))
            prime_numbers = []
            # iterate while number set isn't empty
            while number_set:
                num = number_set.pop()
                prime_numbers.append(num)
                number_set.difference_update(set(range(num * 2, n + 1, num)))
            return prime_numbers
        else:
            # return empty list if the argument is a negative integer
            return []
    else:
        # raise a type error if argument is not an integer
        raise TypeError("Argument must be an integer")
