import sys

#vocab is a map

vocab = {}

total=0

for line in sys.stdin.readlines(): 
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
	if tag not in vocab:
		vocab[tag] = 0
	total=total+1
	vocab[tag] = vocab[tag] + 1
print(vocab)
print(total)

print("# P", "\t", "count", "\t", "tag", "\t", "form")

#keep a counter for the total number of tokens
for tag in vocab:
	freq=vocab[tag]/total
	print('%.2f' % (freq), "\t", vocab[tag], "\t",tag, "\t", "_")

#make a matrix of word → tag and a separate frequency list for tags

