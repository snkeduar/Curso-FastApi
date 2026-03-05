#Funciones en python

#parametros
#def hello(greet="Hello", name="invitado"):

#parametros con valor por defecto
def hello(greet="Hello", name="invitado"):
    print(f"{greet}, {name}")

#argumentos
hello("Hola", "Eduardo")
hello()

#keyword arguments
hello(name="Teddy", greet="Hello")


def big_function(*args, **kwargs):
    print(args)
    print(kwargs)
    return kwargs

print(big_function(1,2,3,4,5,6,7, num1=77, num2=100))