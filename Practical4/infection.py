n=91 #the total number of students
m=int(input('The total number of students is 91. Please input the initial number of infected students:')) #the initial number of infected students
s=float(input('Please input the growing rate of infection:')) #The growing rate of infection
d=0 #day number
#calculate the nomber of infected students each day
while m<n:
    m=m+m*s
    d+=1
    print('The number of infected students on day',d,'is',m)
print('It takes',d,'days for all students to be infected.')