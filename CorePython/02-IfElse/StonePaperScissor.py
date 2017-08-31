import random

cpu_choice = ['stone','paper','scissor']

cpu = random.choice(cpu_choice)

gameExit = True

while gameExit:

    user_input = input("Enter your choice : ")

    if user_input == cpu:
        print("CPU Choice is : ",cpu)
        print('Tie')
    elif user_input == 'stone' and cpu == 'scissor':
        print("CPU Choice is : ",cpu)
        print('You Win')
    elif user_input == 'paper' and cpu == 'stone':
        print("CPU Choice is : ",cpu)
        print('You Win')
    elif user_input == 'scissor' and cpu == 'paper':
        print("CPU Choice is : ",cpu)
        print('You Win')
    elif user_input == 'stone' and cpu == 'paper':
        print("CPU Choice is : ",cpu)
        print('CPU Win')
    elif user_input == 'paper' and cpu == 'scissor':
        print("CPU Choice is : ",cpu)
        print('CPU Win')
    elif user_input == 'scissor' and cpu == 'stone':
        print("CPU Choice is : ",cpu)
        print('CPU Win')
    else:
        print("Wrong choice,Enter again")
        gameExit = False
