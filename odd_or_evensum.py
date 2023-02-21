list = [2, 4, 3, 5, 6]


def sum_odd_even(list):
    evensum = 0
    oddsum = 0
    final = []
    for item in list:
        if item % 2 == 0:
            evensum = evensum + item
        else:
            oddsum = oddsum + item
    final.append(evensum)
    final.append(oddsum)
    return final


print(sum_odd_even(list))
