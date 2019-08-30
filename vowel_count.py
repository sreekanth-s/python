word=str(input("Enter a string to calculate the number of vowels in the string.: "))

char="aeiouAEIOU"

a=e=i=o=u=A=E=I=O=U=0

for z in range(len(word)):
#    print(word[z])
    for j in range(len(char)):
        if word[z] == char[j]:
            vars()[char[j]]+=1


print("a=",a,"e=",e,"i=",i,"o=",o,"u=",u,"A=",A,"E=",E,"I=",I,"O=",O,"U=",U)
