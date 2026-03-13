#input age and check if it is valid
#if not, print reminding message
#if so, input weight and check if it is valid
#the same checking method as the age for weight
#same for creatine concentration
#input gender and check if it is valid
#calculate CrCl for male and female with different formular

a=int(input('How old are you:')) #store age
#check if age is valid
if a>=100 or a<0: 
    print("Please input valid age:")
else:
    w=float(input('Please input your weight in kg:')) #store weight
    #check if weight is valid
    if w<=20 or w>=80:
        print("Please input valid weight.")
    else:
        c=float(input("Please input your creatine concentration in μmol/l:")) #store creatine concentration
        #check if creatine concentration is valid
        if c<=0 or c>=100:
            print("Please input valid creatine concentration.") 
        else:
            g=str(input("Please input your gender(male or female):")) #store gender
            #check if gender is valid, and if so, give the CrCl value by gender
            if g=='male':
                CrCl=(140-a)*w/(72*c)
                print("Your CrCl is",CrCl)
            elif g=='female':
                CrCl=(140-a)*w*0.85/(72*c) #female's CrCl needs to multiply 0.85
                print("Your CrCl is",CrCl)
            else:
                print("Please input a valid gender.")