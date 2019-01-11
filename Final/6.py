countries = ['Russia','German','France','Canada']
print (f'I have been to {len(countries)} countries')
print ('Countries I would like to visit will not offer a visa fast enough.')
print (f'I can not visit {countries[0]}')
countries[0] = 'United State'
for c in countries:
	print (f'I desire to visit {c}.')