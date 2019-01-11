ss = ['Chengdu','Chicago','New York','Berlin','Paris']
for s in ss[:3]:
	print ("The first three items in the list are: "+s)
for sss in ss[slice(1,4,1)]:
	print ("Three items from the middle of the list are "+sss)
for ssss in ss[slice(-1,1,-1)]:
	print("The last three items from the end of the list are: "+ssss)