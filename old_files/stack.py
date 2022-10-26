'''
Stacks and queues walkthrough



'''


# stack can be implemented using a list.
stack = []






Recursion:

- Recursion is a methodology where you call the defined function in itself.
For example

def countdown(x=1):         # define countdown
    if (x == 0):            # break condition
            print("done")
            return
    else:
            print(x,"...")
            countdown(x-1)  # call the same function
            
