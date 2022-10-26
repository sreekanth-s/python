def saa(n):
    i,j,s=0,1,1

    while (s<n):
        print(s)
        s=i+j
        i=j
        j=s
