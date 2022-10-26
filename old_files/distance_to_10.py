num=int(input("Enter a number to count it's distance from 10: "))

def distance_to_10(num):

    # maintain a count to calculate the iterations
    count=0

    # check if the number is euqal to 10 first
    if num == 10:
        print("You've entered 10")

    # if the number is > 10, count
    elif num > 10:
        while num != 10:
            num = num - 1
            count+=1

        print(count)
        return count

    elif num < 10:
        while num != 10:
            num = num + 1
            count+=1

        print(count)
        return count




distance_to_10(num)
