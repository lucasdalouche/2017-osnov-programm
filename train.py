import sys


lines = sys.stdin.readlines()

words = {}

total=0

for line in lines: 
	line=line.strip()

	if '\t' not in line:
		continue 

	#take the line and return a list of columns
	row = line.split('\t')

	#if there aren't exactly ten columns skip the line
	if len(row) != 10:
		continue

	tag = row[3]

	if "_" in tag:
		continue

	if tag not in words:
		words[tag] = 0

	total=total+1
	words[tag] = words[tag] + 1
print(words)
print("total of tagged words = ", total)

print("# P", "\t", "count", "\t", "tag", "\t", "form")

for tag in words:
	freq=words[tag]/total
	print('%.2f' % (freq), "\t", words[tag], "\t",tag, "\t", "_")