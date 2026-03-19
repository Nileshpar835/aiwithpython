import os

#file to store task

FILE_NAME="C:\\Users\\phulc\\PycharmProjects\\PythonProject\\AIwithPyhton\\tasks.txt"


#loadd task from file

def load_tasks():
    tasks={}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,'r') as f:
            for line in f:
                task_id,title,status=line.split(" | ")
                tasks[int(task_id)]={"title":title,"status":status}
    return tasks

#save task to file
def savetasks(tasks):
    with open(FILE_NAME,'w') as f:
        for task_id,task in tasks.items():
            f.write(f"{task_id} |{task['title']}|{task['status']}\n")
#add new task

def addtask(tasks):
    title=input("Enter task title: ")
    task_id=max(tasks.keys(),default=0)+1
    tasks[task_id]={"title":title,"status":"incomplate"}
    print(f"Task {task_id} added to {title}")


def viewtask(tasks):
    if not tasks:
        print("No task found")
    else:
        for task_id,task in tasks.items():
            print(f"Task {task_id} {task['title']} status: {task['status']}")

def marktaskcomplate(tasks):
    task_id=int(input("Enter task id to mark as complate: "))
    if task_id in tasks:
          tasks[task_id]["status"] = "complate"
          print(f"Task {task_id} marked as complate")
    else:
        print("task id not found")

def deletetask(tasks):
    task_id=int(input("Enter task id to delete: "))
    if task_id in tasks:
        deletetask=tasks.pop(task_id)
        print(f"Task {task_id} deleted from {deletetask['title']}")
    else:
        print("task id not found")

def mainmenu():

    tasks=load_tasks()
    while True:
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as complate")
        print("4. Delete task")
        print("5. Exit")

        choice=int(input("Enter choice: "))
        if choice==1:
            addtask(tasks)
        elif choice==2:
            viewtask(tasks)
        elif choice==3:
            marktaskcomplate(tasks)
        elif choice==4:
            deletetask(tasks)
        elif choice==5:
            print("Thank you for using AI with Pyhton")
            break
        else:
            print("Invalid choice")

if __name__=="__main__":
    mainmenu()