from colorama import Fore,Style
import random
import string
list=['rock','paper','scissor']
print(Fore.YELLOW+Style.BRIGHT+"\n====🎮 Rock-Paper-Scissors Game 🎮====\n"+Style.RESET_ALL)
haNa=str(input("Tell me player you want to play this Game(Yes/No) : "))
while(haNa=='yes'):
    print("1. rock ")
    print("2. paper ")
    print("3. scissor ")
    userchoice=str(input(Fore.WHITE+Style.BRIGHT+"Choose one of these from above prompt (rock,paper,scissor) : "+Style.RESET_ALL))
    computerguess=random.choice(list)
    print(f"\n🧍User chooses : {Fore.BLUE}{userchoice}{Style.RESET_ALL}")
    print(f"🤖 Computer chooses :{Fore.CYAN} {computerguess} {Style.RESET_ALL}\n")
    if userchoice==computerguess:
        print("Game is tie! 😐 ")
        haNa=str(input("Want to play this game again (Yes/No) : "))   
        if(haNa=='no'):
            break
        else:
            continue
    elif ((userchoice=='rock' and computerguess=='scissor')or(userchoice=='paper' and computerguess=='rock')or(userchoice=='scissor' and computerguess=='paper')):
        print(Fore.GREEN+Style.BRIGHT+"HURRAH!🎉 You win the Game."+Style.RESET_ALL)
        haNa=str(input("Want to play this game again (Yes/No) : "))   
        if(haNa=='no'):
            break
        else:
            continue
    else:
        print(Fore.MAGENTA+Style.BRIGHT+"💻 Computer win the game!"+Style.RESET_ALL)  
        haNa=str(input("Want to play this game again (Yes/No) : "))   
        if(haNa=='no'):
            break
        else:
            continue
