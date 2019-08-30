#!/usr/bin/python

lb=int(input("Enter a lower bound: "))
ub=int(input("Enter a upper bound: "))

if lb < ub:
	print("Even numbers in given range are: ")
	while(lb!=ub):
		if lb%2==0:
			print(lb)
		lb=lb+1
else:
	print("Enter bounds as specified.")
