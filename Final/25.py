name = 'apple'
if "APPLE".lower() == name:
	print(f'I love {name}')

num1 = input('Input the number: ')
num = int(num1)
print (f'The num is {num}')
#inequal
if num != 99:
	print ('The number is not 99')
else:
	print ('The number is 99')
#bigger
if num > 90:
	print ('The number is greater than 90')
else:
	print ('The number is smaller than 90')
#smaller
if num < 90:
	print ('The number is smaller than 90')
else:
	print ('The number is greater than 90')
#> or =
if num >= 90:
	print ('The number is greater than or equal 90')
else:
	print ('The number is smaller than or equal 90')
#< or =
if num <= 90:
	print ('The number is smaller than or equal 90')
else:
	print ('The number is greater than or equal 90')