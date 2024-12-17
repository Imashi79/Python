'''Using following list of cities per country,
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
Write a program that asks user to enter a city name and it should tell which country the city belongs to
Write a program that asks user to enter two cities and it tells you if they both are in same country or not. 
For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and 
dhaka it should print "They don't belong to same country" '''

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

#question 01
city = input("Enter a city name : ")
if  city in india :
      print (city + " is belong  to India")
elif city  in  pakistan:
      print (city + " is belong  to Pakistan")
elif city in bangladesh:
      print(city + " is belong  to Bangalsdesh")
else:
      print("not belonged to India, pakistan or bangladesh")
          
#question 02
print()
city1 = input ("Enter a city name : ")
city2 = input ("Enter a city name : ")

if  city1 in india and city2 in india :
      print ("both cities are  belong  to India")
elif city1  in  pakistan and city2  in  pakistan :
      print ("both cities are belong  to Pakistan")
elif city1 in bangladesh and city2 in bangladesh:
      print("both cities are belong  to Bangalsdesh")
else:
      print("both cities are not belonged to same country ")


'''
Write a python program that can tell your if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
Ask user to enter his fasting sugar level
If it is below 80 to 100 range then print that sugar is low
If it is above 100 then print that it is high otherwise print that it is normal'''

suger = input("Enter your fasting sugar level : ")
suger = float(suger)

if suger < 80 :
      print("sugar is low")
elif 80 <= suger and suger <= 100:
      print ("suger is normal")  
else:
      print("suger is high")          