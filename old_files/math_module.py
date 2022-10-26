'''
num=int(input("Enter an integer to find if it is a power of 2: "))

if (num%2 == 0):
    for i in range(0,num//2):
            if ((2**(num//2)) == num):
                    print(num, "is a power of two")
else:
    print(num, "is not a power of 2")


'''

'''
def is_power_of_two(n):
    """Return True if n is a power of two."""
    if n <= 0:
        return False
    else:
        print(n, n-1)
        return n & (n - 1) == 0

n = int(input('Enter a number: '))

if is_power_of_two(n):
    print('{} is a power of two.'.format(n))
else:
    print('{} is not a power of two.'.format(n))


'''

'''
num1=None
num2=None

while (num1 is None and num2 is None) or ( (num1 < 0) or (num2 < 0) ) :
    num1=int(input("Enter a number: "))
    num2=int(input("Enter a number: "))
    print("Enter natural numbers ")
    #exit()

if num1 < num2 :
    print(num2 - num1)
else:
    print(num1 - num2)

'''

'''
print("Enter three numbers when prompted to find the largest of them. ")

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))


# print(max(num1, num2, num3), "is the largest of three numbers. ")

# print(min(num1, num2, num3), "is the largest of three numbers. ")




if((num1 > num2) and (num1 > num3)):
    print(num1, "is the largest of the three numbers. ")
elif ((num2 > num1) and (num2 > num3)):
    print(num2, "is the largest of the three numbers. ")
else:
    print(num3, "is the largest of the three numbers. ")


if((num1 < num2) and (num1 < num3)):
    print(num1, "is the smallest of the three numbers. ")
elif ((num2 < num1) and (num2 < num3)):
    print(num2, "is the smallest of the three numbers. ")
else:
    print(num3, "is the smallest of the three numbers. ")

'''

print("Enter three numbers when prompted to find the largest of them. ")

num=[]

num.append(int(input("Enter first number: ")))
num.append(int(input("Enter second number: ")))
num.append(int(input("Enter third number: ")))

num=sorted(num)

print(num[0], "is the smallest of the three numbers and ", num[2], "is the largest of the three numbers. ")
