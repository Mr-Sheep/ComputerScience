persons = {
	'Peter':['1','2','3','5'],
	'Anthony':['1456','245','34','56'],
	'Steven':['41','452','3546','234'],
	'Eric':['1','43','13','15'],
	}
for key,names in persons.items():
	print (key+ "'s favorite num is ")
	for name in names: 
		print("\t" + name)