universities = ['Harvard', 'Princeton University','beida']
universities.append('Columbia University')
universities.append('Massachusetts Institute of Technology')
universities.append('University of Chicago')

print('I can only apply to two universities')
print (universities)

while len(universities) > 2:
	for University in universities:
		pop = universities.pop()
		print ('I can not apply to ' + pop)
		print (len(universities))

print (universities)
