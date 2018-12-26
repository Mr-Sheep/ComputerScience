inputs = [1,3,11,7,9]
number = 0
for q in inputs:
	if (q % 2) == 0:
		number = inputs.index(q)
	elif (q % 2) != 0:
		continue
	else:
		number = 0
print (number)