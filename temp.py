def sum_of_numbers_in_alphanumeric_string(string=""):
    """count the sum of inidividual charecters that are numbers in a given string"""
    total = 0
    for val in string:
        if val.isnumeric():
            total=total+int(val)

    return total


#x=sum_of_numbers_in_alphanumeric_string("34g3v6456b456456b56b4n 64n7b46b6546.6")

#print(x)


def encoding_and_decoding(coded_str=""):
    """ """

    new_str = ""

    for i in range(len(coded_str)):
        tmp=1
        print(new_str)
        print(coded_str)
        print(i)
        new_str=new_str+coded_str[i]
        while coded_str[i] == coded_str[i+1] :
                tmp = tmp+1
                i = i + 1
#                print(i)
        coded_str=coded_str[i:]
#        print(coded_str)
        new_str=new_str+str(tmp)

    return new_str

y=encoding_and_decoding("sssaaaaaii")

print(y)
