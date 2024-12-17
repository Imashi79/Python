import random
print("Number Guessing Game!\n ")

top_value = input("Enter a number :")

if top_value.isdigit():
    top_value = int(top_value)

    if top_value <= 0 :
        print("Please type a number larger than 0 next time.")
else:
    print("Please type a number next time")


print("Let start!🥳🥳🥳")
random_number = random.randint(0,top_value)
while True:
    guess_no = input("Guess a number: ")
    if guess_no.isdigit():
        guess_no = int(guess_no)
    else:
        print("Please type a number next time😑")
        continue

    if guess_no == random_number:
        print("You Got It!😀")
        break
    else:
        print("You Got It Wrong! Try Again😔")
    
