c=10
type(type(c))


meta class



python
0123456

print(str[0:6])


 for -5 to 256 the value of id will be same for same integer declared.

id(s)

id(obj, /)
    Return the identity of an object.

    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)

WAP to greet a user


??????????????????????????????????????


str="sasfdakjekf"
s=3214
isinstance(s,str)

========================================================================================

- A new function is defined by the def keyword. ends with parantheses and a colon.
  all statments indednted under the def keyword are considered the block of the function.

            def some_function():
                return "This value is returned"     # the string is returned if you call the function.
                pass                                # pass is a keyword which says to not give any errors if nothing is performed in the function.

    For example, the following function does nothing and returns nothing.
    Write without pass and you should see an error.

            def some_function():
                pass


- Arguments in a function. rather how to define and pass them right.

    1. Positional argument


            def substract(num1, num2):
                pass        \     \_______ 2nd argument
                             \_____________________________1st argument


    2. Default arguments


            def circle_area(radius, pi=3.141):
                area = pi * (radius ** 2)  \________ default argument. if second argument is not passed, the default value is considered.
                return area


        Default arguments must be trailing. Meaning all the default arguments should be declared after the positional arguments.

    3. Keyword arguments.
       While calling a function, one can specifically specify the argument name and pass the values so that there is no need to follow the order.

       Define the function like this


            def substract(num1, num2):
                return num1 - num2


        and run like this.


            substract(num2=20, num1=10)


        so what this does is assign 20 to num2 and 10 to num1.
        You do not have to remember the position, but pass the value to the argument name.

        When you use positional and keyword arguments together, keyword arguments must be trailing.

        To accept a keyword argument and mandate it by passing keyword while calling function, write below.

            def some_function(*, keyword1 = 1):
                pass           \          \__________________ have to specify the keyword
                                \
                                 \______________________________ note no variable name after * indicating no positional arguments.


    4. Variable number of arguments.

            def add(*numbers):      # usual practice is to use *args, however, any name can be given
                pass

        A tuple is generated and you can work on the tuple in the function.
        Below is an example which uses variable arguments.

            def add(*args):
                res=0
                for val in range(numbers):
                    res += val
                return res

        Keyword arguments should be passed only after and positional should be before the variable arguments.

            def some_function(positional1, positional2, ...., *args, keyword1=1, keyword2=2, ...):
                pass

        The above rule is important because this is shit.

            def some_function( a, b, *args, c, d):



========================================================================================

__name__

    is a special
## This code is called Boiler plate. FTW

if __name__ == "__main__":
    print("Executing script as individual module")


========================================================================================

August 24
