l1=[1,2,3,4,5,1,2,3,4,5]

s1=list(set(l1))

s1=[1,2,3,4,5]

d1={}

temp = 0
x=0
value=l1[0]
y=0

while s1 != []:
    if value in l1[x:]:
        temp = temp + 1
        d1[value] = temp
        if y == 0 and x == 0:
            break
        y=l1[x:].index(value)
        x=y+1





print(d1)







"""

#for value in l1:
temp = 0
x=1
for value in l1[x:]:
    temp = temp + 1
    d1[value] = temp
    x=l1[x+1:].index(value)
    print(x)


print(d1)


"""

"""

for value in s1:
    temp = 0
    x=0
    if value in l1[x:]:
        temp = temp + 1
        d1[value] = temp
        x=x+1

print(d1)

"""






def count_occurances(l1=[]):

    s1=set(l1)
    d1={}

    for value in s1:
        temp=0
        for i in l1:
            if value == i:
                temp=temp+1
                d1[value] = temp
    return d1


def min_max_of_a_list(l1=[]):

    less = great = l1[0]

    for value in l1:
        if value < l1[0]:
            less = value
        elif value > l1[0]:
            great = value

    print(less)
    print(great)



#print(count_occurances(l1))














"""

while i in range(len(l1)):
    if i in l1[value:]:

"""

"""

l1=[]

less = great = l1[0]

#print(temp)

for value in l1:
    if value < l1[0]:
        less = value
    elif value > l1[0]:
        great = value

print(less)
print(great)

"""

"""

def func(x,y=[]):
    y.append(24)
    print(x)
    print(y)

#func(x=1, y=[2,3])


def add_list(x,y=None):
    if y is None:
        y=[]
    y.append(x)
    print(y)

add_list(1)

add_list(2)

add_list(3)

add_list(4)


"""
