




def mergelists(l1,l2):
    i=j=0
    l3=[]

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i=i+1
        else:
            l3.append(l2[j])
            j=j+1

    if i < len(l1):
        l3.extend(l1[i:])
    else:
        l3.extend(l2[j:])

    print(l3)



if __name__ == "__main__":

    l1=[1,2,3,5]
    l2=[1,1,3,4,5,7,8,10,111]

    mergelists(l1,l2)
