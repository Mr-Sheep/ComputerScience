a = [234,654654,344,124,987]
n = len(a)
for i in range(1,n-1):
	for k in range(n-i):
		if a[k] > a[k+1]:
			a[k], a[k+1] = a[k+1],a[k]
print (a)