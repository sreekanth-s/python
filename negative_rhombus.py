num=int(input("Enter a number to print number of lines: "))
star="*"
space="-"


for i in range(1, num+1):
    for n in range(num+1, i, -1):
        print(star, end=" ")
    for o in range(1, i):
        print(space, end=" ")
    for p in range(1, i):
        print(space, end=" ")
    for q in range(num+1, i, -1):
        print(star, end=" ")
    print()

for i in range(1, num+1):
    for j in range(1, i+1):
        print(star, end=" ")
    for k in range(num, i, -1):
        print(space, end=" ")
    for l in range(num, i, -1):
        print(space, end=" ")
    for m in range(1, i+1):
        print(star, end=" ")
    print()

print()
print()

for i in range(1, num+1):
    for l in range(num, i, -1):
        print(space, end="")
    for m in range(1, i+1):
        print(star, end="")
    print()

print()
print()



print()
print()


for i in range(1, num+1):
    for p in range(1, i):
        print(space, end="")
    for q in range(num+1, i, -1):
        print(star, end="")
    print()
