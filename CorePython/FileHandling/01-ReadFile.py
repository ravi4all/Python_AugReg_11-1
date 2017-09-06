file = open('demo.txt', 'r')

print(file.read())

file.close()

file_1 = open("demo_1.txt", 'w')
file_1.write("This file is written with python")
file_1.close()
