import math

# Question 1
age = 40
# Question 2
height = 1.72
# Question 3
complex_number = 3 + 4j

# Question 4 - Calculating the area of a triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print(f"The area of the triangle with base {base} and height {height} is {area}")
print()
print()

# Question 5 - Calculating the perimeter of a triangle
side_a = float(input("Enter the length of side a of the triangle: "))
side_b = float(input("Enter the length of side b of the triangle: "))
side_c = float(input("Enter the length of side c of the triangle: "))
perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle with sides {side_a}, {side_b}, and {side_c} is {perimeter}")
print()
print()

# Question 6 
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print(f"The area of the rectangle with length: {length}, and width: {width} is {area}")
print(f"The perimeter of the rectangle with length: {length}, and width: {width} is {perimeter}")
print()
print()

#Question 7 
radius = float(input("Enter the radius of a circle: "))
area = round((math.pi * math.pow(radius, 2)), 3)
circumference = round((2 * math.pi * radius), 3)
print(f"The area of a circle with radius: {radius} is {area}")
print(f"The circumference of a circle with radius: {radius} is {circumference}")
print()
print()

# Question 8
x_intercept = -(-2) / 2
y_intercept = -2
slope8 = 2
print(f"x-intercept is: {x_intercept}")
print(f"y-intercept is: {y_intercept}")

#Question 9
slope9 = ((10 - 2) / (6 - 2))
print(f"The slope for Question 9 is {slope9}")

# Question 10
if slope9 == slope8:
  print("The slope for Question 8 and Question 9 are equal")
elif slope9 > slope8:
  print("The slope for Question 9 is greater than the slope for Question 8")
else:
  print("The slope for Question 8 is greater than the slope for Question 9")
print()
print()

#Question 11
for x in range(-4, 4):
  y = x ** 2 + 6 * x + 9
  print(f"The y-value for {x} is {y}")
  if y == 0:
    print(f"At x equal to {x}, y is 0")
    break
print()
print()

# Question 12
print(len('python') != len('dragon'))

# Question 13
print('on' in 'python' and 'on' in 'dragon')

# Question 14
print('jargon' in "I hope this course is not full of jargon")

#Question 15
print('on' not in 'python' and 'on' not in 'dragon')

# Question 16
print(str(float(len('python'))))

# Question 17
print()
number = int(input("Enter a number: "))
if number % 2 == 0:
  print(f"{number} is an even number")
else:
  print(f"{number} is not an even number")
print()

# Question 18
print()
print(f"The floor division of 7 by 3 is equal to the int conversion of 2.7: {7 // 3 == int(2.7)}")
print()

# Question 19
print()
print(f"The type of '10' is equal to type of 10: {type('10') == type(10)}")
print()

# Question 20
print()
print(f"The 'int' conversion of '9.8' is equal to 10: {int(9.8) == 10}")
print()

# Question 21
print()
hours_worked = float(input("Enter the number of hours worked: "))
rate_per_hour = float(input("What is the rate per hour? "))
weekly_earning = hours_worked * rate_per_hour
print(f"Your weekly earning is: {weekly_earning}")

# Question 22
print()
number_of_years_lived = int(input("Enter the number of years you have lived: "))
number_of_seconds_lived = number_of_years_lived * 12 * 31 * 24 * 60 * 60
print(f"You have lived for {number_of_seconds_lived} seconds")

# Question 23
print()
for i in range(1, 6):
  print(f"{i}  {1} {i**1}  {i**2}  {i**3}")