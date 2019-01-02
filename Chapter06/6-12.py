cities = {
	'Chengdu':{
		'loc':'China',
		'pop':'14.43 million',
		'fact':'No actual war.'
	},
	'Los angeles':{
		'loc':'United State',
		'pop':'4 million',
		'fact':'Disney Land here!'
	},
	'Chicago':{
		'loc':'United State',
		'pop':'2.716 million',
		'fact':'All airports names from WWII'
	}
}
for city,info in cities.items():
	print ('City: '+city)
	info_info = info['loc']+'\n\t'+info['pop']+'\n\t'+info['fact']

	print ('\t'+ info_info)