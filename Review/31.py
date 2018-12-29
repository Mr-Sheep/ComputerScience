def ss(a):
	n = len(a)
	for i in range(n):
		for k in range(n-i-1):
			if a[k] > a[k+1]:
				a[k],a[k+1] = a[k+1],a[k]
	return a

print (ss (a = [1.3, 3.4, 3.9, 3.3, 2.8, 2.2, 3.7]))