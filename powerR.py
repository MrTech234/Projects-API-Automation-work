while True:
	print("\n Welcome to Ebuka's To-do list ")
	print("A. Add a task: ")
	print("B. view tasks: ")
	print("C. mark task as done (remove) ")
	print("D. Exit ")
	option = input("Choose an option(A/B/C/D): ").upper()
	if option == "A":
		task = ("Enter new task: ")
		with open("task.txt", "a") as f:
			f.write(task + "\n")
		print("Task added ")
	elif option == "B":
		try:
			with open("task.txt", "r") as f:
				lines = f.readlines()
			if not lines:
				print("No task yet")
			else:
				print("\n your Tasks: ")
				for i, line in enumerate(lines, 1):
					print(f"{i} . {line . strip()}")
		except FileNotFoundError:
			print("No task file yet. Add a task first please :")
	elif option == "C":
		try:
			with open("task.txt" "r") as f:
				lines = f.readlines()
			for i, line in enumerate (lines, 1):
				print(f"{i} . {line.strip()}")
			num = int(input("Enter task number to remove: "))
			if 1< num < len(lines):
				removed = lens.pop(num-1)
				with open("tasks.txt", "w") as f:
					f.writelines(lines)
				print(f"Task removed: {removed.strip()}")
			else:
				print("Invalid task number.")
		except(ValueError, FileNotFoundError):
			print("Something went wro g. Try again.")
	elif option == "D":
		print("Goodbye!")
		break
	else:
		print("Invalid choice, try again motherfucker! ")

