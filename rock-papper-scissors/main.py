import random 


def winner(user, cpu):
#in cases where CPU is winner
    if (user == "Rock" and cpu == "Paper") or (user == "Paper" and cpu == "Scissor") or (user == "Scissor" and cpu == "Rock"):
        return "\nUser : " + user + "\nCPU : " + cpu + "\nWinner : CPU"
    #in cases where User is winner
    elif(cpu == "Rock" and user == "Paper") or (cpu == "Paper" and user == "Scissor") or (cpu == "Scissor" and user == "Rock"):
        return "\nUser : " + user + "\nCPU : " + cpu + "\nWinner : User"
    #in cases of ties
    elif user == cpu:
        return "\nUser : " + user + "\nCPU : " + cpu + "\nWinner : Draw"
        
#list of options program uses
options = ["Rock", "Paper", "Scissor"]

while True:
    UI = input("\nEnter Your Choice (rock, paper, scissor) : ").title()
    
    #program continues
    if UI not in options:
        continue 
    print(winner(UI, random.choice(options)))

    YN = input("\nPlay Again? (yes/no) : ").lower()
    if YN == "no":
        break 
