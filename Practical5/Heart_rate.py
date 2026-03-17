#create the list of heart rates
heart_rates=[72,60,126,85,90,59,76,131,88,121,64]

#calculate the mean value and report it and the number of patients
total=0
for i in heart_rates:
    total+=i
mean=total/len(heart_rates)
print('There are',len(heart_rates),'patients in the dataset and the mean value of their heart rates is',mean)

#Count the number of patients in each category
Low=0
Normal=0
High=0
for rate in heart_rates:
    if rate<60:
        Low+=1
    elif rate>120:
        High+=1
    else:
        Normal+=1
cate=[Low,Normal,High]
print('The number of heart rate measurements in Low, Normal and High is',cate,'respectively.')

#Compare and print the largest
if Low>Normal and Low>High:
    print('Low contains the largest number of patients.')
elif Normal>Low and Normal>High:
    print('Normal contains the largest number of patients.')
else:
    print('High contains the largest number of patients.')

#draw the pie chart
import matplotlib.pyplot as plt
labels='Low','Normal','High'
sizes=cate
explode=(0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.title('heart rate categories')
plt.axis('equal')
plt.show()