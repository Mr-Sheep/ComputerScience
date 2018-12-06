user = 'admin'
password = 'admin'
login1 = input ("username: ")
login2 = input ("password: ")
attempts = 0
okay = False
#attempting part
while attempts < 4:
	if login1 == user:
		if login2 == password:
			print ('Login successfully.')
			okay = True
			break
		else:
			attempts = attempts + 1
			print ('Bad password. You have '+str(attempts)+' tries.')
			continue
	else:
		print ("User doesn't exist")

#welcome page
if okay == True:
	print('Welcome to the system!')
else:
	print('Get out plz')