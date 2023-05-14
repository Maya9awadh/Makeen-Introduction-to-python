string=input("Enter string: ")

valid= len(string)>=8

position=0

while valid and position<len(string):
    
    valid=((string[position].isupper()) or (string[position].islower()) or (string[position].isdigit())
           or (string[position] == '@' or '$' or '#'))
    position=position+1

if valid :
    print("The string is valid")
else:
    print("The string is not valid")