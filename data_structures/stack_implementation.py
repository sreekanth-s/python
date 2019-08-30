def execution():

    opr = input("Enter an operation to perform: ")

    if opr == "1" or opr == "push":
        value = input("Enter a value to push: ")
        ret = stack_push(value)
        if ret == None:
            print("The stack is full. try popping. \n \n")
            execution()
        else:
            print("\n \n")
            execution()

    elif opr == "2" or opr == "pop":
        ret = stack_pop(sl)
        if ret == None :
            print("The stack is empty. try pushing. \n \n ")
            execution()
        else:
            print("\n \n")
            execution()

    elif opr == "3" or opr == "is_empty":
        ret = stack_is_empty(sl)
        if ret == True :
            print("The stack is indeed empty. \n \n")
            execution()
        else:
            print("The stack is not empty. ")
            execution()

    elif opr == "4" or opr == "peek" :
        ret = stack_peek(sl)
        if ret == None :
            print("The stack is empty. try pushing. \n \n")
            execution()
        else:
            print("The top most element is ", ret, "\n \n")
            execution()

    elif opr == "5" or opr == "size" :
        ret = stack_size(sl)
        print("The size of the stack is ", ret, "\n \n")
        execution()

    elif opr == "6" or opr == "stack_print" :
        stack_print(sl)
        execution()

    else:
        print(sl, "is the final stack ")
        pass


def stack_push(value):
    if len(sl) == s_size:
        return None
    else:
        sl.append(value)
        return sl


def stack_pop(sl):
    if sl == []:
        return None
    else:
        return sl.pop()


def stack_is_empty(sl):
    if len(sl) == 0:
        return True


def stack_peek(sl):
    if sl == []:
        return None
    else:
        return sl[-1]


def stack_size(sl):
    return len(sl)


def stack_print(sl):
    print("The stack size entered is ", s_size)
    print("The current stack is ", sl, "\n \n")
    return



if __name__ == "__main__":
    """ """

    s_size = int(input("Enter stack size: "))
    sl=[]
    if s_size < 1:
        print("Enter a valid size for stack.")
        exit
    else:
        print("you have selected a stack of size ", s_size)
        print("now you can perform below operations on the stack: \n \
        1. push         \n \
        2. pop          \n \
        3. is_empty     \n \
        4. peek         \n \
        5. size         \n \
        6. print        \n \
        ")
        execution()
