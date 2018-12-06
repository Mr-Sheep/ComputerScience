admins = ['centos','admin','ubuntu','debian','windows']
print ('enter your username: ')
login = input()
if login == 'admin':
	print ('Plz use "rm -rf in your terminal"')
else:
	print ('Hello '+ login +' the rm -rf command is not availiable for you.')