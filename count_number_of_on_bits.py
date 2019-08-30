
print("Enter a number to find the number of ON bits in a number.")

num=int(input("Enter a positive integer: "))

print_num = num
count=0

if num > 0:
    while num > 0:
        if num & 1:
            count+=1
        num = num >> 1
    print("The number entered", print_num, "has", count, "ON bits.")

else:
    print("Enter a positive number. ")
