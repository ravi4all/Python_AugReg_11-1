import random

a = ["Hi","Hello","Hey","Heya","Namaste","Hie","Hola"]

while True:
    user = input("Enter your message : ")
    cpu_ans = random.choice(a)
    print(cpu_ans)
