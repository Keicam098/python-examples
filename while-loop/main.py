i, x, y = 1, 1, 0

# pętla iterująca do 6
while i < 6:
    print(i)
    i += 1

#przerwanie pętli while
while x < 6:
    print(x)
    if x == 3:
        break
    x += 1

# else w pętli while
while y < 6:
    print(y)
    if y == 3:
        break
    y +=1
else:
    print("koniec iteracji")