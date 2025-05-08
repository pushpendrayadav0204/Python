import sys 
X= int,list[(input("Enter elements= "))]
max = 0
min = sys.maxsize
for i in X:
    if X[i] < min :
        min = X[i]
    if X[i] > max :
        max = X[i]

print(max,min)