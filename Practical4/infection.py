n=91 #the total number of students is 91
m=int(input('The total number of students is 91. Please input the initial number of infected students:')) #get the initial number of infected students
s=float(input('Please input the growing rate of infection:')) #get the growing rate of infection
d=0 #initialise day number
#calculate the number of infected students each day
while m<n:
    m=m+m*s #add newly infected students to the total infected students
    d+=1
    print('The number of infected students on day',d,'is',m)
print('It takes',d,'days for all students to be infected.')