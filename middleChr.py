
#get string from user
string=input("enter string: ")

a=len(string)

middle=""

if a%2==0:

    middle=string[a//2] + string[(a//2)-1]
else:
    
    middle=string[a//2]
print("middle char is: ",middle)
