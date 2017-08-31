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
        result = num_1 + num_2
        print(result)

    elif choice == 2:
        result = num_1 - num_2
        print(result)

    elif choice == 3:
        result = num_1 / num_2
        print(result)

    else:
        result = num_1 * num_2
        print(result)
