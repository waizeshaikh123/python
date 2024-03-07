class person:
    def __init__(self, n ,oc):
        self.name = n
        self.occupation = oc

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person("zohaib", "shopkeeper")
a.info()