def calculator(x,y, opr):
    return eval(x+opr+y)

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
            "1" : "+",
            "2" : "-",
            "3" : "/",
            "4" : "*",
            "q" : quit
        }

        user_choice = input("Enter your choice : ")

        num_1 = input("Enter first number : ")
        num_2 = input("Enter second number : ")

        # print(todo.get(user_choice)(num_1, num_2, user_choice))
        opr = todo.get(user_choice)
        print(calculator(num_1,num_2,opr))

        user_input = input("Do you want to continue : ")

        if user_input == "yes":
            main()
        else:
            quit()


if __name__ == '__main__':
    main()