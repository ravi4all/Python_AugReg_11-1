import random

a = ['stone', 'paper', 'scissor']

game = True

while game:
    cpu_choice = random.choice(a)
    user_choice = input("Enter your choice : ")
    print("CPU Choice is",cpu_choice)

    if cpu_choice == user_choice:
        print("Match Tie")
    elif user_choice == 'stone' and cpu_choice == 'scissor':
        print("You win")
    elif user_choice ==  'scissor' and cpu_choice == 'paper':
        print("You win")
    elif user_choice == 'paper' and cpu_choice == 'stone':
        print("You win")
    elif user_choice == 'stone' and cpu_choice == 'paper':
        print("CPU win")
    elif user_choice ==  'scissor' and cpu_choice == 'stone':
        print("CPU win")
    elif user_choice == 'paper' and cpu_choice == 'scissor':
        print("CPU win")
    else:
        print("Try Again")