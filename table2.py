row=int(input("Enter the number of row: "))
column=int(input("Enter the number of colomun: "))

l=[[0]*column for i in range(row)]

for i in range(row):
    for j in range(column):
        l[i][j]=int(input("Enter the value: "))
 
for i in range(row):
    for j in range(column):
        print(l[i][j],end=' ')
    print()