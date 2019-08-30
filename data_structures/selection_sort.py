def selection_sort(un_li=[]):

    for i in range(len(un_li)):

        l_index = i

        for j in range(len(un_li[i:])):

            if un_li[l_index] > un_li[j]:
                l_index = j

            print(i, j, l_index)

            print(un_li[l_index])

        un_li[l_index],un_li[i] = un_li[i],un_li[l_index]

        print(un_li)










selection_sort([3, 9, 99, 72, 0])
