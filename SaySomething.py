import os

#Loop structure
#Two types of loops
#Counted loops: We know in advance how many times something should run for loops
#Conditional loops: We dont know how many times something will run before entering the loop while loops

while (True):
	statement = input("What would you like me to say: ")
	os.system("say "+statement)