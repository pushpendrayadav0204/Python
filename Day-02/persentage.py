marks= []
total  = 0 
for i in range (0,5):
    marks.append(int(input(f"Enter {i+1} subject marks: ")))
    total += marks[i]
print("your marks is: ",marks)
print("Total marks is: ",total)
percentage = (total*100)/500 
print("Your percentage is: ",percentage,"%")
