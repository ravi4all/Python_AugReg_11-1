class Avenger:

    def __init__(self,name,power,skills):
        self.name = name
        self.power = power
        self.skills = skills

    def __str__(self):
        return "Name : "+self.name+ " Powers : "+self.power+ " Skills : "+self.skills