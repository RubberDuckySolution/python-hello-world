############ FUNCTION ARGUMENTS ############

# The signature of the function is: 
#       def - special keyword in python to indicate a function is being defined
#       describe_arguments - the function name
#       (single_argument) - the function parameters, ie the arguments or data you provide the function to perform work on
def describe_argument(single_argument):
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
def describe_arguments_2(single_argument, *argv):
    print(f'First argument : {single_argument}')
    
    print('All following arguments:')
    for arg in argv:
        print(arg)


# **kwargs is more special python syntax that allows us to give arguments with names, rather than by position
#       eg describe_arguments(amount=5, multiplier=2, name='scott')
#       eg describe_arguments(5, 2, 'scott')
def describe_kwarguments(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')


# We can combine both methods to have a dynamic list of arguments, as well as named ones
#       eg describe_arguments("print", "this", "string", "please", name='scott', amount=5)
def describe_all_kwarguments(*argv, **kwargs):
    print('All following arguments:')
    for arg in argv:
        print(arg)

    for key, value in kwargs.items():
        print(f'{key} : {value}')


# A function may take no arguments at all:
def describe_no_arguments():
    print('I dont do much at all')




########### FUNCTION RETURN STATEMENTS ############
# So far the functions shown in this file just print information without doing anything (you may remember this as void functions in c++)
# Generally we want a function to actually do or change something, we have it give us this result via a return statement 
def return_sum(x, y):
    print(f'Got numbers: {x} & {y}')
    # Here we create a new variable called result
    # We assign it the value of the provided numbers added together
    result = x + y
    # Now we use the keyword 'return' which ends the function and gives the value of result
    return result


# We can also return multiple values from a function    
def return_multiple_values(a_number, a_string):
    print(f'Received a number: {a_number}')
    doubled = 2*a_number
    print(f'Number x 2: {doubled}')

    upper = a_string.upper()
    print(f'Received a string: {a_string}')
    print(f'String in uppercase: {upper}')

    return doubled, upper


# We can return no value (at least explicity) like a void function
# We will see that python returns something on our behalf anyway
def return_no_values(x, y):
    print(x)
    print(y)
