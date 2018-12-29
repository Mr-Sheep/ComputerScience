person = {
	'Peter':'Python',
	'Joy':'C',
	'Robin':'Go',
	'Anthony':'Ruby',
	'Lily':'MySQL',

	}

people = ['yoyo', 'Joy', 'Peter', 'Robin', 'bobo']

for name in people:
    if name in person.keys():
        print('Thanks for taking the poll, ' + name.title())
    else:
        print('Please take the poll ' + name.title())