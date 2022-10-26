def armstrong(num=0):
    """Python program to check if the number provided by the user is an Armstrong number or not take input from the user"""
    # initialize sum
    sum = 0
    # find the sum of the cube of each digit
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
    # display the result
    if num == sum:
       return True
    else:
       return False





if __name__ == "__main__":
    print(armstrong(-153))
    print(armstrong(13))
