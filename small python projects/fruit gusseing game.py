import random 

fruits = ["apple", "orange", "mango" , "grapes", "peach", "Guava", "plum","kiwi"] #fruit list
name = input("What is your name : ") #get user name as input

print("\nHi " + name + "👋. Welcome Fruit Guessing Game . \nLet's start!\n") 

#pick = random.randint(0,7) #create random number
#fruit = fruits[pick].lower() # store a fruit name which is going to guess 
fruit = random.choice(fruits).lower() #choose fruit name randomly
size = len(fruit) #get a size of word
answer = ["_"] * size # create a list for word length

print("This fruit has "+ str(size) + " characters. You can guess characters " + str(size+3) + "times")

count = 1
score = 0

while ((size + 3) >= count): # checking user guessing count over or not
    
    user = input ("Guess a letter : ").lower() #get guessing character
    
    if len(user) != 1: #check user enter character or word
        print("you can only enter one letter!\n")
        count += 1
        continue
    
    if not user.isalpha():  # check if the input is a letter
        print("You can only enter letters!\n")
        count += 1
        continue
    
    if user in answer: #if user already give that character then skip
        print("you already guess this letter!\n")
        count += 1
        continue
    
    for i in range (size):
        if fruit[i] == user: #check user guessing character in fruit name
            
            answer[i] = user
            score += 1 #check how many times user guess correct character
           
    
    for i in range (size):
        print(answer[i])   # print answer with user guessing characters
    

    count += 1
    if score == size :  # check user guess all characters right
        print("\nCongratulations You win🥳")
        break

if count > size + 3 and score < size: # check user is lost or not
    print("You Lost! Your guessing times are over😔\nCorrect answer is " + fruit + ". Please Try again! ")

