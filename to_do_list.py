tasks = []

# function for adding tasks 
def add_task():
    getting_task =input("add a task: ")
    tasks.append(getting_task.lower)
    print("task added successfully")
#function for removing tasks
def remove_task():
    removeing_task = input("type task you want to remove: ")
    if removeing_task not in tasks: 
        print("this task does not exist")
    else:
         print("task removed successfully")
         tasks.remove(removeing_task.lower)       
#function for listing  tasks
def list_task():
    if  not tasks  :
        print("tasks list is empty")
    else:
        print(tasks)

#main program
print("it is to do list program")
print("choose what you want to do")
print('''if you want to 
      add task type:1
      remove task type:2
      list all task type:3''')
while True:
    user_input = int(input("choose what you want to do: "))
    if user_input == 1:
        add_task()
    elif user_input == 2:
        remove_task()
    elif user_input == 3:
        list_task()
    else:
        print("this is invalid input")