#5-5
alien_color = ('0:greem','1:yellow','2:red')
print (alien_color)
color = input('input: ')
score = 0
if color == '0':
	print ('You just got 5 points!')
	score = score +5
elif color == '1':
	print ('You just got 10 points!')
	score = score + 10
else:
	print ('You just got 15 points!')
	score = score + 15
print ('Your final score is '+score)
