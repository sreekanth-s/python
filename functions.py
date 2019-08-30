print("Enter a number range to check basic math functions. \n \n")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

def add(*args):
    sum=0
    sum = sum + (*args)
    return sum

def sub(num1, num2):
    return num1-num2

def mul(num1, num2):
    return num1*num2

def div(num1, num2):
    if num2 == 0:
        print("Zero can never be divided. ")
        exit()
    else:
        return num1/num2


print("The addition of", num1, "and", num2, "is", add(num1, num2))

print("The Substraction of", num1, "and", num2, "is", sub(num1, num2))

print("The multiplication of", num1, "and", num2, "is", mul(num1, num2))

print("The division of", num1, "and", num2, "is", div(num1, num2))
