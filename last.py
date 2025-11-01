while True:
	print("\n Welcome to Ebubu's CLI App ")
	print("\n Menu: ")
	print("A. Add Tasks: ")
	print("B. View Tasks: ")
	print("C. Delete/mark task as done ")
	print("D. Exit ")
	option = input("Choose an option A/B/C/D/E: ").upper()
	if option == "A":
		task= input("Enter a task, and the date it was added: ")
		with open("tasks.txt", "a") as f:
			f.write(task + "\n")
		print("Task added! ")
	elif option == "B":
		try:
			with open("tasks.txt", "r") as f:
				lines = f.readlines()
			if lines:
				print("\n Your Tasks: ")
				for i, lines in enumerate (lines, 1):
					print(f"{i} . {lines . strip()} ")
			else:
				print("No task to show! ")
		except FileNotFoundError:
			print("There are no task yet ")
	elif option == "C":
		try:
			with open("tasks.txt", "r") as f:
				lines = f.readlines()
			for i, line in enumerate (lines, 1):
				print(f"{i} . {line . strip()} ")
			num = int(input("Enter the task to delete: "))
			if 0 < num <= len(lines):
				removed = lines.pop(num - 1)
				with open("tasks.txt", "a") as f:
					f.writelines(lines)
				print(f"tasks removed: {removed . strip()}")
			else:
				print("Invalid task number! ")
		except FileNotFoundError:
				print("Something went wrong, try again later ")
	elif option == "D":
		print("Goodbye bro!!! ")
		break
	else:
		print("Invalid choice, try again! ")

