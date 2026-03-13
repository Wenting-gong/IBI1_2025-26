#let user input all the variables and store them
#check if the variables are all valid, if not, print the reminding message
#calculate CrCl for male and female with different formular and print that out

#store all the variables
a=int(input('How old are you:')) #store age
w=float(input('Please input your weight in kg:')) #store weight
c=float(input("Please input your creatine concentration in μmol/l:")) #store creatine concentration
g=str(input("Please input your gender(male or female):")) #store gender

#check if all the variables are valid
if a>=100 or a<0:  #for age
    print("The age should be within 0~100!")
if w<=20 or w>=80: #for weight
    print("The weight should be within 20~80 kg!")
if c<=0 or c>=100: #for creatine concentration
    print("The creatine concentration should be within 0~100 μmol/l.") 
#check if gender is valid, and if so, give the CrCl value by gender
if g=='male':
    CrCl=(140-a)*w/(72*c)
    print("Your CrCl is",CrCl)
elif g=='female':
    CrCl=(140-a)*w*0.85/(72*c) #female's CrCl needs to multiply 0.85
    print("Your CrCl is",CrCl)
else:
    print("Please input a valid gender.")