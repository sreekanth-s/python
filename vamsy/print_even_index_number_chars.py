## Write a program to accept a string from the user and display characters that are present at an even index number.
# str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

try:
    str_1 = str(input("Enter a string: "))
except:
    print("Kya fook ke aaya bey")

for x in str_1:
    print(str[x,2])


"""for i in range(len(str_1)):
    if i % 2 == 0:
        print(str_1[i])
"""
"""
end_list = [x for x in str_1 if x % 2 == 0]

print(end_list)

"""


