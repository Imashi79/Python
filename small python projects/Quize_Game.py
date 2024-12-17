print("Welcome to my Quize Game!")

play = input("Do you want to play? ")

if play.lower() != "yes":{
    quit()
}
score = 0
print("\nLet's Start!")
answer = input("Q-01.What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

answer = input("Q-02.What does ROM stands for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

answer = input("Q-03.What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

answer = input("Q-01.What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions Correct!")
print("You got " + str((score / 4)) + "%")