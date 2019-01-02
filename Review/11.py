universities = ['UIUC','Stanford','ITHU']
print ('I want to apply to '+str(len(universities))+' universities\n')
print ("I can't attend to "+universities[2]+'\n')
universities[2] = 'NTU'
for universitie in universities:
	print ('I want to attend to '+ universitie)
print ('\nI have more application money')
universities.insert(0,'Columbia University')
universities.insert(1,'Yale University')
universities.append('University of California–Berkeley')

