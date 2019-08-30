#! /usr/bin/python3.6
'''
string = str(input("Enter a string to manipulate: "))

print("This is the string you entered :", string)

print("This is the same string in Upper case: ", string.upper())

print("This is the string in Lower case: ", string.lower())

print("This is the string that has it's first charecter replaced by * in rest of the string : ", string[0]+string[1:].replace(string[0],"*"))
'''
'''
##### Plaindrome

if string == string[::-1]:
    print("String is a palindrome ")
else:
    print("String is not a palindrome")
'''

#### If the string is a rotation

str1=str(input("Enter a string: "))
str2=str(input("Enter a string: "))

#print(ord(str1)+ord(str2))



if len(str1) == len(str2):
    if str1=="" or str2=="":
        print("You haven't entered a string. Try again...  ")
    elif str1 == str2:
        print("Strings are the same")
    elif str1 in str2[::-1]*2:
        print("str1 and str2 are in some anticlock rotation")
    elif str1 in str2*2:
        print("str1 and str2 are some clock rotation. ")
        print(str2*2)
else:
    print("str2 and str1 are not equal. ")







'''
    val1=str1.index(str2[0])
    print(val1)

    chk1=str2[val1]+str2[val1+1]
    val2=str1.rfind(chk1)


    for i in range(len(str2)):

'''






'''
    for i in len(str2):





    if ( ( str2[0] in str1) and ( str2[0] == str1[0] )):
        val=str1.index(str2[0])
        tmp=str1[val:]+str1[:val]
        if tmp == str2:
            print("The given strings are in clockwise")
else:
    print("Enter valid input chut")


# for i in range(len(str2)):

#   lllalll
#   lalllll



#       lejlkwefoiwejiw
#       lkwefoiwejiwlej


'''

'''
Help on method_descriptor:

endswith(...)
S.endswith(suffix[, start[, end]]) -> bool

Return True if S ends with the specified suffix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
suffix can also be a tuple of strings to try.
'''















































































###########
