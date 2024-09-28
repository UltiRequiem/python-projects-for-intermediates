import random


def winner(user, cpu):
    
    if (user == "Rock" and cpu == "Paper") or (user == "Paper" and cpu == "Scissor") or (user == "Scissor" and cpu == "Rock"):
        return "\nUser : " + user + "\nCPU : " + cpu + "\nWinner : CPU"
    
    elif(cpu == "Rock" and user == "Paper") or (cpu == "Paper" and user == "Scissor") or (cpu == "Scissor" and user == "Rock"):
        return "\nUser : " + user + "\nCPU : " + cpu + "\nWinner : User"
    
    elif user == cpu:
        return "\nUser : " + user + "\nCPU : " + cpu + "\nWinner : Draw"
        

options = ["Rock", "Paper", "Scissor"]

while True:
    UI = input("\nEnter Your Choice (rock, paper, scissor) : ").title()
    
    if UI not in options:
        continue
    print(winner(UI, random.choice(options)))

    YN = input("\nPlay Again? (yes/no) : ").lower()
    if YN == "no":
        break
