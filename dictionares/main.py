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

# skopiowanie słownika do nowej zmiennej 
newCar = car.copy()
newCar2 = dict(car)

cars = {
    "auto1": {
        "producent": "Audi",
        "model": "A3",
        "rocznik": "2003"
    },
    "auto2": {
        "producent": "BMW",
        "model": "e36",
        "rocznik": "1998"
    },
    "auto3": {
        "producent": "Toyota",
        "model": "Yaris",
        "rocznik": "2009"
    },
    "auto4": {
        "producent": "Fiat",
        "model": "Punto",
        "rocznik": "2007"
    },
}
print(cars["auto2"]["producent"])
print(cars["auto3"]["rocznik"])