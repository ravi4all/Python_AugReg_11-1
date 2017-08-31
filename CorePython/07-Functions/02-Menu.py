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


while True:

    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))

    result = 0

    print("""
    1. Addition
    2. Subtraction
    3. Divide
    4. Multiply
    """)

    choice = int(input("Enter your choice : "))

    if choice == 1:
        add()

    elif choice == 2:
        sub()

    elif choice == 3:
        div()

    else:
        mul()
