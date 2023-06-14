def snakefill(n):
	tiles = n * n
	length = 1
	count = 0
	while True:
		length = length * 2
		count += 1
		if length > tiles:
			return count - 1

print(snakefill(24))