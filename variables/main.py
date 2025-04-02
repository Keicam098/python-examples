# to jest komentarz
x = 5 # zmienna przechowuje liczbę całkowitą (int)
name = "Maciej" # zmienna przechowuje ciąg znaków (string)
is_human = True # zmienna przechowuje wartość logiczną (bool)

# przykłady deklaracji zmiennych 
text = "to jest ciąg znaków"
number = 24
float_variable = 2.4
logic_variable = True


# sprawdzenie typów zmiennych
print(type(text))
print(type(number))
print(type(float_variable))
print(type(logic_variable))


#wielokrotne przypisanie wartości
color, is_fruit, quantity = "red", True, 2

j = k = "jabłko"

print(j,k)

#wyświetlenie zawartości zmiennych 

print(color)#red
print(is_fruit)#true
print(quantity)#2

# Łączenie ciągów znaków 

first_part = "SLI"
second_part ="MAK"
full_text = first_part + second_part #SLIMAK

#Zmiana typów zmiennych 

print(full_text)

string_age = "10" 
int_age = int(string_age)#konwersja string -> int

print(type(string_age))
print(type(int_age))

int_quantity = 5
float_quantity = float(int_quantity) #konwersja int -> float 

print(type(int_quantity))
print(type(float_quantity))

int_height = 180
string_height = str(int_height) #konwersja int -> string

print(type(int_height))
print(type(string_height))

# usunięcie zmiennej z pamięci 

del_variable = 10

print(del_variable)
del del_variable

print(del_variable) #błąd - nie ma zmiennej w pamięci 
