#Ask user for information
operator = input("Introduce an operation\n")
number1 = int(input("Introduce your first number\n"))
number2 = int(input("Introduce your second number\n"))

#Present information back to the user
print("The operation selected is " + operator)
if operator == '+':
    result = number1 + number2
    print(result)
elif operator == '-':
    result = number1 - number2
    print(result)