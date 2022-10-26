# 
# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

from ast import Try
from itertools import product

try:
    num_1 = int(input("Enter the first number "))
    num_2 = int(input("Enter the second number "))
except:
    print("kindly enter numbers and not anything else")
    exit()

product = num_2 * num_1
sum = num_2 + num_1


if product <= 1000:
    print(product)
else:
    print(sum)