#this is 3-10
#this is 3-4
peoples = ['Robin','Anthony','Alex','Steven']
message = ' u wanna come to the dinner?'
message2 = ' I found a BIGGER table!!!'

print (sorted(peoples))

Joy =peoples
Joy.sort(reverse=True)
print(Joy)

print (reversed(peoples))


#invitation
for people in peoples:
	print ("Hey " + people + message)

#starting 3-5
#Robin cannot come to dinner
print ('\n'+peoples[0]+' cannot come to dinner.'+'\n')
peoples[0] = 'Eric'
print ("Hey " + peoples[0] + message+'\n')

#print the second set of invitation
print ('\n')
for people in peoples:
	print ("Hey " + people + message)

#print the third set of invitation
print ('\n')
for people in peoples:
	print ("Hey " + people + message2)

#Add new to beginning of ur list
peoples.insert( 0,'Tony')

#Add new in the middle
peoples.insert( 3,'Marco')

#Add new in the end
peoples.append('Luda')

#Once again print
print ('\n')
for people in peoples:
	print ("Hey " + people + message)


#start of 3-7
#print only two can be invited
print ('\nDear Mr.Sheep u can only invite 2 people for dinner!')

#Sorry for kicking
print ('\n')
while len(peoples) > 2:
	kick = peoples.pop()
	print ('Sorry ' + kick +' you can come to my party next time')

#Still inviting
print ('\n')
for people in peoples:
	print ("Hey " + people + message)

del peoples[0:]
print (peoples)