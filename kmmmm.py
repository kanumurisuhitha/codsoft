#empty list to store tasks
tlist=[]
#function that add tasks
def addtlist(t):
    tlist.append(t)
    print(f"Task'{t}'added!")
def alt():
    if tlist:
        print("To-Do List:")
        for i,t in enumerate(tlist,1):
            print(f"{i}.{t}")
    else:
            print("Your To-Do List is empty.")
#mark a task as done
def mtdar(tindex):
    if 1<=tindex<=len(tlist):
        t=tlist[tindex-1]
        print(f"Task'{t}'marked as done!")
        del tlist[tindex-1]
    else:
        print("Invalid task index.")
while True:
    print("\nOptions:")
    print("1.Add a task")
    print("2.List tasks")
    print("3.Mark a task as done")
    print("4.Quit")
    c=input("Enter your choice (1/2/3/4):")
    if c=="1":
        t=input("Enter the task:")
        addtlist(t)
    elif c=="2":
        alt()
    elif c=="3":
        tindex=int(input("Enter the task number to mark as done:"))
        mtdar(tindex)
    elif c=="4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.Please select 1,2,3,or4.")
