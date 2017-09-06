name = input("Enter your name : ")
age = input("Enter your age : ")

file = open('userData.txt', 'w')
file.write(name + " " + age)
print("Data written successfully")

file.close()
