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

    # types of strings in python
    # may be declared with single or double quotes
    string_with_quotes = '{"a":"blah"}'
    print(string_with_quotes)
    
    # f strings allow you to insert variables or the output of some code in a string
    var_string_1 = f'I have a cool json blob check this out: {string_with_quotes}'
    var_string_2 = f'1 + 1 = {1+1}'
    print(var_string_1)
    print(var_string_2)
    
    # before f strings were introduced, you could insert values in to strings (string interpolation) using the format() function
    # Notice how we can provide strings as positional and/or as keyword arguments to the format() function
    var_string_3 = 'hi {}, my {thingy} is {}, sup with {}'.format(
        'John',
        'Jane',
        'Bob',
        thingy = 'name'
    )
    print(var_string_3)
    
    # Because indentation is extremely important to python syntax, theres a way to declare multi-line strings
    # using three single or double quotation marks lets python interpret new lines correctly
    multiline_string = """asdj
ajsgdsah
askdhasjgdl\ra
asdgkhgsadkja
iaushdjashgdjk
hgasdhjgasa"""
    print(multiline_string)

    # python also has r strings (or raw strings) that tells it to interpret the backslash character literally
    # computers represent new lines or line breaks as \n or \r\n depending on the system (windows, mac, linux, etc)
    # ie the \ character is used to 'escape' strings and signify a special character, we use raw strings in python to avoid this
    string_with_newline = 'hello\r\nworld'
    literal_string = r'hello\r\nworld'
    print(string_with_newline)
    print(literal_string)




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


def explain_boolean():
    # Built in data type 3: bool
    # bool is used to represent boolean values, ie True or False

    my_truth = True
    my_false = False

    print(f'true variable = {my_truth}')
    print(f'false variable = {my_false}')

    # Using an if statement we can perform some action depending on wether the variable evaluates to true or false
    # From these below statements we should only see one of them print
    if my_truth:
        print('Variable was true!')

    if my_false:
        print('Variable was false!')



def explain_collections():
    # Built in data type 4: Sequences - ie list, tuple, range
    # Built in data type 5: Maps - ie dict
    # Built in data type 6: Sets - ie set, frozenset

    # TODO: flesh out examples here
