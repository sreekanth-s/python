"""
num=int(input("Enter a number to find factorial: "))

if (num <= 0):
    print("Enter a valid integer! ")
else:
    print("You've entered ", num)
    for i in range(1,num):
        num=num*i

print("and the factorial is ",num)

"""

num=int(input("Enter a number to find factorial: "))
print("You've entered ", num)

fact=1

if (num <= 0):
    print("Enter a valid integer! ")
else:
    while num > 1:
        fact=fact*(num)
        num=num-1
    print("and the factorial is ", fact)



def factorial(num):
    fact=1
    fact=fact*num
    num=num-1
    factorial(num-1)






"""

def factorial(num):
    if num==1:
        print(result)
        exit()
        result=num*(num-1)
        factorial(num)

#

factorial(5)
"""
