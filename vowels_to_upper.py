'''
this program converts the vowels given in a string to UPPERCASE
for example sai to sAI
'''

s=str(input("Enter a string: "))
'''
for i in range(len(s)):
    if s[i] == 'a' or 'e' or 'i' or 'o' or 'u':
            print(s[i].upper())
    else:
            print(s[i])
'''

for i in range(len(s)):
    if s[i] in ('a' , 'e' , 'i' , 'o' , 'u'):
            print(s[i].upper(),end='')
    else:
            print(s[i],end='')

print()
