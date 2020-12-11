#Check if a Number is Positive, Negative or 0

#using If else if Method

num = float(input("Enter a number: "))
if num > 0:
	print("Positive number")
elif num == 0:
	print("Zero")
else:
	print("Negative number")
	


#using Nested IF method.
num = float(input("Enter a number: "))
if num >= 0:
	if num == 0:
		print("Zero")
	else:
		print("Positive number")
else:
	print("Negative number")