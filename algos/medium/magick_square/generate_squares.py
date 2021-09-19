
m = [[2, 9, 4], 
	[7, 5, 3], 
	[6, 1, 8]]

n = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

m = [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

for el in n:
	print(el)
	
for el in m:
	print(el)


print(new_matrix)