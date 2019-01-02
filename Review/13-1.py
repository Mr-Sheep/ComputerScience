universities = ['UCLA','Stanford','ITHU']
print ('I want to apply to '+str(len(universities))+' universities\n')
print ("I can't attend to "+universities[2]+'\n')
universities[2] = 'NTU'
for universitie in universities:
	print ('I want to attend to '+ universitie)
print ('\nI have more application money\n')
universities.insert(0,'Columbia University')
universities.insert(1,'Yale University')
universities.append('University of California–Berkeley')

for universitie in universities:
	print ('Now I want to attend to '+ universitie)

print ('You have just been accepted to early admission by UCLA.')
print ('Unfortunately, their early admission rules limit you to applying to only 2 other universities')
while len(universities) > 2:
	print ('I can not apply to '+universities.pop())