x=[[1,2,3],[3,4,5]]
for i in range(2):
    for j in range(3):
        print(x[i][j],end='')
    print()
print([[0]*3]*4)

f=[[0]*3 for i in range(4)]
print(f)

l=[[i]*3 for i in range(1,4)]
print(l)

for i in range(3):
    for j in range(3):
        print(l[i][j],end='  ')
    print()

