""" Variables are used in python to store the values"""
"""Rules
* Variable names starting with (a-z)(A-Z) letters and _(underscore)
* It should not starts with any numbers or special charcters 
* Variable names are Case sensitive """

"""To create a variable A and Print"""

"""A = "Hello"
print(A)"""

"""Variables are divided by Two types
1. Local Variables(This variales scode inside the function only
2. Global Variables( This variable scope Throught the function)"""


"""global var"""
a = "Hi"
def variable():
    a = "hello"
    print(a)
    """Local Var"""
variable()
print(a)