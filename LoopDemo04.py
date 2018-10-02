#Aloop is a programming structure that can repeat a section of code
#A loop can run the same code exactly over and over or
#with some thought it can generate a pattern

#There are two broad categories of loops
# Conditional looops: These loop as long as a condition is true

# Counted loops (for): These loops use a counter to keep track of how many the loop has run


#You can use any loop in any situation, but ussually from a design
#perspective there is a better loop in terms of coding.

#If you know how in advance how many times a loop should run a COUNTED LOOP 
#is usually a better choice

#If you dont know how many times a loop should run a CONDITIONAL LOOP
#is usually the better choice

print("***********************************")
#Taking Inputs

word = "" #We have to declare and initialize word so it fails the while loop
#a while loop evaluates a condition when it is first reached
#If the condition is true it enters the loop block
while len(word) < 6 or word.isalpha() == False:
	#Loop block
	word = input("Please input a word larger than five letters: ")
	print(word.isalpha())
	if (len(word) < 6):
		print("BudSki, I said more than five letters")

	if(word.isalpha() == False):
		print("Dude, I said a real word!!!")
	#When we reach the bottom of the loop block we check the condition
	#again. If it is true, we go back to the top of the block and run
	#it again


print(word+" is a seriously long word!")