class Programmer:
    def __init__(self, name, salary, skills):
        self.name = name
        self.salary = salary
        self.skills = skills
    def getSkills(self):
        print(f"{self.name}'s skills are:")
        for i in self.skills:
            print(i)
Achyut = Programmer("Achyut Srivastava", 40000000, ['Python', 'HTML', 'CSS', 'C', 'Javascript', 'Django'])
Prakhar = Programmer("PKP", 4000000000000000000000, ['Python', 'Javascript', 'HTML','CSS' ])

Achyut.getSkills()
Prakhar.getSkills()