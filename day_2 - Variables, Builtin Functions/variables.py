# Day 2: 30 Days of Python Programming

first_name = "Ekomobong"
last_name = "Lawrence"
full_name = first_name + last_name
country = "Nigeria"
city = "Ikot Ekpene"
age = 40
year = 2026
is_married = True
is_true = True
is_light_on = False

length, width, area = 5, 6, 30

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(length))
print(type(area))

print(len(first_name))
print(len(last_name))

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_one - num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
area_of_circle = 3.14 * radius ** 2
print(f"Area of a circle with radius {radius} is {area_of_circle}cm^2")
circum_of_circle = 2 * 3.14 * radius
print(f"Circumference of a circle with radius {radius} is {circum_of_circle}cm")

input_radius = float(input("Enter a value for the radius of your circle: "))
input_area = 3.14 * input_radius ** 2
print(f"Area of a circle with radius {input_radius} is {input_area}cm^2")
input_circum = 2 * 3.14 * input_radius
print(f"Circumference of a circle with radius {input_radius} is {input_circum}cm")
