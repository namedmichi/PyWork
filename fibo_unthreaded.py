fiboNum = [1, 1]


def fibo(n):
    i = 0
    while i < n:
        ergebniss = fiboNum[i] + fiboNum[i+1]
        i = i + 1
        fiboNum.append(ergebniss)
    return fiboNum[n]


print(fibo(34))
