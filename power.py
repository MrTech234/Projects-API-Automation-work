while True:
	print("\n welcome to Ebuka to fo list")
	menu = input("Add a task: ")
	menu = input("View tasks: ")
	menu = input("Mark task as done: ")
	menu = input("Exit")
	options = input("A,B,C,D")
	if options == "A":
		with open("tasks.txt", "a") as f:
	elif options == "B":
		with open("tasks.txt", "r") as f:
		lines = f.readlines()
		for i, lines in enumerate (lines,1):
			print(f"{i}.{line.strip()}")
	elif options == "C":
		print("pick a task number: ")
		if task number = "1,20":
			print("DONE")
	else:
		print("Invalid option, try again")
		continue
	else:
		print("Goodbye")
		break
