num=int(input("Enter a number to print number of lines: "))

string=str(input("Enter a string that you want to print: "))

"""
for i in range(1, num+1):
    print(i*string, sep=" ")

"""





for i in range(num, 0, -1):
    print(i*string)


for i in range(1, num+1):
    print(i*string)




"""
for line in range(1,num+1):
    for col in range(1,line+1):
        print(string, end=" ")
    print()
"""
