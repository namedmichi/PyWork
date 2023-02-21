import math

a = [2, 5]
b = [10, 7]


def line_segment(v1, v2):
    x1 = v1[0]
    x2 = v2[0]
    y1 = v1[1]
    y2 = v2[1]
    temp1 = pow((x2 - x1), 2)
    temp2 = pow((y2 - y1), 2)
    temp1 = temp1 + temp2
    result = math.sqrt(temp1)
    return round(result, 2)


print(line_segment(b, a))
