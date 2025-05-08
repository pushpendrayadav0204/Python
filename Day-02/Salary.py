basic_Salry = int(input("Enter Your Basic Salary : "))
travel_allowance = (10/100)*basic_Salry
pf = (7.8/100)*basic_Salry
da = 500
gross_salary = basic_Salry+travel_allowance+da
Net_Salary = gross_salary-pf
print("Your Gross Salary is : ",gross_salary)
print("Your Net Salary is : ",Net_Salary)