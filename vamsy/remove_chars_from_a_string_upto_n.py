## Write a program to remove characters from a string starting from zero up to n and return a new string.
# remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.

try:
    input_string = str(input("Enter a string: "))
    input_number = int(input("Enter the number of chars to be removed: "))
except:
    print("Kindly enter the specified type only")

# str_length = len(input_string)

def remove_chars(input_string, input_number):
    return(input_string[input_number:len(input_string)])

new_string = remove_chars(input_string, input_number)

print(new_string)
