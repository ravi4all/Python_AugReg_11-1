with open('file_1.txt') as file:
    # for i in range(10):
    #     f = file.readline()
    #     print(f, end='')
    data = file.readlines()
    # print(data)
    for i in data:
        print(i, end="")
