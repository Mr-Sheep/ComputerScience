#this is 4-11
pizzas = ['Pizza Marinara','Pizza Margherita','Neapolitan Pizza']
friend_pizzas = ['Pizza Marinara','Pizza Margherita','Neapolitan Pizza']

for pizza in pizzas:
	print ('I like '+pizza)
print ('I really love '+pizzas[1])
print ('I really love '+pizzas[0])
print ('I really love '+pizzas[2])
print ('\n')



pizzas.append('Pizza Pepperoni')
friend_pizzas.append('Pizza al Taglio')



for pizza in pizzas:
	print ('I like '+pizza)
for pizza1 in friend_pizzas:
	print ('My friend like '+pizza1)