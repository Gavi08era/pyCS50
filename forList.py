students=['Harry', 'Hermonine', 'Ron']
j=len(students)
print(j)
for i in range(len(students)):
    if i==j-1:
         print(i, students[i], end=".")
    else:
        print(i, students[i], end=", ")
