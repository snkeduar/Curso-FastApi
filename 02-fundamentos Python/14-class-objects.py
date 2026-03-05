class Person:
    pass
# Una clase es como un molde donde se definen caracteristicas y comportamientos
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        return f"{self.name} está trabajando duro."

#Instanciar la clase
persona1 = Person("Eduardo", 35)
#Acceder a los metodos de la clase
#se le llama metdo a una función que vive dentro de una clase
print(persona1.work())
persona2 = Person("Jerson", 34)
print(persona2.work())