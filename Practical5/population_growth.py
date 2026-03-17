#create the arrays and calculate the percentage change of population 
import numpy as np
pop_2020=np.array([66.7,1426.0,59.4,208.6,331.6])
pop_2024=np.array([69.2,1410.0,58.9,212.0,340.1])
change=(pop_2024-pop_2020)/pop_2020*100
print(change)

#change the array into list and sort it
change=change.tolist()
dict={}
coun=['UK','China','Italy','Beazil','USA']
for i in range(len(change)):
    dict[change[i]]=coun[i]
sorted_change=sorted(change)
sorted_change.reverse()
print(sorted_change)
#Result:[3.7481259370314843, 2.5633293124246075, 1.629913710450626, -0.8417508417508417, -1.1220196353436185]
print(dict[change[0]],'has the largest population increase of',change[0],dict[change[-1]],'has the largest decrease of',change[-1])

#draw the bar chart
import matplotlib.pyplot as plt
N=len(change)
population_change=change
ind=np.arange(N)
width=0.35
p1=plt.bar(ind,population_change,width)
plt.ylabel('population change')
plt.title('Percentage change of population in different countries')
plt.xticks(ind,('UK','China','Italy','Brazil','USA'))
plt.yticks=(np.arange(-1.5,4.0,0.5))
plt.axhline(0,color='black',linewidth=0.8)
plt.show()