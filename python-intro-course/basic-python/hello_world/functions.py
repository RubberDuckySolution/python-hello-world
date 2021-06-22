# The signature of the function is: 
#       def - special keyword in python to indicate a function is being defined
#       describe_arguments - the function name
#       (single_argument) - the function parameters, ie the arguments or data you provide the function to perform work on
def describe_arguments(single_argument):
    print(f'First argument : {single_argument}')


# Notice this function has the same name as the last, this function will 'override' the last definition and will be called 
# This function also takes a special argument: *argv
#    *argv - built in python syntax to provide any number of arguments:
#    eg argv could equal "a"; or it could be "a", "b", "c"; or "a", "b", ... , "z"
def describe_arguments(*argv):
    print('All following arguments:')
    for arg in argv:
        print(arg)


# We can use both types of parameters, in case we know we need to treat the first argument differently
def describe_arguments(single_argument, *argv):
    print(f'First argument : {single_argument}')
    
    print('All following arguments:')
    for arg in argv:
        print(arg)


# **kwargs is more special python syntax that allows us to give arguments with names, rather than by position
#       eg describe_arguments(amount=5, multiplier=2, name='scott')
def describe_arguments(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')


# We can combine both methods to have a dynamic list of arguments, as well as named ones
#       eg describe_arguments("print", "this", "string", "please", name='scott', amount=5)
def describe_arguments(*argv, **kwargs):
    print('All following arguments:')
    for arg in argv:
        print(arg)

    for key, value in kwargs.items():
        print(f'{key} : {value}')


# A function may take no arguments at all:
def describe_arguments():
    print('I dont do much at all')




# FUNCTION OVERLOADING