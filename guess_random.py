from random import randint

r=randint(1,100)
print(r)



d=False

while not d:
    num=int(input("guess the number: "))
    if num<1 or num>100:
        print("the number outside the range")
    else:
        if num==r:
            print("great")
            d=True
        elif num>r:
            print("go lower")
        else:
            print("go upper")
        