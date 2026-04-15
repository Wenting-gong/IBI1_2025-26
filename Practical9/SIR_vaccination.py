#import neccessary libraries
import numpy as np
import matplotlib.pyplot as plt

#initialize variables
N=10000 #total number
beta=0.3 #probability of infection during contact
gamma=0.05 #probability of recovery

vaccination_rates=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
infected_list=[]

for rate in vaccination_rates:
    v=int(N*rate)
    s=N-v-1
    i=1
    r=0
    history=[[s,i,r,v]]

#loop for 1000 times
    for t in range(1000):
        alpha=beta*max(i,0)/(N-v) if N>v else 0 #calculate the probability of infection
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
        r=N-i-s-v
        history.append([s,i,r,v])
    history=np.array(history)
    infected_list.append(history[:,1])
#draw the plot
plt.figure(figsize=(10,6))
colors=["#45049f","#5848ed","#5f70ce","#00ACC1","#15A69A","#4CAF50","#8BC34A","#CDDC39","#FBE51D","#EBCC71","#ffdfae"]
for j in range(len(vaccination_rates)):
    rate=vaccination_rates[j]
    i_history=infected_list[j]
    color=colors[j]
    plt.plot(i_history,label=f'{int(rate*100)}%',color=color,linewidth=1.5)
plt.title('SIR model with different vaccination rates')
plt.xlabel('time')
plt.ylabel('number of people')
plt.xticks(np.arange(0,1001,200))
plt.yticks(np.arange(0,5001,1000))
plt.legend()
plt.show()