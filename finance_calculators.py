import math



input_calculator = input("investment: to calculate the amount you'll earn from your investment \nbond: to calculate the amount you'll have to pay on a home loan \n\nEnter either 'investment' or 'bond' from the menu to proceed: ")



if(input_calculator.lower() == "investment"):
    P = int(input("How much money are you depositing?: ")) 
    r = float(input("Please enter inerest rate as a numerical value without the '%': ")) 
    t = int(input("Please specify the length of your investment in years: "))
    interest_type = input("Please pick either simple or compound interest: ") 

    if(interest_type.lower() == "simple"):
        simple_interest = P*(1 + (r/100)*t) 
        print(simple_interest) 

    elif(interest_type.lower() == "compound"): 
        compound_interest = P*math.pow((1+(r/100)),t) 
        print(compound_interest)  

elif(input_calculator.lower() == "bond"):
    V = int(input("Please state the current value of the property: "))
    i = float(input("What is the interest rate?: "))
    n = int(input("Please state the repayment length in months: ")) 

    i = (i / 100) / 12.0
    bond_repayment = (i * V) / (1-(1 + i) ** (-n)) 
    print(bond_repayment)

 

