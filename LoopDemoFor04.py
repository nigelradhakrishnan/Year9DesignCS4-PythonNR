print("****************************")
print("Coutned Loops: For")

print("0")
print("1")
print("2")
print("3")

#When we think of a loop I want you to think about
#Count: the variable that holds the current count
#Check: The check that is done each time the loop runs 
#Change: The change applied to the count eac time the loop runs

#for <count var> in range (<initial value>, <chack value>, <change>)
for i in range(0,4,1):
	print(i)

print("******************")
for i in range(-44,137,1):
	print(i)

	if (i % 2 == 0):
		print(str(i)+" is even")
		print(str(i)+" is odd")