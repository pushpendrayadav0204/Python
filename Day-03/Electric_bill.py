X = int(input("Enter unit of last month: "))
Y = int(input("Enter unit of current month: "))
total_unit=X+Y
if total_unit>= 0 and total_unit <= 100:
    print("Bill amount: ",total_unit*2)
elif total_unit>= 101 and total_unit <= 200:
    print("Bill amount: ",total_unit*3)
elif total_unit>= 201 and total_unit <= 300:
    print("Bill amount: ",total_unit*4)
elif total_unit >= 301 :
    print("Bill amount: ",total_unit*5)