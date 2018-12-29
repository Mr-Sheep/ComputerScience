guest = ['Joy','Linda','Lily']

guest.insert( 0 ,'Alex')#在list中的第一个添加Alex
guest.insert( 2 ,'Boron')#在list中第三个添加
guest.append('Carbon')#在list最后一个加
print('Dear '+ guest[0]+', could you please go to my party? The place that we will meet is Joy')
print('Dear '+ guest[1]+', could you please go to my party? The place that we will meet is Joy')
print('Dear '+ guest[2]+', could you please go to my party? The place that we will meet is Joy')
print('Dear '+ guest[3]+', could you please go to my party? The place that we will meet is Joy')
print('Dear '+ guest[4]+', could you please go to my party? The place that we will meet is Joy')
print('Dear '+ guest[5]+', could you please go to my party? The place that we will meet is Joy')
print("I'm sorry about there are only 2 peopel can go to my party.")

kick = guest.pop()#删除guest中的第一项（。 如果用 guest.pop(0)也是第一项，用 pop(1)是删除第二项）
print ('Sorry '+ kick)

kick = guest.pop()
print ('Sorry '+ kick)

kick = guest.pop()
print ('Sorry '+ kick)

kick = guest.pop()
print ('Sorry '+ kick)

print('Dear '+ guest[0]+', could you please go to my party? The place that we will meet is Joy')
print('Dear '+ guest[1]+', could you please go to my party? The place that we will meet is Joy')

del guest[0:]#删掉guest中从第一项到最后一项
#del guest[0]就是删除第一项
#del guest[0:2]就是删除1～3项
print (guest)