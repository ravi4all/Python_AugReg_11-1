class Avenger:

    def __init__(self,name,power,skills):
        self.name = name
        self.power = power
        self.skills = skills

    def __str__(self):
        return "Name : "+self.name+ " Powers : "+self.power+ " Skills : "+self.skills

avengers_list = []

def add_avengers(name,power,skills):

    avengerId = 0
    avengerObj = Avenger(name,power,skills)
    avengerId +=1
    avengers_list.append(avengerObj)
    return avengers_list
