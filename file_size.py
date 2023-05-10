#enter the number of file
num_file=int(input("Enter the number of files:" ))

#enter the size o each file
size_of_each_file=int(input("Enter the size of each file: "))

#enter memory size
memory=int(input("Enter memory size: "))

#set the required memory
required_memory=num_file*size_of_each_file

if required_memory <=memory:
    print("yes")  
else:
    print("No")
