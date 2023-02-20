bag = [1, 2, 4, 5, 6, 7, 8]
missing = []


def missing_nos(List, k):
    temp = 1
    for item in List:
        if temp == item:
            temp = temp + 1
            pass
        else:
            missing.append(temp)
            temp = temp + 2
    else:
        if not len(missing) == k:
            while len(missing) < k:
                missing.append(temp)
                temp = temp + 1
    print(missing)


missing_nos(bag, 3)
