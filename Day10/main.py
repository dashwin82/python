


# Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculate():
    num1 = int(input("What's is the first number?: "))
    should_continue = True
    for symbol in operations:
        print(symbol)

    while should_continue:
        operation_symbol = input("Pick a operation from the symbol?: ")
        num2 = int(input("What's is the second number?: "))

        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type y to cotinue calculating {answer}, or type 'n' to start a new calculation?: ").lower() == 'y':
            num1 = answer
        else:
            should_continue = False
            calculate()

calculate()


