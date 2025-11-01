While True:
	print("\n Welcome to Ebuka's to do list ")
	menu A = input("Add Task")
	menu B = input("View Task")
	menu C = input("Mark task as done")
	menu D = input("Exit")
	options = input("A,B,C,D")
	if options == "A":
		with open("tasks.txt", "a") as f:
	elif options == "B":
		with open("tasks.txt", "r") as f:
		lines = f.readlines()
		for i, limes in enumerate (lines, 1):
			print(f"{i} . {line.strip()}")
	elif option == "C":
		print("pick a task number: ")
		if task number = "1,20":
			print("Done")
	else:
		print("invalid option, try again")
		continue
	else:
		print("Goodbye")
		break
