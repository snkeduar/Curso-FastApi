user = {
    "name": "Ricardo",
    "age": 29,
    "email": "eduar-150@gmail.com",
    "active": True,
    (19.12, -98.32): "Cancún México"
}

print(user)
user["name"] = "Eduardo"
user["age"] = 35
print("geolocalizacion: ", user[(19.12, -98.32)])
print("usuario modificado: ", user)

print("items: ", user.items())
print("Values: ", user.values())
print("keys: ", user.keys())
user["country"] = "México"
print(user)
