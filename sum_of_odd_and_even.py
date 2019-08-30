
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of the range: "))

def sum_of_odd_and_even(start, end):
    """ Returns the sum of all even numbers and odd numbers in range start and end """

    even_sum = 0
    odd_sum = 0

    for number in range(start, end+1):
        if number %2 == 0:
            even_sum += number
        else:
            odd_sum += number

    return odd_sum, even_sum

print(sum_of_odd_and_even(start, end))
