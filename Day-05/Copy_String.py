X=str(input("Enter your String: "))
def copy(X):
    Y=""
    for i in range(0,len(X),1):
        Y+=X[i]
    print("Copied String: ",Y)
copy(X)
