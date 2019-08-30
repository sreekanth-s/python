num1=int(input("Enter a  number: "))

















for x in range(num1,0,-1):
	print("*"*(x*2-1))
	for y in range (x,num1+1):
		print(" ", end="")
