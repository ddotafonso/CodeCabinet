
class Manager:
    def __init__(self, name):
        self.name = name
        
    def getName(self):
        print(f"Welcome to" + " " + self.name)
        
        

kfc = Manager("KFC")
kfc.getName()