
def number_length(z):
    count = 0
    for item in z:
        count = count + 1
    return count


numb = input("Zahl eingeben: ")

print(number_length(numb))
