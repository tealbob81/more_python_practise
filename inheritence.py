class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f'this animal says {sound}')

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species='Cat')
        self.breed= breed
        self.toy = toy

    def play(self):
        return f'{self.name} plays with {self.toy}!'

the_cat = Cat('The Cat', 'Cutie', 'Bear')

print(the_cat)
print(the_cat.species)
print(the_cat.breed)
print(the_cat.toy)
print(the_cat.play())












##class Human():
##    def __init__(self, first, last, age):
##        self.first = first
##        self.last = last
##        self._age = age
####
####    def get_age(self):
####        return self._age
####
####    def set_age(self, new_age):
##
##    @property
##    def age(self):
##        return self._age # access the '_age' property
##
##    @age.setter
##    def age(self, value):
##        if value >= 0:
##            self._age = value
##        else:
##            raise ValueError("age can't be negative!")
##
##    @property
##    def full_name(self):
##        return f'{self.first.title()} {self.last.title()}'
##
##    
##    
##
##
##jane = Human('Jane', 'Goodall', 34)
####print(jane.get_age())
####jane.set_age(45)
####print(jane.get_age())
##
##print(jane.age) # no need to 'call' function. No parens needed
##jane.age = 20
##print(jane.age)
##print(jane.full_name)
##
##
##
##


