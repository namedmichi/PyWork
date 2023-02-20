

def XaO(s):

    counterx = 0
    countero = 0
    for item in s:
        if item == "x":
            counterx = counterx + 1
        elif item == "o":
            countero = countero + 1
    if counterx == countero:
        return True
    else:
        return False


text = "xox"

if XaO(text):
    print("ja")
