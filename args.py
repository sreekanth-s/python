def range_add_odd_and_even(lb, ub, include_ub=True):

    even_sum=0
    odd_sum=0

    if include_ub == False:
        upper=ub
    else:
        upper=ub+1

    for value in range(lb, upper):

        if value%2 == 0:
            even_sum = even_sum + value
        else:
            odd_sum = odd_sum + value

    return even_sum, odd_sum

    print(even_sum)
    print(odd_sum)





a,b=range_add_odd_and_even(1, 10)

print(a, b)

print(type(a))

print(type(b))

b=range_add_odd_and_even(1, 4, False)

print(type(b))

print(b)
