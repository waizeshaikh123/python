class emplot:
    company= "aplle"
    def show(self):
        print(f"the name is {self.name} and company name is {self.company}")
    @classmethod
    def chngcompany(cls,newcompany):
        cls.company = newcompany
        
# creating object of the class  
emp1 = emplot()
emp1.name = "waize"
emp1.show()
emp1.chngcompany("tesla")
emp1.show()
