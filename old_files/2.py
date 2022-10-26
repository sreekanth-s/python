def min_max_of_a_list(l1=[]):

    if l1 == []:
        print("")

    less = great = l1[0]

    for value in l1:
        if value < l1[0]:
            less = value
        elif value > l1[0]:
            great = value

    print(less)
    print(great)


min_max_of_a_list([1,2,3,6,0])
