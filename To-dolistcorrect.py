while True:
	print("\n Welcome to Ebuka's To do list")
	print("A. add a task: ")
	print("B. view tasks: ")
	print("C. mark task as done (remove) ")
	print("D. Exit")
	option = input("Choose an option (A/B/C/D): ").upper()
	if option == "A":
		task = input("Enter new task: ")
		with open("tasks.txt", "a") as f:
			f.write(task + "\n")
		print("Task added! ")
	elif option == "B":
		try:
			with open("tasks.txt", "r") as f:
				lines = f.readlines()
			if not lines:
				print("No tasks yet! ")
			else:
				print("\n Your Tasks: ")
				for i, line in enumerate(lines,1):
					print(f"{i} . {line . strip()} ")
		except FileNotFoundError:
			print("No tasks file yet. Add a task first ")
	elif option == "C":
		try:
			with open("tasks.txt", "r") as f:
				lines = f.readlines()
			for i, line in enumerate(lines,1):
				print(f"{i} . {line.strip()} ")
			num = int(input("Enter task number to remove: "))
			if 1 < num <= len(lines):
				removed = lines. pop(num - 1)
				with open("tasks.txt", "w") as f:
					f.readlines (lines)
				print(f" Task removed: {removed.strip} ")
			else:
				print(" invalid task number")
		except FileNotFound:
			print("Something went erong. Try again ")
	elif option == "D":
		print("Good luck! ")
		break
	else:
		print("invalid choice, try again ")
