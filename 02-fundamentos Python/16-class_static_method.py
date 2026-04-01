class Person:
    species = "Humano"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod # Se invoca solo a travez de la clase, Cambia los valores a nivel clase (afecta a todas las instancias)
    def change_species(cls, new_species):
        cls.species = new_species

    @staticmethod # Se invoca a nivel clase y nivel objeto
    def is_older(age):
        return age >= 18

person1 = Person("Ricardo", 12)
person2 = Person("Fernando", 35)

print(person1.species)
print(person2.species)

#person1.change_species("Reptiliano")
Person.change_species("Reptiliano")

print(person1.species)
print(person2.species)

print(Person.is_older(20))
print(person1.is_older(person1.age))