list = [1, 2, 3, 4, 5]


def product_of_others(list):
    end_list = []
    leng = len(list)
    temp_list = list[:]
    for x in range(leng):
        temp_list[x] = 0
        temp_prod = 1
        temp_list.remove(0)
        for item in temp_list:

            temp_prod = temp_prod * item
        else:
            end_list.append(temp_prod)
            temp_list = list[:]
    print(end_list)


product_of_others(list)
