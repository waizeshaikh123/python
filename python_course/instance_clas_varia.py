class Employee:
    companyName = "Toyota"
    def __init__(self, name):
        self.name = name
        self.raisi = 0.4
    def details(self):
        print(f"name is {self.name} company name is {self.companyName} raise amount is {self.raisi}")
        
a  = Employee("waize")
a.raisi = 9
a.details()
b = Employee("zohaib")
b.companyName = "tata"
b.details()
# (Employee.details(a)) 