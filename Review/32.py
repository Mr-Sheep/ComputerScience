def ss(a):
	n = len(a)
	for i in range(n):
		for k in range(n-i-1):
			if a[k] > a[k+1]:
				a[k],a[k+1] = a[k+1],a[k]
	return a

print (ss (a = [38, 4, 84, 19, 54]))

