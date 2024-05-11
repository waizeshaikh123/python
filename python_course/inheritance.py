# class Employee:
#     def __init__(self, name ,id):
#         self.name = name
#         self.id = id
#     def details_emp(self):
#         print(f"{self.name} is {self.id}")
# class Programmer(Employee):
#     def Show_lang(self):
#         print("Python is not a default language")

# class Merge(Programmer,Employee):
#     def Show_more(self):
#         print(f"This is emploee class:{Employee}\nand this is:{Programmer}")
        
# em = Employee("Waize", 300)
# em.details_emp()
# eme = Programmer("zoahib", 800)
# eme.details_emp()
# eme.Show_lang()
# eme1 = Merge("sabtain",500)
# eme1.Show_lang()
# eme1.Show_more()


class Employee:
    def __init__(self,name ,idd):
        self.name = name
        self.idd = idd
    def showinfo(self):
        print(f'my name is {self.name} and value is {self.idd}')
        
class Programmers(Employee):
    def show(slef):
        print("i am a Programmer in Employee")
        
a = Programmers("waize",400)
a.show()
a.showinfo()

