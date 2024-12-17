#You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.

length = 92.8
width = 48.8
area = length * width
print (round(area, 2))

#You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. 
#Find out using python, how many dollars is the shopkeeper going to give you back?

rest_of_money = 20 - (1.49 * 9)
print(rest_of_money)

'''You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. 
If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. 
Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)'''

square_area = 5.5 ** 2
cost = square_area * 500
print ("cost" , cost)

#Print binary representation of number 17

no = 17 
print("Binary of number " +str(no)+ " is: " ,format(no,'b'))