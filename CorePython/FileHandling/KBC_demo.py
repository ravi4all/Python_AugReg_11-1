# opt1 = ['Yogi', 'Modi', 'Arvind', 'Lalu']
# opt2 = ['Java Virtual Machine', 'Javascript VM', 'Java Visited Machine', 'Java Virtual Model']
ans = ['Modi','Java Virtual Machine']
money = [1000,2000,5000,10000,20000,40000,80000,160000,10000000,70000000]
opt = [
    ['Yogi', 'Modi', 'Arvind', 'Lalu'],
    ['Java Virtual Machine', 'Javascript VM', 'Java Visited Machine', 'Java Virtual Model']
       ]
with open('ques.txt', 'r+') as file:
    while True:
        for i in range(2):
            a = file.readline()
            print(a)
            print("""
Options - {}
            """.format(opt[i]))
            user_ans = input("ans: ")
            if user_ans in ans:
                print("Sahi Jawab...")
            else:
                print("Sorry...Try next time...")
                break
        break
