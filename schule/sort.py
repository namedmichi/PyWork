def meinefunktion(n):
  
  return abs(n % 2)

meinezahlen = [100, 50, 64, 82, 23]
meinezahlen.sort(key = meinefunktion)
print(meinezahlen)      