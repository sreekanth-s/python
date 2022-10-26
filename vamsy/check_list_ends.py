## Write a function to return True if the first and last number of a given list is same. If numbers are different then return False

def check_list_ends(input_list):
    if input_list[0] == input_list[-1]:
        return True
    else:
        return False 

