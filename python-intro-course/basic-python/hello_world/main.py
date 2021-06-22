# This is a comment line, anything starting with # will be ignored by the compiler
# Import statements live here at the top of the file
# Some libraries are default in any python environment and will always be available
# Others will require being installed via 'pipenv' before they can be used
import io

# You can import code from other python files within the same project too
from functions import describe_arguments


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


def test_arguments():
    describe_arguments("print", "this", "string", "please")



# A special line that means the code will only run when the script is executed
# But prevents the code being run if imported in another python file
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
# This is the entry point for where our script starts, the main method
if __name__ == '__main__':
    print('running main application')

    result = perform_action(1,2)
    print(result)
    print(type(result))

    result = perform_action('a', 'b')
    print(result)
    print(type(result))