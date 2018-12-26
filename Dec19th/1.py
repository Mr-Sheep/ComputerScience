#devide an algorithm to compute x的n, where x is a real number and n is an int
#{First give a procedure for computing x的n when n is none-negative by successive multiplication by x, starting with 1
#Then extend this procedure, and use  the fact that x的-n =1/x的n to compute when x is negative}

#procedure
#power (x: a real num, n: a interger)
#power :=1
#for number: = 1 to n
#	power: = power * x
#if n < 0 then power: 1/power


x_str = input ('Plz inout x: ')
n_str = input ('Plz input n: ')
n = int(n_str)
x = int(x_str)
#if x < 0:
#	answer = 1/x**n
#	print (answer)
#elif x > 0:
#	answer = x**n
#	print (answer)
#else:
#	print ('0')

for i in range(0,n):
