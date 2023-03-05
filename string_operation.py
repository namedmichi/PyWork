text = "4 + 3"


def string_operation(text):
    a = text.split(" ")
    z1 = int(a[0])
    z2 = int(a[2])
    op = a[1]
    match op:
        case "+":
            result = z1 + z2
        case "-":
            result = z1 - z2
        case "*":
            result = z1 * z2
        case "//":
            result = z1 // z2
        case other:
            print("fehleingabe!")
    return result


print(string_operation(text))
