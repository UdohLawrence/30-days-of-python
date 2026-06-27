# Level 1

# Question 1
empty_tuple = ()

# Question 2
brothers = ("Uduak", "Ete", "Eyo", "Inyang", "Bassey")
sisters = ("Emem", "Iniobong", "Ekemini", "Iniobong")

# Question 3
siblings = brothers + sisters

# Question 4
number_of_siblings = len(siblings)
print("Number of siblings:", number_of_siblings)

# Question 5
family_members = siblings + ("Father", "Mother")
# print("Family members:", family_members)


###############################################
# Level 2
###############################################

# Question 1
siblings, parents = family_members[:9], family_members[9:]
# print("Siblings:", siblings)
# print("Parents:", parents)

# Question 2
fruits = ("apple", "banana", "cherry", "date", "elderberry")
vegetables = ("asparagus", "broccoli", "carrot", "daikon", "eggplant")
animal_products = ("milk", "cheese", "yogurt", "butter", "cream")

food_stuff_tp = fruits + vegetables + animal_products
#print("Food stuff tuple:", food_stuff_tp)

# Question 3
food_stuff_lt = list(food_stuff_tp)
#print("Food stuff list:", food_stuff_lt)

# Question 4
# print(len(food_stuff_tp))
middle_item = food_stuff_tp[7:8]
#print("Middle item:", middle_item)

# Question 5
first_three_items = food_stuff_tp[:3]
#print("First three items:", first_three_items)
last_three_items = food_stuff_tp[-3:]
#print("Last three items:", last_three_items)

# Question 6
del food_stuff_tp
del food_stuff_lt
# print(food_stuff_tp)
# print(food_stuff_lt)

nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print("Estonia" in nordic_countries)  # False
print("Iceland" in nordic_countries)  # True