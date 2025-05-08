
x = input()

s = int(x[0])**3
s += int(x[1])**3
s += int(x[2])**3

if int(x) == s :
    print(s ,"This is Armstrong number ")
else :
    print( s ,"This is not Armstrong number ")