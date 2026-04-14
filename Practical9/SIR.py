#import neccessary libraries
import numpy as np
import matplotlib.pyplot as plt

#initialize variables
N=10000 #total number
s=9999 #susceptible
i=1 #infected
r=0 #recoverd
beta=0.3 #probability of infection during contact
gamma=0.05 #probability of recovery
history=[[s,i,r]]

#loop for 1000 times
#calculate the probability of infection using the proportion of infected people in the population
#randomly make susceptible people contact with others and calculate newly infection number
#calculate newly recovery number
#calculate total susceptible and infected number
#make sure all numbers are not negative
#add new numbers to the list
for t in range(1000):
    alpha=beta*max(i,0)/N #calculate the probability of infection
    if s>0:
        infected_array=np.random.choice(range(2),size=s,p=[1-alpha,alpha])
        new_infected=np.sum(infected_array)
    else:
        new_infected=0
    if i>0:
        recovered_array=np.random.choice(range(2),size=i,p=[1-gamma,gamma])
        new_recovered=np.sum(recovered_array)
    else:
        new_recovered=0
    s=max(s-new_infected,0)
    i=max(i-new_recovered+new_infected,0)
    r=N-i-s
    history.append([s,i,r])
history=np.array(history)
print(history)

#draw the plot
s_list=history[:,0]
i_list=history[:,1]
r_list=history[:,2]
plt.title('SIR model')
plt.xlabel('time')
plt.ylabel('number of people')
x_ticks=np.arange(0,1001,200)
y_ticks=np.arange(0,10001,2000)
plt.plot(s_list,label='susceptible')
plt.plot(i_list,label='infected')
plt.plot(r_list,label='recovered')
plt.legend()
plt.show()