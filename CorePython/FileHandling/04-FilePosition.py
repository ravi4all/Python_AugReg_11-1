file = open('demo_1.txt', 'r+')

# data = file.read()
# print(data)

# Will start reading from 3rd character
# file.seek(50)
# print(file.read())

# file.seek(2)
# print(file.read())
# print("-------------------------")
# file.seek(2,0)
# print(file.read())

file.seek(-5,0)
print(file.read())

file.close()
