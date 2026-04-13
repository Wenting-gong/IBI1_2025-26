#store the populations as variables
a=5.08 #the population in 2004 is 5.08 million
b=5.33 #the population in 2014 is 5.33 million
c=5.55 #the population in 2024 is 5.55 million

#calculate the growing population
d=b-a #calculate the growing population between 2004 and 2014
print('d=',d)
e=c-b #calculate the growing population between 2014 and 2024
print('e=',e)

#compare the differences
if d>e:
    print('The population growth decelerates.')
else:
    print('The population growth accelerates.')
#The result:The population growth decelerates.

#create X and Y
list=[[True,False],[False,True],[True,True],[False,False]]
for i in list: 
    X=i[0]
    Y=i[1]
    W=X or Y
    print(f'X:{X},Y:{Y},W:{W}')
#The result: 
X:True,Y:False,W:True
X:False,Y:True,W:True
X:True,Y:True,W:True
X:False,Y:False,W:False
