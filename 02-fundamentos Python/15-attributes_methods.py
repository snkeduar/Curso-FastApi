class Person:
    species = "Humano"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._energy = 100 # Protección simulado por convensión
        self.__password = "1234" #Atributo privado

    def work(self):
        return f"{self.name} está trabajando duro."
    
    def _waste_energy(self, quantity):
        self._energy -= quantity
        return self._energy
    
    def __generate_password(self):
        return f"$${self.name}-{self.age}$$"
    
person1 = Person("Ricardo", 29)
person2 = Person("Eduardo", 35)

print(person1.work())
#print(person1.__password)
print(person1._Person__password)
#print(person1.__generate_password())
print(person1._Person__generate_password())
print(person1._waste_energy(10))
print(person2.work())