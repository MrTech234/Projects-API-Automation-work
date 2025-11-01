while True:
	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter Second number: "))
	operation = input("Enter operation, /: ")
	if operation == "/":
		if num2 != 0:
			result = num1 / num2
		else:
			result = "Error! Division by zero! "
		print("Result", result)
		choice = input("Do you wish to continue? (yes/no): ")
		if choice.lower() == "no":
			print("Goodbye! ")
			break

