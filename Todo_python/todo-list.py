print "Welcome to the TODO task management program."

todo_dict = {}

while True:
    task = raw_input("Please enter a TODO task: ")
    status = raw_input("Was the task completed yet? (yes/no) ")
    print "Your task is: " + task

    if status == "yes":
        todo_dict[task] = True  # this is how we add a key-value pair into a dict
    else:
        todo_dict[task] = False

    new = raw_input("Would you like to enter new task? (yes/no) ")

    if new == "no":
        break

with open("todo.txt", "w+") as todo_file:
    print "Completed tasks:"  # open the TXT file (or create a new one)

    todo_file.write("Completed tasks:\n")  # write into the TXT file
    for item in todo_dict:
        if todo_dict[item] == True:
            print "- " + item
            todo_file.write("- " + item + "\n")  # add task into the TXT file

    todo_file.write("\n")

    print "Incomplete tasks:"
    todo_file.write("Incomplete tasks:\n")  # write into the TXT file
    for item in todo_dict:
        if todo_dict[item] == False:
            print "- " + item
            todo_file.write("- " + item + "\n")  # add task into the TXT file

    todo_file.close()  # close the TXT file

print "All tasks: %s" % todo_dict

print "END"


