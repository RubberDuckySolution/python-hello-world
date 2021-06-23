######### DATA TYPES ##############
def explain_strings():
    # Built in data type 1: str (string)
    # Python uses the str type to handle words/letters/sentences, anything involving text
    my_string = 'hello'
    print(f'my_string = {my_string}')
    print(f'type of my_string = {type(my_string)}')

    # There are a number of built in methods for working with strings
    # You can see what functions are available in an IDE like Visual Studio Code or in a python terminal
    print(f'capitalized: {my_string.capitalize()}')
    print(f'number of l letters in string: {my_string.count("l")}')
    print(f'ends with letter o: {my_string.endswith("o")}')

    # we can also combine strings using the + operator, eg
    my_sentence = my_string + " world"
    print(my_sentence)
    print(type(my_sentence))
    # Other operations like - (subtract), * (multiply), / (divide), throw an error as it is not clear
    # how to perform those actions on strings


def explain_numbers():
    # Built in data type 2: int, float, complex (numbers)
    # int is used to represent whole numbers, eg 1, 47, 987283
    # float is used to represent decimal point numbers, eg 1.232, 92.48, 100.1
    # complex is used to represent complex numbers (ie imaginary numbers)

    my_integer = 1
    my_float = 3.2

    # python automatically handles the types as a result of performing operations
    # eg
    integer_result = my_integer + my_integer
    print(f'integer addition result: {integer_result} has type: {type(integer_result)}')

    float_result = my_integer + my_float 
    print(f'float addition result: {float_result} has type: {type(float_result)}')


# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview