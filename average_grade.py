sum_=0
i=0
grade=0
while grade>=0  :
    grade=int(input("Enter the grade of student: "))
    sum_=sum_+grade
    i=i+1

avg=sum_/i
print(avg)
