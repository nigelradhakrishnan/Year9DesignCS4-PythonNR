#This program will show how to effectively use substring
#Prompt th User for their first name and their last name

#Input
fName = input("What is you first name: ")
lName = input("What is your last name: ")

#Process
result = fName[2:4] + "." + lName[5:9]
lenlName = len(lName)
#Output
print("Hi "+result)