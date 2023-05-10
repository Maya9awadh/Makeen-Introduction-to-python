"""
Program to calculate the temperature in celisius and
fahrenhait
"""
#ask the user to enter temperature
temp=float(input("Enter temp: "))

#ask the user to choose C or F
unit=input("Enter temperature unit 'C' or 'F': ")

if unit=='C':
    #Calculate the temperature in fahrenheit
    temp_F=32+(1.8*temp)
    print("The temparatue in fahrenheit is: %.2f F" % temp_F)
    
elif unit=='F':
    #calculte the temperature in celsius
    temp_C=(temp-32)/1.8
    print("The temparatue in celsius is: %.2f C" % temp_C)