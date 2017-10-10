import sys

table = {}

table["a"] = "ⴰ"
table ["b"] = "ⴱ"
table ["bh"] = "ⴲ"
table ["g"] = "ⴳ"
table ["ghh"] = "ⴴ"
table ["dj"] = "ⴵ"
table ["d"] = "ⴷ"
table ["dh"] = "ⴸ"
table ["dd"] = "ⴹ"
table ["ddh"] = "ⴺ"
table ["ey"] = "ⴻ"
table ["f"] = "ⴼ"
table ["k"] = "ⴽ"
table ["khh"] = "ⴿ"
table ["h"] = "ⵀ"
#table ["h"] = "ⵁ"
table ["hh"] = "ⵃ"
table ["ʿ"] = "ⵄ"
table ["kh"] = "ⵅ"
table ["q"] = "ⵇ"
table ["i"] = "ⵉ"
table ["j"] = "ⵊ"
table ["l"] = "ⵍ"
table ["m"] = "ⵎ"
table ["n"] = "ⵏ"
table ["ny"] = "ⵐ"
table ["ng"] = "ⵑ"
table ["p"] = "ⵒ"
table ["u"] = "ⵓ"
 #table ["w"] = "ⵓ"
table ["r"] = "ⵔ"
table ["rr"] = "ⵕ"
table ["gh"] = "ⵖ"
table ["s"] = "ⵙ"
table ["ss"] = "ⵚ"
table ["sh"] = "ⵛ"
table ["t"] = "ⵜ"
table ["th"] = "ⵝ"
table ["ch"] = "ⵞ"
table ["tt"] = "ⵟ"
table ["v"] = "ⵠ"
table ["w"] = "ⵡ"
table ["y"] = "ⵢ"
table ["z"] = "ⵣ"
#table [""] = "ⵤ"
table ["zz"] = "ⵥ"
table ["é"] = "ⵦ"
table ["o"] = "ⵧ"

#c = character

for line in sys.stdin.readlines():
	line=line.strip()

	if '\t' not in line:
		print(line)
		continue 
	#take the line and return a list of columns
	row = line.strip().split('\t')
	#if there aren't exactly ten columns skip the line
	if len(row) != 10:
		continue
	#apply transformation to the form column
	transliterated = row[1]
	for c  in table:
		transliterated = transliterated.replace(c, table[c])

	row[9]= "Translit="+transliterated
	out = "\t".join(row)
	print(out.strip())
