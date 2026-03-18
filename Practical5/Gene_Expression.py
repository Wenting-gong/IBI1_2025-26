#create the library
gene={'TP53':12.4, 'EGFR':15.1, 'BRCA1':8.2, 'PTEN':5.3, 'ESR1':10.7}
print('The initial dictionary is ',gene)
gene['MYC']=11.6

#draw the bar chart
import matplotlib.pyplot as plt
import numpy as np
ind=np.arange(len(gene))
width=0.35
p1=plt.bar(ind, gene.values(), width)
plt.ylabel('Expression value')
plt.title('Expression values of genes')
plt.xticks(ind,(gene.keys()))
plt.yticks(np.arange(0,16,8))
plt.show()

#check the expression value of a gene of interest
g=str(input('Please tell me what gene are you interest in:'))
if g in gene:
    g_value=gene[g]
    print('The expression value of',g,'is',g_value)
else:
    print('The gene is not in the library.')

#calculate the mean value of expression values
total=0
for i in gene.values():
    total+=i
mean=total/len(gene)
print('The average of gene expression is',mean)