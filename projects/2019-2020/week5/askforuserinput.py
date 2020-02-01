
def ask_user_input():
    #Ask user for information
    operator = input("Introduce an operation\n")
    try: 
        number1 = int(input("Introduce your first number\n"))
        number2 = int(input("Introduce your second number\n"))
    except ValueError:
        print("Numbers must be integers\n")
    return (operator, number1, number2)
    # We're returning a 3-tuple
    # A tuple is a sequence of immutable Python objects. 
    # Tuples are sequences, just like lists. 
    # The differences between tuples and lists are, the tuples cannot be changed unlike 
    # lists and tuples use parentheses, whereas lists use square brackets. 
    # Creating a tuple is as simple as putting different comma-separated values.    

def do_operation(operator, number1, number2):
    ''' Operate two numbers using operations variable 
        @operator: String 
        @number1: Integer
        @number2: Integer
    '''
    if operator == '+':
        result = number1 + number2
        print(result)
    elif operator == '-':
        result = number1 - number2
        print(result)
    elif operator == '*':
        result = number1 * number2
        print(result)
    elif operator == '/':
        try:
            result = number1 / number2
            print(result)
        except ZeroDivisionError:
            print("Error during the operation: You can't divide by 0\n")


# Main body of the program # 
data_to_operate = ask_user_input()
# Result of ask_user_Input is returned as a tuple, so we have to access it as a list
do_operation(operator=data_to_operate[0], number1=data_to_operate[1], number2=data_to_operate[2])