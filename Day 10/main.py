from art import logo
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for op in operations:
        print(op)
    shouldContinue = True

    while shouldContinue:

        symbol = input("Type an operation symbol: ")
        num2 = float(input("What's the next number?: "))
        function = operations[symbol]
        result = function(num1,num2)
        print(f"{num1} {symbol} {num2} = {result}")
        yesOrNo = input(f"Type'y' to continue calculating with {result} or 'n' to start a new calculation: ")
        if yesOrNo == "y":
            num1 = result
        else:
            shouldContinue = False
            calculator()

calculator()