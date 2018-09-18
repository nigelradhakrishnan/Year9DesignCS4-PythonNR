#This file will go through the basics of
#String manipulation

#Strings are collections of characters
#Strings are enclosed in "" or ''
#"Nigel"
#"Nigel is cool"
#"Nigel is cool!"
#Two things we need to think about
#When we talk about strings
#index - Always starts at 0
#length

#Example
#  01234	"012345"
# "Nigel"	"Monkey"
# len("Nigel") = 5
# len("Monkey") = 6

name = "Nigel"

print(name) #I can print strings

sentence = name + " is cool!" #concatination is adding strings
print(sentence)
print(sentence + "!")

#I can access specific letters
fLetter = name [0] #name at 0
print(fLetter)
letters1 = name [0:2] #inclusive:exclusive
print(letters1)
letters2 = name[2:]
print(letters2)
letters3 = name[:2]
print(letters3)

lname = len(name) #length of string
print(lname)

#if I want to print out all letters
for i in range (len(name)):
	print(name[i])