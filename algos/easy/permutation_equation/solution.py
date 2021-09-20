p = [5, 2, 1, 3, 4]

results = []
for i in range(len(p)+1):
	if i in p:
		# print(i, p.index(i)+1)
		val = i
		val_idx = p.index(i)+1
		if val_idx in p:
			print(p.index(val_idx)+1)
			results.append(p.index(val_idx)+1)


	