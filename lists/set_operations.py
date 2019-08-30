# WAP to accept two lists and write functions to find union, intersection and inverse intersections of those two lists.

def union(l1=[], l2=[]):

    t1=intersection(l1,l2)
    t2=inverse_intersection(l1,l2)

    return t1+t2


def intersection(l1=[], l2=[]):

    in_li=[]

    l1=unique_list(l1)
    l2=unique_list(l2)

    if len(l1) < len(l2):
        for val in l1:
            if val in l2:
                in_li.append(val)
    elif len(l2) <= len(l1):
        for val in l2:
            if val in l1:
                in_li.append(val)

    return in_li



def inverse_intersection(l1=[], l2=[]):

    l1=unique_list(l1)
    l2=unique_list(l2)

    inv_li=[]
    temp_li=l1+l2

    for val in temp_li:
        if val in l1 and val in l2:
            do_nothing()
        else:
            inv_li.append(val)

    return inv_li

def do_nothing():
    pass


def unique_list(l1):

    uniq_li=[]

    for i in range(len(l1)):
        if l1[i] in l1[i+1:]:
            do_nothing()
        else:
            uniq_li.append(l1[i])

    return uniq_li





l1=[1,1,2,3,4,5,6,7,7,7,8]
l2=[7,7,7,8,9,0,1,2,3]

print(union(l1,l2))

print(intersection(l1,l2))

print(inverse_intersection(l1,l2))





""" for val in temp_li:
        if val in l1 and val in l2:
            in_li.append(val)

    print(in_li)
"""
