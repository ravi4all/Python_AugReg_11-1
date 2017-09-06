opt1 = ['Yogi', 'Modi', 'Arvind', 'Lalu']
opt2 = ['Java Virtual Machine', 'Javascript VM', 'Java Visited Machine', 'Java Virtual Model']
with open('ques.txt', 'r+') as file:
    while True:
        a = file.readline()
        print(a)
        print("""
a. Yogi             b. Modi
c. Arvind           d. Lalu
        """)
        ans = input("ans: ")
        if ans == 'Modi':
            print("Sahi Jawab...")
        else:
            print("Sorry...Try next time...")
            break

