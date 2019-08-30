string=input("Enter a string that you want to reverse: ")

print("Entered string is ",string)

new_string=[]

old_string=[]


#for i in range(len(string)):
	
#	print(string[i],end='')
	

print("Reversed string is:",end=" ")

for i in range(len(string)):

	print(string[-(i+1)],end='')

	old_string.append(string[i])

	new_string.append(string[-(i+1)])


print()

#print(old_string)
#print(new_string)
	

if old_string == new_string:
	print("You know what, you entered a palindrome")

