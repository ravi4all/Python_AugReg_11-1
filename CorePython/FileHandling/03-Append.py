name = input("Enter your name : ")
age = input("Enter your age : ")

file = open('userData.txt', 'a')
file.write(name + " " + age + "\n")
print("Data written successfully")

file = open('userData.txt', 'r')
data = file.read()
print(data)

file_1 = open("demo.txt", 'w')
file_1.write(data)

file_1.close()

file.close()
