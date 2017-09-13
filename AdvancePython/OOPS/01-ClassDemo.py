class MyFirstClass:
    print("My Class")

    def one(self):
        print("One function executed")


print(__name__)
if __name__ == '__main__':
    obj = MyFirstClass()
    obj.one()
