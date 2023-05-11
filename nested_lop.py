msq=input("Enter decrypted message: " )

originl=''
for i in msq:
    d=ord(i)
    h=d-3
    originl=originl+chr(h)
print(originl)

divisor=0
for i in range(1,101):
    divisor=0
    for j in range(1,i):
        if i%j==0:
            divisor=divisor+j
    if divisor==i:
        print(i)