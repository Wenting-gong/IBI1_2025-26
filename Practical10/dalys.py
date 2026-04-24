#import neccessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read csv file and fetch information
dalys_data=pd.read_csv('dalys-rate-from-all-causes.csv')

#check specific value (showing the third and fourth columns for the first 10 rows)
record=dalys_data.iloc[0:10,2:4]
print(record)
print(record.describe()) 
#Result: 1998 reported the maximum DALYs in the first 10 years in Afghanistan

#get years in Zimbabwe
my_rows=[]
for i in range(len(dalys_data)):
    if dalys_data.iloc[i,0]=='Zimbabwe':
        flag=True
    else:
        flag=False
    my_rows.append(flag)
Zimbabwe_year=dalys_data.loc[my_rows,'Year']
print(Zimbabwe_year)
first_year=Zimbabwe_year.min()
last_year=Zimbabwe_year.max()
print(f"The first year is {first_year}, the last year is {last_year}")
#Result: first year is 1990, last year is 2019

#Recent year situations across countries
recent_data=dalys_data.loc[dalys_data.Year==2019,['Entity','DALYs']]
print(recent_data.info())
max_country=recent_data.loc[recent_data['DALYs'].idxmax()]
min_country=recent_data.loc[recent_data['DALYs'].idxmin()]
print(f'country with thelargest DALYs is {max_country.Entity}\ncountry with the smallest DALYs is {min_country.Entity}')
#Result:country with thelargest DALYs is Lesotho, country with the smallest DALYs is Singapore

#Create a plot to show the DALYs change over time in the maximum country
record=dalys_data.loc[dalys_data.Entity==max_country.Entity,['Year','DALYs']]
plt.plot(record.Year,record.DALYs,'g+')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs over time in the country with the largest DAYLs in 2019')
plt.xticks(record.Year,rotation=-90)
plt.show()

#check for year range and DALYs in China and UK
china=dalys_data.loc[dalys_data.Entity=='China',['Year','DALYs']].rename(columns={'DALYs':'China_DALYs'})
uk=dalys_data.loc[dalys_data.Entity=='United Kingdom',['Year','DALYs']].rename(columns={'DALYs':'UK_DALYs'})

#merge two dataframe together for comparison
compare=pd.merge(china,uk,how='inner',on='Year')

#calculate the differences using pandas
compare['Difference']=compare.China_DALYs-compare.UK_DALYs
print(compare)

#draw a plot
plt.plot(compare.Year,compare.China_DALYs,'r+',label='China_DALYs')
plt.plot(compare.Year,compare.UK_DALYs,'b+',label='UK_DALYs')
plt.plot(compare.Year,compare['Difference'],label='Difference(China-UK)')
plt.legend()
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs Change over Time')
plt.xticks(compare.Year,rotation=90)
plt.show()