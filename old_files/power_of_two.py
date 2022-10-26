#!/usr/bin/python3.6

num=int(input("Enter a number to find if it is a power of 2 : "))

def power_of_2(num):
    if num <= 0:
        print("Enter a valid natural number")
        exit()

    while num%2 == 0:
        num=num//2

    return num


print("Power of 2" if power_of_2(num)==1 else "Not a power of 2")
