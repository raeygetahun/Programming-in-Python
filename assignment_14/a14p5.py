class Person:
    def __init__(self,firstname,lastname,profession):
        self.firstname = firstname
        self.lastname=lastname
        self.profession=profession
        
    def setfirstname(self,firstname):
        self.firstname=firstname
    
    def setlastname(self,lastname):
        self.lastname=lastname
        
    def setprofession(self,profession):
        self.profession=profession
    
    def getfulldata(self):
        return f"{self.firstname} {self.lastname} is a {self.profession}."
        
        
person = Person("Raey", "Getahun", "Student")
print(person.getfulldata())