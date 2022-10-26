#!/usr/bin/python3.6

number=int(input("Enter a number to find the number of ON bits in it : "))

binary_value=bin(number)

count=0


for i in range(len(bin(number))-2):
    #print(range(len(bin(number))))
    print(i)
    #print(binary_value[i+2])
    if binary_value[i+2] == "1":
        count=count+1
        #print(count)

print("The binary equivalent of ", number, "is ", binary_value, "\n and the number of ON bits in it are ", count)
