class Animal:
    def __init__(self, type, name, color, age):
        self.type = type
        self.name = name
        self.color = color
        self.age = age

    def nac(self):
        print('Type of animal: ', self.type)
        print('Name of animal: ', self.name)
        print('Color of animal: ', self.color)
        print('Age of animal: ', self.age)


cat = Animal('Lion', 'Martin', 'orange', 3)

print(cat.nac())
