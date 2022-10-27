## Iterate the given list of numbers and print only those numbers which are divisible by 5

input_list=[1,2,3,4,5,10,12,15.5,20.0,100]

def divisible_by_5(input_list):
    for i in input_list:
        if i % 5 == 0:
            print(i)

divisible_by_5(input_list)