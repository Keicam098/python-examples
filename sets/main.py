# tworzenie setów z danymi o różnym typie
fruits = {"jablko", "pomarancza", "sliwka"}
numbers = {3, 4, 6, 9}
logic = {True, False}
mixed = {True, 9, "krzeslo"}
list = ["monitor", "myszka"]

#tworzenie setu za pomocą konstruktora
setConstuctor = set(("pomidor", "marchew", "papryka"))

# sprawdzanie typu zmiennej fruits
print(type(fruits))

#sprawdzenie długości setu
print(len(numbers))

#rozszerzanie setu o inny set
mixed.update(numbers)
print(mixed)
logic.update(list)
print(logic)

# dodawanie elementów do setu
fruits.add("kiwi")
print(fruits)

# usuwanie danej ze setu
logic.remove(True)
print(logic)
logic.discard("myszka")
print(logic)

#usuwanie losowej danej ze setu
print(numbers)
numbers.pop()
print(numbers)

#czyszczenie setu
logic.clear()
print(logic)

#usuwanie setu z pamięci
del logic

#łączenie dwóch setów
fruitsNumbers = fruits.union(numbers)
print(fruitsNumbers)

mixedLogic = mixed | numbers
print(mixedLogic)