current_users = ['admin','centos','unbuntu','debian','windows']
new_users = ['centos','debian','MacOSX','fedora','red_hat']
print (current_users)
print (new_users)
for new_user in new_users:
	if new_user in current_users:
		print ('This name is taken already.')
	elif new_user.lower() in current_users:
		print ('This name is taken already.')
	elif new_user.upper() in current_users:
		print ('This name is taken already.')
	elif new_user.title() in current_users:
		print ('This name is taken already.')
	else:
		print ('Congratuation, this username is avaliable for now.')
