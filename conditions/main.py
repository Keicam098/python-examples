a = 9
b = 5

# struktura warunków w Pythonie 

if a > b:
    print("a jest większe od b")
elif a < b:
    print("a jest mniejsze od b")
else:
    print("a i b są równe")

# warunek jednoliniowy
print("a i b są równe") if a == b else print("a i b nie są równe")

# warunek z łącznikiem and gdy oba zwracają True to wyświetli sie komunikat
if b >= 5 and a <= 10:
    print("a jest mniejsze lub równe 10 a b jest większe lub równe 5")

# warunek z łącznikiem or gdy jeden jest prawidłowy to wyświetli się komunikat 
if a != 10 or b > 3:
    print("a nie jest równe 10 lub b jest większe od 3")

# warunek  z argumentem pass używany jest w gdy deklarujemy warunek bez jego ciała
if b > a:
    pass

# iteracja po liście 
fruits = ["jablko", "pomarancza", "sliwka"]

# sprawdzanie za pomocą warunku czy dany element istnieje w liście
if "jablko" in fruits:
    print("jablko znajduje się w liście owoce")

car = {
    "producent": "BMW",
    "model": "e46"
}

# sprawdzanie z pomocą warunku czy dany klucz istnieje w słowniku i czy zawiera wartość e36

if "model" in car:
    print("w słowniku określony jest model")
    if car["model"] == "e36":
        print("modelem auta jest e36")