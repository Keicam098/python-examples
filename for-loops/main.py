fruits = ["banan", "jablko", "pomarancza"]

# pętla iterująca po liście
for fruit in fruits:
    print(fruit)
k = 0
# pętla iterująca po ciągu znaków
for letter in "jakiśtekst":
    if letter == "k":
        k=k+1


print(f"litera k występuje {k} razy w naszym ciągu znaków")

# pętla iterująca 6 razy 
for i in range(6):
    print(i)

# pętla iterująca od 2 do 6
for i in range(2,6):
    print(i)


# pętla iterująca od 2 do 30 co 3
for i in range(2, 30, 3):
    print(i)

# pętla iterująca po liście i wykonująca else gdy przeiteruje przez  wszystkie elementy
for fruit in fruits:
    print(fruit)
else:
    print("to cała lista owoców")

# continue pomija obrót pętli i idzie do następnego a break wychodzi z pętli
for i in range(10):
    if i % 2 != 0:
        continue
    elif i == 8:
        break
    else:
        print(i)

about_frutis = ["czerwony", "duży", "smaczny"]

# zagnieżdzenie pętli 
for x in about_frutis:
    for y in fruits:
        print(x,y)

# argument pass którego używamy aby zadeklarować pętle bez jej ciała
for x in [0, 1, 2]:
    pass
