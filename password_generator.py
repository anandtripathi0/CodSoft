from colorama import Fore,Style
import random
import string
print(Fore.YELLOW+Style.BRIGHT+"\n==== PASSWORD GENERATOR ====\n"+Style.RESET_ALL)
length=int(input("Enter the lenght of your password (8-12) : "))

character=string.ascii_letters+string.punctuation+string.digits
password = ''.join(random.choice(character)for i in range(length))
print(Fore.GREEN+Style.BRIGHT+"Your password generated successfully! "+Style.RESET_ALL)
print(f"This is your password :{Fore.CYAN} {password} {Style.RESET_ALL}")                   