#!/usr/bin/python3.6

print("value of __name__ in test.py is {}".format(__name__))

import arithmatic

if __name__=="__main__":
    res=arithmatic.add(10,20)
    print("Result is {}".format(res))
