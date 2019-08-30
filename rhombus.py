num=int(input("Enter a number to print number of lines: "))
star=" *"
space=" "


counter = num


"""
for i in range(0, num):
    print((num-i)*star, i*space, sep="", end="")        # Top Left
    print(i*space, (num-i)*star, sep="")                # Top Right
"""
for i in range(0, num):
    print(star*(i+1), (num-(i+1))*space, sep="", end="")
    print( ( num-(i+1) )*space, (i+1)*star, sep="")


"""

## bottom left
for i in range(1, num+1):
    print(star*i, (num-i)*space, sep="", end="")    # Bottom Left
    print((num-i)*space, i*star, sep="")            # Bottom Right


print()
print()


for i in range(0, num):
    print(star*(i+1), (num-(i+1))*space, sep="", end="")
    print( ( num-(i+1) )*space, (i+1)*star, sep="")






print()


## top right
for i in range(0, num):
    print(i*space, (num-i)*star, sep="")

print()

## bottom right
for i in range(1, num+1):
    print((num-i)*space, i*star, sep="")
"""
