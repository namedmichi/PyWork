try:
    print(3/0)
except ZeroDivisionError:
    print("Mit 0 geteilt")
except NameError:
    print("Variable nicht belegt")
else:
    print("geschaft")
