import random
option = ["rock", "paper", "scissor"]
user_Score = 0
Computer_Score = 0
count = 0
while True:
    user_pick = input("Pick Rock/Paper/Scissor or Q to quit : ").lower()
    
    if user_pick == 'q':
        break
    
    if user_pick not in option:
        print("please Enter Rock/Paper/Scissor")
        continue

    pick = random.randint(0,2)
    computer_pick = option[pick]
    print("Computer pick : " + computer_pick)
    count += 1
    if user_pick == "rock" and computer_pick == "scissor" :
        print("You Won!\n")
        user_Score += 1
    elif user_pick == "paper" and computer_pick == "rock" :
        print("You Won!\n")
        user_Score += 1
    elif user_pick == "scissor" and computer_pick == "paper" :
        print("You Won!\n")
        user_Score += 1
    elif user_pick == computer_pick:
        print("You Tie!\n")
    else :
        print("you Lost!\n")
        Computer_Score += 1

print("\nyou play "+ str(count) + "times.")
print("you wins " + str(user_Score)  + " times.")
print("Computer wins " + str(Computer_Score) +" times.")

