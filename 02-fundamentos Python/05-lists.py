# Estructura de datos que almacenan valores

list_numbers = [1,2,3,4,5,2,2]
list_letters = ['a', 'b', 'c', 'd']
list_mix = [ 2, 'z', True, [1,2,3], 5.5]

shopping_cart = ["Laptop", "Silla Gamer", "Café"]

print(type(list_mix))

# Métodos

# append
print(list_numbers)
list_numbers.append(100)
print(list_numbers)

# remove
list_numbers.remove(4)
print(list_numbers)

#count
print(list_numbers.count(2))

# .copy
# .sort()
