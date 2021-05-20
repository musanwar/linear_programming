matrix = [list(map(int, i.split(" "))) for i in input().split(";")]
pos = []

while min(matrix[0]) < 0:
	z = matrix[0]
	ind = z.index(min(z))

	iter_columns = [ [i[ind], i[-1]] for i in matrix ]

	min_val = -1 
	for i in range(len(iter_columns)):
		j = iter_columns[i]
		try:
			x = j[1] / j[0]
			if x > 0 and ( x < min_val or min_val == -1 ):
				min_val, min_val_pos = x, i
		except:
			pass

	pivot_row = [ j / matrix[i][ind] for j in matrix[min_val_pos]]
	
	for i in range(len(matrix)):
		matrix[i] = [matrix[i][j] + (pivot_row[j] * -matrix[i][ind]) for j in range(len(matrix[i]))]
	matrix[min_val_pos] = pivot_row
	pos.append(ind)
	print(matrix)
for i in pos:
	try:
		print(i, matrix[[j[i] for j in matrix].index(1)][-1])
	except:
		pass