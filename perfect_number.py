num=int(input("Enter a number to check if the number is perfect: "))

sum=0

for i in range(1,num):
    if num%i==0:
        sum=sum+i

if sum == num:
    print("yay! you've entered a perfect number")
else:
    print("Sorry! ", num, " is not perfect")
