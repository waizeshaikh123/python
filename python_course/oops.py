class Person:
    name = "waize"
    s_name = "shaikh"
    def info(self):
        print(f"{self.name} is a {self.s_name}")



a = Person()
b = Person()
a.name = "zohaib"
a.s_name = "mangwano"

b.name = "sahil"
b.s_name = "ghori"
a.info()
b.info()
