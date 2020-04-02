from collections import defaultdict
d = defaultdict(list)

dict = {}
for x in range(8):
	dict[x] = [x+1]

for key, value in dict.items():
	dict[key].append([5, 7])
	dict[key].append(8)

print(dict[1][1])

print(dict)