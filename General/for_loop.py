'''After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
Using for loop figure out how many times you got heads'''

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
total = 0
for i in range(len(result)):
    if result[i] == 'heads':
        total += 1
print("times you got heads :" , total)

'''Print square of all numbers between 1 to 10 except even numbers'''
print("\nsquare numbers")
for i in range(1,11):
    if i % 2 == 0 :
        continue
    print(i * i) 

'''Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred.
 If expense is not found then it should print that as well.'''
expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ["January", "Febuary", "March", "April", "May"]
expenses = input("\nenter an expense amount: ")
expenses = int(expenses)
month = 0
for i in range (len(expense_list)):
    if expenses == expense_list[i]:
        month = 1
        a = i
        break
if month == 1:
        print(expenses , " is occured in " + month_list[a])
else:
     print("not founded")

'''Lets say you are running a 5 km race. Write a program that,
Upon completing each 1 km asks you "are you tired?"
If you reply "yes" then it should break and print "you didn't finish the race"
If you reply "no" then it should continue and ask "are you tired" on every km
If you finish all 5 km then it should print congratulations message '''
distance = 0
while True:
    if distance == 5:
          print("Congratulations you finished the race ")
          break
    distance += 1
    print("you finished " , distance, " km")
    choise = input("Are you tired?(y/n) : ")
    if choise == 'y':
         print("you didn't finish the race")
         break

'''
Write a program that prints following shape

*
**
***
****
*****  '''

for i in range(1,6):
    for j in range (1, i+1):
          print("*", end='')
    print()     