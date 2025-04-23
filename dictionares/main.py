# tworzenie słownika
car = {
    "producent": "Toyota",
    "model": "Corolla",
    "rocznik": 2003,
    "bite": False
}

# sprawdzenie ilości elementów słownika
print(len(car))

# sprawdzenie typu zmiennej car
print(type(car))

#tworzenie słownika za pomocą konstruktora 
dictConstructor = dict(producent = "BMW", model = "e36", rocznik = 1998, bite = True)

#wyciąganie ze słownika wartości o kluczu model
print(car["model"])

#wyciąganie ze słownika wartości o kluczu marka
print(car.get("producent"))

#wyświetlanie nazw kluczy słownika
print(car.keys())

#przypisanie do klucza model wartości e46

dictConstructor["model"] = "e46"
print(dictConstructor)

#sprawdzenie wartości słownika 
print(car.values())

#wyświetlenie zbiorów wartości klucz : wartość w słowniku
print(car.items())

# dodanie nowej danej do słownika
car.update({"kolor": "srebrny"})
print(car)
car["przebieg"] = 140000
print(car)

#usunięcie elementu o kluczu kolor 
car.pop("kolor")
print(car)

#usunięcie ostatnio dodanego elementu
car.popitem()
print(car)

#wyczyszczenie słownika
dictConstructor.clear()
print(dictConstructor)