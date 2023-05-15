
#function to compute the area of polygos
import math
def area(n, side):
    area_=(n*side**2)/(4*math.tan(math.pi/n))
    return area_

def main():
    num_side=int(input("Enter the number of sides: "))
    side=float(input("Enter the side: "))
    area_=area(num_side,side)
    print("The area of the polygos is: ",area_)
main()