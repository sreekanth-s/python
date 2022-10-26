num=int(input("Enter a number to print number of lines: "))



#string=str(input("Enter a string that you want to print: "))

star="#"
space="="


"""for i in range(0, num):
    print( (num-(i+1)) * space, ((i+1)+(i)) * star, sep="")

print()
"""
for i in range(0, num):
    print(i*space, (num+(num-1)) * star, i*space, sep="")
    num=num-1










"""
    for i in range( (num+(num-1)), 0, -2):
        print(i*"*")

    for j in range(0, num):
        print(j*"-")


    for i in range( (num+(num-1)), 0, -2):
        print(i*"*")

    for j in range(0, num):
        print(j*"-")
"""


##  print triangle with two for loops

"""
for i in range(1, num+1):
    for j in range(i,num):
        print("-", end="")
    print("*"*(i*2-1), end="")
    for j in range(i,num):
        print("-", end="")
    print()

"""


# print triangle in reverse with two for loops.
"""

for i in range(num, 0, -1):
    for j in range(i, num):
        print("-", end="")
    print("*"* ( (i*2) - 1 ), end="" )
    for j in range(i, num):
        print("-", end="")
    print()

"""
"""
    for j in range(i,num):
        print("-", end="")
    print("&"*(i*2-1))


"""
