#store the name of countries in a list
coun=['UK','China','Italy','Beazil','USA']

#create populations in arrays and calculate the percentage change
import numpy as np
pop_2020=np.array([66.7,1426.0,59.4,208.6,331.6])
pop_2024=np.array([69.2,1410.0,58.9,212.0,340.1])
change=(pop_2024-pop_2020)/pop_2020*100
print('The percentage changes of population for',coun,'are',change)

#change the array into list
change=change.tolist()

#store the percentage change and its country in a dictionary
dict={}
for i in range(len(change)):
    dict[change[i]]=coun[i]

#sort the percentage change list from the largest to the smallest
sorted_change=sorted(change)
sorted_change.reverse()
print('Here is the sorted value: ',sorted_change)

#use the dictionary to find the country name by value and print the message
print(dict[sorted_change[0]],'has the largest population increase of',sorted_change[0],dict[sorted_change[4]],'has the largest decrease of',sorted_change[4])

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