# tupla zawierająca wartości tekstowe

fruits = ("jablko", "pomarancza", "sliwka")

# tupla zawierająca liczby

numbers = (5,8,2,6,9)

# tupla zawierająca wartości logiczne

logic = (True, False, True)

# tupla zawierająca wartości mieszane

mixed = (True, "jablko", 5)

# tworzenie tupli za pomocą konstruktora

tuple_constructor = tuple(("krzeslo", "stolik", "monitor"))

# sprawdzenie typu zmiennej tuple_constructor

print(type(tuple_constructor))

#dostęp do danych tupli za pomocą 

print(fruits[0])
print(fruits[-1])
print(fruits[2:4])
print(fruits[:3])
print(fruits[2:])

#zmiana wartości tupli za pomocą konwesji listy ponieważ tupla nie jest modyfikowana
x = list(fruits)
print(type(fruits))
print(type(x))
x[0] = "kiwi"
fruits = tuple(x)
print(fruits)
print(type(fruits))

#dodawanie danych do tupli poprzez konwersji 

y = list(fruits)
y.append("jablko")
fruits = tuple(y)
print(fruits)

# usuwanie danej do  tupli za pomocą konwersji
z = list(tuple_constructor)
z.remove("monitor")
tuple_constructor = tuple(z)
tuple_constructor
