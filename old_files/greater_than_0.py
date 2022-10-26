import math

num=int(input("Enter a number: "))

if num>0:
	print("The number",num,"is greater than 0")
elif num==0:
	print("hutiya, the number is zero")
else:
	print("The number", num, "is less than 0")




new_string=[]

for i in range(len(string)):
	
	print(string[-(i+1)],end='')
	new_string.append(string[-(i+1)])

if string == new_string :
	print("You know what? You entered a palindorme")