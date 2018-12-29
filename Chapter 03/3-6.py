#this is 3-4
peoples = ['Robin','Anthony','Alex','Steven']
message = ' u wanna come to the dinner?'
message2 = ' I found a BIGGER table!!!'



#全部改成print
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