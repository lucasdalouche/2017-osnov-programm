import sys

table = {}

table["a"] = "A"
table ["u"] = "U"

#c = character

for line in sys.stdin.readlines():
	for c in table:
		print("c", table[c], line)
		line = line.replace(c, table[c])