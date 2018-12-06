#this is 3-4
peoples = ['Robin','Anthony','Alex','Steven']
message = ' u wanna come to the dinner?'
for people in peoples:
	print ("Hey " + people + message)

#Robin cannot come to dinner
print (peoples[0]+' cannot come to dinner.')
peoples[0] = 'Eric'
print ("Hey " + peoples[0] + message)

#print the second set of invitation
for people in peoples:
	print ("Hey " + people + message)

