class Emp:

    __name = None
    __age = None
    __salary = None
    __company = None

    def companyName(self):
        print("Company is",self.company)

    def bio(self):
        print("Employee is {} {} {}".format(self.name, self.age, self.salary))

    def dept(self, *department):
        print("Department is",department)

    def classVar(self):
        n = input("Enter new emp : ")
        self.__name = n
        print("New Emp is", self.__name)


emp = Emp()
emp.name = "Ram"
emp.age = 22
emp.salary = 12000
emp.company = "HCL"

emp.dept('IT','HR','Sales')
emp.companyName()
emp.bio()


emp_2 = Emp()
emp_2.name = "Shyam"
emp_2.age = 23
emp_2.salary = 15000
emp_2.company = "HP"

emp_2.bio()


emp_3 = Emp()
emp_3.classVar()
