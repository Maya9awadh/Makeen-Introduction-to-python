#define a list
prime=[22,3,-2,-1,10,1]

#print all elements of list separated by space
for i in prime:
    print()
    print(i)
    
print()

#print the product of elements
p=1
for i in prime:
    p=p*i
print("The produt of elements is: ",p)
print()

#count the negative number in the list
count=0
for i in prime:
    if i<0:
        count=count+1
print("There are ",count,"negative elements")
