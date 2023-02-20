
text = []
while True:
    temp = int(input("gebe eine Zahl ein. Wenn fertig 000 eingeben "))
    if temp == 000:
        break
    else:
        text.append(temp)


text.sort()

deci = input("asc oder desc? ")
if deci == "asc":
    print(text)
elif deci == "desc":
    text.reverse()
    print(text)
