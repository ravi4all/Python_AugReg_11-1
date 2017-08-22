def calculator(x,y, ch):

    if ch == "1":
        return x + y
    elif ch == "2":
        return x - y
    elif ch == "3":
        return x/y
    elif ch == "4":
        return x*y
    else:
        quit()

def main():

    while True:
        print("""
        1. Add
        2. Sub
        3. Div
        4. Mul
        5. Mod
        6. Pow
        7. Quit
        """)

        todo = {
            "1" : calculator,
            "2" : calculator,
            "3" : calculator,
            "4" : calculator,
            "q" : quit
        }

        user_choice = input("Enter your choice : ")

        num_1 = int(input("Enter first number : "))
        num_2 = int(input("Enter second number : "))

        print(todo.get(user_choice)(num_1, num_2, user_choice))

        user_input = input("Do you want to continue : ")

        if user_input == "yes":
            main()
        else:
            quit()


if __name__ == '__main__':
    main()