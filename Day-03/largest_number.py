X= input("Enter 4 dgit number: ")
if X[-1]>X[-2] and X[-1]>X[-3] and X[-1]>X[-4]:
    print(X[-1],"Is a largest number.")
elif X[-2]>X[-1] and X[-2]>X[-3] and X[-2]>X[-4]:
    print(X[-2],"Is a largest number.")
elif X[-3]>X[-1] and X[-3]>X[-2] and X[-3]>X[-4]:
    print(X[-3],"Is a largest number.")
else:
    print(X[-4],"Is a largest number.")