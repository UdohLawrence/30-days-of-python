# Question 1
empty_list = []

# Question 2
list_with_five_names = ['John', 'Jane', 'Alice', 'Bob', 'Charlie']

# Question 3
print(len(list_with_five_names))

# Question 4
print(list_with_five_names[0], list_with_five_names[2], list_with_five_names[4])

# Question 5
mixed_data_types = ["Ekomobong", 40, 1.74, "married", "Ikot Ekpene"]

# Question 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Question 7
print(it_companies)

# Question 8
print(len(it_companies))

# Question 9
print(it_companies[0], it_companies[3], it_companies[6])

# Question 10
it_companies[0] = 'Meta'
print(it_companies)

# Question 11
it_companies.append('Twitter')
print(it_companies)

# Question 12
it_companies.insert(3, 'LinkedIn')
print(it_companies)

# Question 13
it_companies[0] = it_companies[0].upper()
print(it_companies)

# Question 14
print('#; '.join(it_companies))

# Question 15
print('Facebook' in it_companies)

# Question 16
it_companies.sort()
#it_companies = sorted(it_companies)
print(it_companies)

# Question 17
it_companies.reverse()
print(it_companies)

# Question 18
first_three = it_companies[3:]
print(first_three)

# Question 19
last_three = it_companies[0:-3]
print(last_three)

# Question 20
middle_company = it_companies[5:6]
print(middle_company)

#Question 21
del it_companies[0]
print(it_companies)

# Question 22
del it_companies[4]
print(it_companies)

# Question 24
del it_companies[-1]
print(it_companies)

# Question 25
del it_companies[0:]
print(it_companies)

# Question 26
del it_companies
# print(it_companies)

# Question 27
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
python_sql = ['Python', 'SQL']

new_list_of_tech = front_end + back_end
full_stack = front_end + python_sql + back_end
print(full_stack)

# full_stack.insert(4, 'Python', 'SQL')
# print(full_stack)

###################################################
## Exercises: Level 2
###################################################

# Question 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# a
ages.sort()
min_age = ages.pop(0)
max_age = ages.pop(-1)

# print(min_age)
# print(max_age)
# print(ages)

# b
ages.insert(0, min_age)
ages.append(max_age)

# print(ages)

print(len(ages))