favorite_food =['Burgers','Chicken','Pizza','BBQ']
print ('I like to eat '+favorite_food[0])
print ('I like to eat '+favorite_food[1])
print ('I like to eat '+favorite_food[2])
print ('I like to eat '+favorite_food[3])
friend_food =['Burgers','Chicken','Pizza','BBQ']
favorite_food.append('Beef')
friend_food.append('Beef')

for i in favorite_food:
	print (f"My favorite types of food are {i}")
for k in friend_food:
	print (f'\tmy friend’s favorite types of food are: {k}')

