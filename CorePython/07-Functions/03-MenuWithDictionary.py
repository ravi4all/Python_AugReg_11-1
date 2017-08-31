def add():
    result = num_1 + num_2
    print(result)

def sub():
    result = num_1 - num_2
    print(result)

def div():
    result = num_1 / num_2
    print(result)

def mul():
    result = num_1 * num_2
    print(result)

def errHandler():
    print("Wrong choice, Enter again")


while True:

    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))

    result = 0

    print("""
    1. Addition
    2. Subtraction
    3. Divide
    4. Multiply
    5. Press q to Quit
    """)

    choice = input("Enter your choice : ")

    todo = {
        "1" : add,
        "2" : sub,
        "3" : div,
        "4" : mul,
        "q" : quit
        }

    todo.get(choice, errHandler)()
