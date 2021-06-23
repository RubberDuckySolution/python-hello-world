# This is a comment line, anything starting with # will be ignored by the compiler

# Import statements live here at the top of the file
# Some libraries are default in any python environment and will always be available
# Others will require being installed via 'pipenv' before they can be used
import io

# You can import code from other python files within the same project too
# We use the syntax: from {file path} import {function/class names}
from functions import describe_arguments, describe_argument, describe_all_kwarguments, \
describe_kwarguments, describe_no_arguments, return_multiple_values, return_sum


# Next you define the functions and classes your script will call
def perform_action(argument1, argument2):
    print(f'First argument: {argument1}')
    print(type(argument1))

    print(f'Second argument: {argument2}')
    print(type(argument2))

    result = argument1 + argument2
    print(f'arg1 + arg2: {result}')
    print(f'type of arg1 + arg2: {type(result)}')

    # the return statement will end the function and return whatever follows it 
    return result


def test_perform_action():
    # In python adding numbers works as you'd expect, ie 1 + 2 = 3
    print('============================================')
    result = perform_action(1,2)
    print(result)
    print(type(result))

    print('============================================')
    # In python when we add two strings, they get combined (concatenated) in to one
    # ie 'a' + 'b' = 'ab' 
    result = perform_action('a', 'b')
    print(result)
    print(type(result))

    print('============================================')
    # The commented code below wont work, as the perform_action function tries to add two dictionaries together
    # But a dictionary type in python has no built in method for the + operation 
    # 
    # result = perform_action({'a':1,'b':2}, {'c':3})
    # print(result)
    # print(type(result))


def test_arguments():
    print('============================================')
    describe_argument('hello')
    print('============================================')
    describe_arguments("print", "this", "string", "please")
    print('============================================')
    describe_kwarguments(thing='hello', stuff='goodbye')
    print('============================================')
    describe_all_kwarguments("print", "this", "string", "please", thing='hello', stuff='goodbye')
    print('============================================')
    describe_no_arguments()
    print('============================================')


def test_returning():
    print('============================================')
    print('Adding 1 & 2:')
    added_numbers = return_sum(1, 2)
    print(added_numbers)
    
    print('============================================')
    print('Getting values from: 3, "hello"')
    # Here we can return the values to specific variables
    # eg I know this will return exactly 2 values
    value1, value2 = return_multiple_values(3, 'hello')
    print(f'value1 = {value1}')
    print(f'value2 = {value2}')

    print('============================================')
    # Say we did not know how the return_multiple_values function worked, only that it returns multiple values
    # instead of trying value1 = ... value2 = ... value3 = ... until we find what works, we can do this:
    values = return_multiple_values(3, 'hello')
    # values will contain everything returned by the function as a 'Tuple' type of variable
    print(values)
    print(type(values))
    # We can use the built in function len() to find how many items were returned
    print(len(values))
    print('============================================')
    


# A special line that means the code will only run when the script is executed
# But prevents the code being run if imported in another python file
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
# This is the entry point for where our script starts, the main method
if __name__ == '__main__':
    print('running main application')

    # test_perform_action()
    test_arguments()
    test_returning()