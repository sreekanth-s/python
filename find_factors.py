print("Enter a number range to find the factors between them. \n \n")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))


# check if the numbers are in right range and only then proceed.

if num1 >= num2:
    print("Enter a range please. ")

else:

    for i in range(num1, num2+1):
        # iterating for each number with 2, because 1 is a factor of all numbers.
        for j in range(2, i):
            #enter the if condition only if the % is true and print it.
            if i%j == 0:
                print(i, "=", j, "x", i/j)
                # break because you do not want to find all the factors,
                # but just to find if the number has any other factors
                break
        else:
            print(i, "is a prime number")

        # part where the logic exits, the number becomes prime
