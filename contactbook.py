from colorama import Fore,Style
import string
print(Fore.YELLOW+Style.BRIGHT+"\n=== CONTACT BOOK ===\n"+Style.RESET_ALL)
names=[]
phone_numbers=[]
Emails=[]
S_NO=[]
Addresses=[]
delete=[]
while(True):
    print("1. Add contact")
    print("2. View contact")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit ")
    choice=int(input("Choose from above prompt : "))
    if choice==1:
        total=int(input("Tell me how many contact want to add? : "))
        for i in range(total):
            S_NO.append(str(i))
            name=str(input(f"Enter {i} Store name : "))
            names.append(name)
            phoneNo=int(input(f"Enter {i} contact Phone number : "))
            phone_numbers.append(phoneNo)
            email=str(input(f"Enter {i} contact Email id : "))
            Emails.append(email)
            add=str(input(f"Enter {i} contact Address : "))
            Addresses.append(add)
            print("\n")
    elif choice==2:
            for i in range(total):
                if S_NO[i]==delete:
                  print("data is already deleted")
                else:
                  print(f"S_NO. : {i} \nSTORE NAME : {names[i]} \nPhone_Number : {phone_numbers[i]} \nEMAIL : {Emails[i]}     \nADDRESS : {Addresses[i]}")  
                print("\n")      
    elif choice==3:
        search=str(input("Enter store_name or S_NO. to search a contact details : "))
        for i in range(total):
                if (search==names[i])or(search==S_NO[i]):
                   print(f"S_NO. : {i} \nSTORE NAME : {names[i]} \nPhone_Number : {phone_numbers[i]} \nEMAIL : {Emails[i]} \nADDRESS : {Addresses[i]}")
                   print("\n")         
    
    elif choice==4:
        for i in range(total):
            print("\n")
            print(f"S_NO. : {i} \nSTORE NAME : {names[i]} \nPhone_Number : {phone_numbers[i]} \nEMAIL : {Emails[i]} \nADDRESS : {Addresses[i]}")  
        update=str(input("\ngive me S_NO. of contact detail for updation : "))
        if update:
            for i in range(total):
                if S_NO[i]==update:
                    updated_name=str(input("Tell me updated store name : "))
                    names[i]=updated_name
                    updated_phoneNo=int(input("Tell me updated phone_number : "))
                    phone_numbers[i]=updated_phoneNo
                    updated_email=str(input("Tell me updated email id : "))
                    Emails[i]=updated_email
                    updated_add=str(input("Tell me updated address : "))
                    Addresses[i]=updated_add
                    print("✅ All data updated successfully!\n")  
                    # total-1
                    break
        else:print("Invalid S_NO!")          
    elif choice==5:
        for i in range(total):
            print("\n")
            print(f"S_NO. : {i} \nSTORE NAME : {names[i]} \nPhone_Number : {phone_numbers[i]} \nEMAIL : {Emails[i]} \nADDRESS : {Addresses[i]}")  
        delete=str(input("Give me S_NO. of contact detail for delete process : "))
        if delete:
            for i in range(total):
                if S_NO[i]==delete:
                    del S_NO[i]
                    del names[i]   
                    del phone_numbers[i]   
                    del Emails[i]   
                    del Addresses[i] 
                    print(f"✅ All data of S_NO. {delete} successfully deleted!\n") 
                    total-=1
                    break
        else:print("Invalid S_NO.! ")         
    elif choice==6:
        print("exiting the program!..")
        exit()
    else:print("Invalid choice! ")    
