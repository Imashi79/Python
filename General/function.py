'''Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
area = (1/2)*base*height'''
def calculate_area(base ,height):
    area = (1/2)*base*height
    return area
print("area of triangle " ,calculate_area(2,4))

'''Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle".
 Based on shape type it will calculate area. Equation of rectangle's area is,
rectangle area=length*width
If no shape is supplied then it should take triangle as a default shape'''
def calculate_areas(base ,height, shape):
    if shape == "triangle":
        area = (1/2)*base*height
    elif shape == "rectangle":
        area=base*height
    else:
        print("shape not founded.", end=' ')
        area = 0
    return area
print("area of triangle " ,calculate_areas(2,4,'triangle'))
print("area of rectangle " ,calculate_areas(2,4,'rectangle'))
print("area of circle " ,calculate_areas(2,4,'circle'))
'''
Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
*
**
***
if input is 4 then it should print

*
**
***
****
Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)'''

def print_pattern (number):
    for i in range (1 , number+1):
        for j in range (1 ,i+1):
            print("*", end='')
        print()    

print_pattern(3)
print_pattern(4)        