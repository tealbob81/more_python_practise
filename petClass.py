class Pet():
    allowed = ['cat', 'dog', 'fish', 'rat']

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} as a pet!")
        self.species = species

cat = Pet('The Cat', 'cat')
dog = Pet('Bear', 'dog')


print(cat.species)





#print(f'{dog.name} is a {dog.species}')
