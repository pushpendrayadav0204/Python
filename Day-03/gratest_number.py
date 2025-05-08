x = input()

if (x[0] > x[1] and x[0] > x[-1]) :
    print(x[0] ,'is the greatest number ')
elif (x[1] > x[-1] and x[1] > x[0]) : 
    print(x[1] , 'is the greatest number ')
else :
    print(x[-1] , 'is the greatest number ')