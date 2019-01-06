ss = ['711','Family Mart','Whole Food','Target','Walmart']
for s in ss[:3]:
	print ("The first three items in the list are: "+s)
slice1 = slice(1,4,1)
for sss in ss[slice1]:
	print ("Three items from the middle of the list are "+sss)
slice2 = slice(-1,1,-1)
for ssss in ss[slice2]:
	print("The last three items from the end of the list are: "+ssss)