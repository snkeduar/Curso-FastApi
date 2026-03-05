#and 
age = 25
lecensed = True

if age >= 18 and license:
    print("Puedes manejar")


# Or 
is_student = False
membership = True

if is_student or membership:
    print("obtiene precio especial")

# not 
is_admin = False
if not is_admin:
    print("Acceso denegado")


# Short Circuiting
name = False
print(name and name.upper())
