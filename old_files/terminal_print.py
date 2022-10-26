"""
This is the documentation text of the function say
This is how you say.
"""

def say(message, times=1):
    """
    prints message number of times.
    """

    print(message * times)

def shout(message, times=1):
    """
    prints capitalized message number of times.
    """

    print(str.capitalize(message) * times)
