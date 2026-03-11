#store the variables
a=5.08 #the population in 2004 is 5.08 million
b=5.33 #the population in 2014 is 5.33 million
c=5.55 #the population in 2024 is 5.55 million
#calculate the growing population between 2004 and 2014
d=b-a
print('d=',d)
#calculate the growing population between 2014 and 2024
e=c-b
print('e=',e)
#compare the differences
if d>e:
    print('The population growth decelerates.')
else:
    print('The population growth accelerates.')
#The result:The population growth decelerates.

#create X and Y
X=True
Y=False
#get W
W=X or Y
print('W=',W)
#The result: W= True
