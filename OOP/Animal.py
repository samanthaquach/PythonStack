class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        print "Walking...", self.health
        return self
    
    def run(self):
        self.health -= 5
        print "Runing...", self.health
        return self

    def displayInfo(self):
        print('Animal: ' + str(self.name))
        print('Health: ' + str(self.health))
        print
        return self

class Dog(Animal):
    def Animal(self):
        return "Dog"
    
    def pet(self):
        self. health += 5
        print ("Dogs cannot fly..."), self.health
        return self

class Dragon(Animal):
    def Animal(self):
        return "Dragon"
    
    def fly(self):
        self.health -= 10
        print ("I am a dragon..."), self.health
        return self

class Fish(Animal):
    def Animal(self):
        return "Fish"

    def swim(self):
        self.health += 2
        print ("Just keep swimming..."), self.health
        return self

Animal1 = Animal("Lion", 100).walk().walk().walk().run().run().displayInfo()
Dog1 = Dog("French Bulldog", 150).walk().walk().walk().run().run().pet().displayInfo()
Dragon1 = Dragon("Mushu", 170).fly().fly().displayInfo()
Fish1 = Fish("Nemo", 200).swim().swim().swim().displayInfo()