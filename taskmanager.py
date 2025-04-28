from colorama import Fore,Style
tasks=[]
status=[]
while(True):
        print("\n===TO-DO List===\n")
        print('1.'+ "Add task")
        print('2.'+ "View task")
        print('3.'+ "Mark task as completed")
        print('4.'+ "Delete task")
        print('5.'+ "Exit")
        print("\n")
        choice=int(input("Enter your choice : "))
        if(choice==1):
          totaltask=int(input("How many task you want to add : "))
          for i in range(totaltask):
            task=input(Fore.CYAN+"Enter "+f"{i+1}"+" task name : "+Style.RESET_ALL)
            tasks.append(task)
            stat=input(Fore.MAGENTA+"and also enter task status(completed\pending) : "+Style.RESET_ALL)
            status.append(stat)
        elif(choice==2):
            for i in range(len(tasks)):
                print(f"{i+1}. task is {Fore.GREEN}{tasks[i]}{Style.RESET_ALL} and status is {Fore.RED}{status[i]}{Style.RESET_ALL}")
        elif(choice==3):
            for i in range(len(tasks)):
                if (status[i]=="completed"):
                    print(f"{i+1}. the task is {Fore.YELLOW}{tasks[i]} [✔]{Style.RESET_ALL}")  
        elif(choice==4):
            tasknumber=int(input("Enter task number which you want to delete : "))
            if(0<tasknumber<=totaltask):
                del tasks[tasknumber-1]
                print(f"Your task successfully deleted!")
            for i in range(len(tasks)):
                print(f"{Fore.GREEN}{i+1}. {tasks[i]}{Style.RESET_ALL}") 
        elif(choice==5):
            print("Exiting the program. Goodbye!")        
            exit()
        else: print("invalid task!")    

                              