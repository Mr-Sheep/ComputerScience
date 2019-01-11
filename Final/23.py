books =['A Man Called Ove','Life After Life','The Book Thief']
friend_book = books[:]
books.append('The Immortal Life of Henrietta Lacks ')
friend_book.append('The Nightingale')
for c in books:
	print (f'My favorite books are {c}')
for d in friend_book:
	print (f"\tMy friend's favorite books are {d}")