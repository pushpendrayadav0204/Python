data = (input("Enter three digit number: "))
reverse=data[-1]+data[-2]+data[-3]
print(reverse)
new_data=int(reverse)
# f=new_data//100
# new_data%=100
# s=new_data//10
# new_data%=10
# t=new_data

f=int(reverse[0])
s = int(reverse[1])
t = int(reverse[2])
print(f+s+t)
data=10j
print(type(data))