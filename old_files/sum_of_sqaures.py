def sum_of_squares(*numbers):
    """Returns the sum of squares of the given numbers"""

    sum = 0

    for number in numbers:
        sum += number ** 2

    return sum
