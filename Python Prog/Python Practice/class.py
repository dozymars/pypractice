class printer:
    def __init__(self, prop1, prop2):
        self.prop1 = prop1
        self.prop2 = prop2
    
catridge = printer("black", "colour")

print(catridge.prop1)
print(catridge.prop2)



class Monitor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

sn = Monitor("wide", 29)

print(sn.name)

print(sn.age)

