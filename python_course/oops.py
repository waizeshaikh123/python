# class Person:
#     name = "waize"
#     s_name = "shaikh"
#     def info(self):
#         print(f"{self.name} is a {self.s_name}")

# a = Person()
# b = Person()
# a.name = "zohaib"
# a.s_name = "mangwano"

# b.name = "sahil"
# b.s_name = "ghori"
# a.info()
# b.info()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print(f"My name is {self.name} my age is {self.age}")
        
# a = Person("waize",20)
# b = Person("zohaib",22)

# a.info()
# b.info()

# def greet(fx):
#     def mfx(*args,**kwargs):
#         print("Hy hope You Enjoy")
#         fx(*args, **kwargs)
#         print("See you soon bye...")
#     return mfx

# @greet
# def hello():
#     print("hello world")
# hello()

# @greet
# def add(a,b):
#     print(a+b)
# add(3,4)

class Emp:
    companyName = "Samsung"
    def __init__(self,name):
        self.name = name
    def Sdetails(self):
        print(f"the print is name {self.name} My company is {self.companyName}")
e = Emp("waize")
e.companyName = 'Xiomi'
e.Sdetails()
e1 = Emp("zohaib")
e1.Sdetails()