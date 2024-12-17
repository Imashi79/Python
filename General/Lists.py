'''Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this'''

expenses = [2200,2350,2600,2130,2190]
#1
print("1.extra money spended : $" , (expenses[1]-expenses[0]))
#2
print("2.total expense in first quarter (first three months) : $", (sum(expenses[0:3])))
#3
print("3.",2000 in expenses)
#4
expenses.append(1980)
print("4.ater adding june month expenses" ,expenses)
#5
expenses[3] -=  200
print("5.after got refund 200$ in April " ,expenses)
print("\n ")

'''You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)'''

heros=['spider man','thor','hulk','iron man','captain america']
#1
print("1.Length of the list : " , len(heros))
#2
heros.append("black panther")
print("2. after adding black panther : " , heros)
#3
heros.remove("black panther")
heros.insert(3,"black panther")
print("3.after changing place of black panther  : " , heros)
#4
heros[1:3] = ["doctor strange"]
print(heros)
#5
heros.sort()
print(heros)