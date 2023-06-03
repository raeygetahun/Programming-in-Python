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
    
    def areEqual(self,newPerson):
        if(self.lastname==newPerson.lastname and self.firstname==newPerson.firstname):
            return True
        else:
            return False
        
    def isGreaterthan(self,newPerson):
        if(self.lastname>newPerson.lastname or self.lastname==newPerson.lastname and self.firstname>newPerson.firstname):
            return True
        else:
            return False
        
    def isLessthan(self,newPerson):
        if(self.lastname<newPerson.lastname or self.lastname==newPerson.lastname and self.firstname<newPerson.firstname):
            return True
        else:
            return False
    
        
person = Person("Raey", "Getahun", "Student")
person2 = Person("Zaey", "Getahun", "Student")
print(person.isGreaterthan(person2))