words = ['Hi', 'I', 'Am']

print('Dear '+ words[0]+', do you want this gift?')
print('Dear '+ words[1]+', do you want this gift?')
print('Dear '+ words[2]+', do you want this gift?')
print(words[2] + " can't go to this party")

words[2] = 'Runald'


words.insert( 0 ,'Alex')
words.insert( 2 ,'Boron')
words.append('Carbon')


print(words)

print(sorted(words))
print(words)

print(sorted(words, reverse=True))
print(words)

print(sorted(words, reverse=True))
print(words)

print(sorted(words))
print(words)

print(sorted(words, reverse=True))
print(words)

print(len(words))

kick = words.pop()
print ('Sorry '+ kick)

kick = words.pop()
print ('Sorry '+ kick)

kick = words.pop()
print ('Sorry '+ kick)

kick = words.pop()
print ('Sorry '+ kick)

print('Dear '+ words[0]+', do you want this gift? The place that we will meet is Joy')
print('Dear '+ words[1]+', do you want this gift? The place that we will meet is Joy')

del words[0:]
print (words)  