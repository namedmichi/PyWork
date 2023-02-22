dic = {"#": 5, "O": 3, "X": 1, "!": -1, "!!": -3, "!!!": -5}

list = ["#", "!", "!!", "X", "!!!"]


def checkscore(list):
    sum = 0
    for item in list:

        try:
            sum = sum + dic[item]
        except:
            print("Falsche werte eingegeben")
            quit()

    if sum > 0:
        return sum
    else:
        return 0


print(checkscore(list))
