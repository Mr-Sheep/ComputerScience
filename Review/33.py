def ss(a):
	n = len(a)
	times = 0
	for i in range(n):
		for k in range(n-i-1):
			if a[k] > a[k+1]:
				a[k],a[k+1] = a[k+1],a[k]
				times = times * times+1
	print (f'The worst time {times}')
	return a
print (ss (a = [38, 4, 84, 19, 54]))

