
#function to get the sum of integer digits
def sum_digits(n):
    h=str(n)
    sum_=0
    for i in h:
        sum_=sum_+int(i)
    return sum_

number=int(input("Enter a number: "))
print()
print("the sum of numbers is",sum_digits(number))