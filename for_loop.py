v="virgina"
for i in v :
    print(i,end=' ')
print("\n")


r=int(input("Enter range: "))
sum_=0

for i in range(r):
    num=int(input("Enter number: "))
    sum_=sum_+num

avg=sum_/r
print("average is ",avg)