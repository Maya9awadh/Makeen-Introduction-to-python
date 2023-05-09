#program to calculate the total surfac volume and area o cylinder
import math

hieght_of_cylinder=4
radius_of_cylinder=6


area=2*math.pi*radius_of_cylinder**2 + 2*math.pi*radius_of_cylinder*hieght_of_cylinder

volume_of_surface=math.pi*radius_of_cylinder**2*hieght_of_cylinder

print("Volume is: %.2f" % volume_of_surface)
print("Surface area is: %.2f" % area)