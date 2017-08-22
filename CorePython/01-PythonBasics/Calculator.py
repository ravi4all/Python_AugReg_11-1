def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def div(x,y):
    return x/y

def mul(x,y):
    return x * y


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
            "1" : add,
            "2" : sub,
            "3" : div,
            "4" : mul,
            "q" : quit
        }

        user_choice = input("Enter your choice : ")

        num_1 = int(input("Enter first number : "))
        num_2 = int(input("Enter second number : "))

        print(todo.get(user_choice)(num_1, num_2))

        user_input = input("Do you want to continue : ")

        if user_input == "yes":
            main()
        else:
            quit()

        # if user_choice == 1:
        #     add()
        # elif user_choice == 2:
        #     sub()
        # elif user_choice == 3:
        #     div()
        # elif user_choice == 4:
        #     mul()
        # else:
        #     quit()


if __name__ == '__main__':
    main()