def meinefunktion(n):
    return lambda a: a * n


verdoppler = meinefunktion(2)
verdreifacher = meinefunktion(3)

print(verdoppler(11))

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)
x = abs(-7.25)

print(x)
