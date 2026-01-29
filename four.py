todo_list = []

while True:
    task = input("Enter a task (or type 'done' to quit): ")
    if task.lower() == 'done':
        break
    todo_list.append(task)

print("\nYour To-Do List:")
for index, item in enumerate(todo_list, 1):
    print(f"{index}. {item}")