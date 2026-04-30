tasks=[]
def add_task():
    name=input('Enter your name:')
    priority=input('Enter priority:(low,medium,high):'.capitalize())
    try:
        time=float(input('Enter time required:'))
        task={
            'Name':name,
            'Priority':priority,
            'Time':time,
            'status':'Pending'
        }
        tasks.append(task)
        print("task added successfully my nigga")
    except ValueError:
        print("inalid input.")
def View_task():
    if not tasks:
        print("Empty Task.")
    else:
        print("-----List of Tasks-----")
        for i,task in enumerate(tasks,1):
            print(f"{i}.| Status:[|{task['status']}] | Name:{task['Name']} | Priority: {task['Priority']} | Time: {task['Time']} hrs")
def Marks_completed():
    View_task()
    if not tasks:
        return
    try:
        choice=int(input("select task number to mark as completed:"))
        if 1<= choice <= len(tasks):
            tasks[choice-1]["status"]="Completed"
            print('task updated.')
        else:
            print("invalid task number.")
    except ValueError:
        print("please enter a valid number.")
def analyse_task():
    if not tasks:
        print("nothing to analyse.")
        return
    total_task=len(tasks)
    total_time=sum(task['Time'] for task in tasks)
    high_priority=[t['Name'] for t in tasks if t['Priority']=="high"]
    low_priority=[t['Name'] for t in tasks if t['Priority']=="low"]
    medium_priority=[t['Name'] for t in tasks if t['Priority']=="medium"] 
    long_task=[t['Name'] for t in tasks if t['Time']>3]
    short_task=[t['Name'] for t in tasks if t['Time']<=3]
    completed_count=sum(1 for t in tasks if t['status']=="Completed")
    pending_count=total_task-completed_count
    print("\n---task analysis---")
    print(f"total tasks:{total_task}")
    print(f"High priority tasks:{','.join(high_priority) if high_priority else 'none'}")
    print(f"Low priority tasks:{','.join(low_priority) if low_priority else 'none'}")
    print(f"medium priority tasks:{','.join(medium_priority) if medium_priority else 'none'}")
    print(f"Tasks more than 3 hours:{','.join(long_task) if long_task else 'none'}")
    print(f"Tasks less than 3 hours:{','.join(short_task) if short_task else 'none'}")
    if total_time > 8:
        print('warning.total work exceeds to 8 hours.take a break nigga.')
    else:
        print('Work more niggers,work more!!!!!!!.jezz man work on it.')
    if completed_count > pending_count:
        print("grate job nigga, you completed more tasks.")
def main_menu():
    while True:
        print("\n---- smart intership task manager----")
        print("1.Add task")
        print("2.View task")
        print("3.Mark completed")
        print("4.Analyse task")
        print("5.exit")
        choices=int(input("Enter your choice:"))
        if choices==1:
            add_task()
        elif choices==2:
            View_task()
        elif choices==3:
            Marks_completed()
        elif choices==4:
            analyse_task()
        elif choices==5:
            print("exiting from the task,Good Bye!.")
            break
        else:
            print("invalid choice.")

def login_system():
    print("Login Page")
    user=input("Username:")
    passw=input("Password:")
    if user=="user1" and passw=="123":
        print("login successfull")
        main_menu()
        return True
    else:
        print("Access Denied")
        return False
login_system()

    