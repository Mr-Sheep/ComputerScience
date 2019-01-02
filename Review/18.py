movies = ['Spider-Man: Into the Spider-Verse','Black Panther','Bumblebee','Mission: Impossible - Fallout','Paddington 2']
movies_sort = sorted(movies)
for movie in movies:
	print ('I want to watch '+movie)
print ('\n')
for mo in movies_sort:
	print ('(Sort)I want to watch '+mo)

movies.reverse()
print ('\n')
for mov in movies:
	print ('2 I want to watch '+mov)
movies.reverse()
print ('\n')
for movi in movies:
	print ('3 I want to watch '+movi)

