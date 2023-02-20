text = input("geben sie einen Text ein: ")
counter = 0
umlaute = {"a", "e", "i", "o", "u"}


for item in text:
    if item in umlaute:
        counter = counter + 1
print(counter)
