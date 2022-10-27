## Write a program to find how many times substring “star” appears in the given string.

input_string = "something something something something"
substring = "thing"

def find_substring(input_string, substring):
    return input_string.count(substring)
    
print(find_substring(input_string, substring))