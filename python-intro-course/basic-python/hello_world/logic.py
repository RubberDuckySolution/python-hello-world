########### IF STATEMENTS #############
def example_if_statements():
    # if statements will evaluate the truth of some condition and then only execute the next block of code
    # given that it evaluates to true, otherwise it will skip over that block of code and continue on
    if 1 + 1 == 2:
        print('yep 1 + 1 is 2')

    if 1 + 1 == 3:
        print('hmmm 1 + 1 is 3??')

    my_number = 100
    print(f'let my_number = {my_number}')
    if my_number == 100:
        print(f'yes {my_number} is 100')

    if my_number > 1:
        print(f'yes {my_number} is greater than 1')


def example_else_statements():
    # say we want to evaluate a number of different conditions and decide from there what path of execution (or block of code)
    # we want to run depending on which turns out to be true - for this we use else statements

def print_if_true(to_print_or_not_to_print, statement):
    if to_print_or_not_to_print:
        print(statement)


def example_conditional_statements():
    # or
    # and
    # in
    if (1+1 == 2) or (1+1 == 3):
        print('something was true')

    if (1+1 == 2) and (1+1 == 3):
        print('everything was true')

    if (1+1 == 2) or (1+1 == 3) and (True == True):
        print('python chose the order to evaluate conditions')

    if ((1+1 == 2) or (1+1 == 3)) and (True == True):
        print('we used parentheses to control the order of evaluation')

    if (1+1 == 2) or ((1+1 == 3) and (True == True)):
        print('we used parentheses to control the order of evaluation')

    if (1+1 == 5) or ((1+1 == 3) and (True == True)):
        print('this print statement wont execute')


########### FOR STATEMENTS ############
def example_for_statements():



########### WHILE STATEMENTS ##########
 