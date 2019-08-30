num=int(input("Enter a number: "))

def reverse_a_number(num):
    """ prints the digits of the number given in reverse order """
    rev_num = 0

    while(num > 0):
        rev_num = rev_num * 10 + num%10
        num = num//10

    return rev_num



if num > 0:
    print(reverse_a_number(num))

else:
    num = -1*num
    print(-1*reverse_a_number(num))
