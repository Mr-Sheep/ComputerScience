age1 = input ('Age: ')
age = int(age1)
if age < 2:
	print ('Is a baby.')
elif age >= 2 and age <4:
	print ('Is a toddler.')
elif age >= 4 and age < 13:
	print ('Is a kid')
elif age >= 13 and age < 20:
	print ('Is a teenager')
elif age >=20 and age <65:
	print ('Is an adult.')
else:
	print ('Is a elder.')
