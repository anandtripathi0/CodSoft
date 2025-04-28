from colorama import Fore,Style
print(Fore.YELLOW+"\n==BASIC CALCULATOR USING PYTHON=="+Style.BRIGHT)
print(Fore.CYAN+Style.BRIGHT+"\n-------------------------------------\n"+Style.RESET_ALL)

while(True):
    print("1. Addition (+) ")
    print("2. Subtraction (-) ")
    print("3. Multiplication (*) ")
    print("4. Division (/) ")
    print("5. Exit (want to exit it.) ")
    print("\n")
    choice=str(input("Choose from this (+,-,*,/) and if you want to exit write (exit) : "))
    if choice=='+':
        num1=float(input(Fore.WHITE+"Enter 1st number : "+Style.BRIGHT))
        num2=float(input(Fore.WHITE+"Enter 2nd number : "+Style.BRIGHT))
        add=num1+num2
        print(Fore.BLUE+f" OK, SUM is : {add}\n"+Style.RESET_ALL)
    elif choice=='-':
        num1=float(input(Fore.WHITE+"Enter 1st number : "+Style.BRIGHT))
        num2=float(input(Fore.WHITE+"Enter 2nd number : "+Style.BRIGHT))
        sub=num1-num2
        print(Fore.BLUE+f" OK, SUBTRACTED value is : {sub}\n"+Style.RESET_ALL)
    elif choice=='*':
        num1=float(input(Fore.WHITE+"Enter 1st number : "+Style.BRIGHT))
        num2=float(input(Fore.WHITE+"Enter 2nd number : "+Style.BRIGHT))
        mul=num1*num2
        print(Fore.BLUE+f" OK, MULTIPLIED value is : {mul}\n"+Style.RESET_ALL)
    elif choice=='/':
        num1=float(input(Fore.WHITE+"Enter 1st number : "+Style.BRIGHT))
        num2=float(input(Fore.WHITE+"Enter 2nd number : "+Style.BRIGHT))
        div=num1/num2
        print(Fore.BLUE+f" OK, DIVIDED value is : {div}\n"+Style.RESET_ALL)
    elif choice=='exit':
        print(Fore.RED+" OK, now exiting the calculator. Goodbye!"+Style.RESET_ALL)
        exit()
    else: print("Invalid Input! ")    