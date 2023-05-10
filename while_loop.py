#print the first 10 even number
num=0
while num<20:
    if(num%2==0):
        print(num)
    num=num+1
print("\n")

#print the first 10 number with their squares
count=0
while count<10:
    print(count," ",count**2)
    count=count+1
print("\n")

#display the sequene 105,98,91....7
n=105
while n>=7:
    print(n)
    n=n-7
print("\n")

#display acsii character of word hello
string='Hello'
i=0
while i< len(string):
    print(ord(string[i]))
    i=i+1

#disply the factor of 10
print("\n")
num=1
while num<=10:
    if 10%num==0:
        print(num)
    num=num+1