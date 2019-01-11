amin = 0
amax = 0
a = [77, -10, 177, 83, 68]
for i in a:
	if i < amin:
		amin = i
	elif i - amin > amax:
		amax = i - amin
