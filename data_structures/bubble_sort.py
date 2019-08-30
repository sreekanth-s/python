def bubble_sort(un_li=[]):

    un_len=len(un_li)

    while un_len > 0:

        for i in range(0, un_len-1):

            if un_li[i] > un_li[i+1]:
                un_li[i],un_li[i+1] = un_li[i+1],un_li[i]

        un_len = un_len - 1

    print(un_li)

    return un_li


bubble_sort([3,4,7,2,1,6,9,0])
