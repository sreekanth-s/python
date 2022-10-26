##
##  A program which takes a series of inputs to add them to a list
##  and give out the average of the numbers.
##



number_of_items=int(input("Enter a positive number of items that the list contains: "))

num_list=[]

sum=0

for i in range(number_of_items):
#    print(i)
    num_list.append(int(input("Enter the number of the list: ")))
    sum=sum+(num_list[i])

print(round( (sum / len(num_list)), 3) , "is the average of all numbers in the list.")
#print(num_list)
