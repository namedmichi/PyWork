list = [18, 20, 60]


def up_down(tup, gup, gdown):
    schneller = gdown / gup
    tdown = tup / schneller
    tuph = tup / 60
    tdownh = tdown / 60
    sup = gup * tuph
    sdown = gdown * tdownh
    sges = sup + sdown
    tges = tuph + tdownh
    gesch = sges / tges
    return gesch


print(up_down(30, 10, 30))
