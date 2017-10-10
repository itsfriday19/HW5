import re

f = open("regex_sum_39997.txt", "r")
text = f.read()

found_nums = re.findall('[0-9]+', text)

convert = []
for n in found_nums:
	n = int(n)
	convert.append(n)

sum_ints = sum(convert)

print (sum_ints)