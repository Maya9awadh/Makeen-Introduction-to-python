l=[[0]*4 for i in range(4)]
for i in range(4):
    for j in range(4):
        if(i==j):
            l[i][j]=1
          
        elif(i>j):
            l[i][j]=2
     
for i in range(4):
    for j in range(4):
        print(l[i][j],end=' ')
    print()

print()
l1=[[0]*4 for i in range(4)]
for i in range(4):
    for j in range(4):
        if(i==j):
            l1[i][j]=1
        elif((i-j==2)):
            l1[i][j]=1
        elif((j-i==2)):
            l1[i][j]=1
for i in range(4):
    for j in range(4):
        print(l1[i][j],end=' ')
    print()