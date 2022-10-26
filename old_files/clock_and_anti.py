str1=input("Enter a string: ")
str2=input("Enter a string: ")

if str2[0] in str1:
    val=str1.index(str2[0])
#    tmp=str2[val:]+str2[:val]
    tmp=str1[val:]+str1[:val]
    print(tmp)
    print(val)
else:
    print("Enter valid input chut")

if tmp == str2:
    print("Clock")
