countries = ['Russia','German','France','Canada']
print (f'I have been to {len(countries)} countries')
print ('Countries I would like to visit will not offer a visa fast enough.')
print (f'I can not visit {countries[0]}\n')
countries[0] = 'United State'
for c in countries:
	print (f'\tI desire to visit {c}.')
countries.append('Aus')
countries.append('NZ')
countries.append('JP')
print ('\nI have more fund.\n')
countries.insert(0,'ROC')
countries.insert(4,'KR')

for d in countries:
	print (f'\tNew invittion message to {d}.')

print ('\nOil price increases, I can only go to 2 countries\n')
while len(countries) > 2:
	print ('\tI can not apply to '+countries.pop())

print (countries)
for e in countries:
	print (f'\tI will still apply to {e}.')
del countries[0:]
print (countries)