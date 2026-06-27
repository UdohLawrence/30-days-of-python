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

print(ages)

# c

if len(ages) % 2 == 0:
    median_age = (ages[len(ages) // 2] + ages[len(ages) // 2 - 1]) / 2
else:
    median_age = ages[len(ages) // 2]

print(f"Median age: {median_age}")

# d
sum_of_ages = sum(ages)
average_age = sum_of_ages / len(ages)
print(f"Average age: {average_age}")

# e
age_range = max_age - min_age
print(f"Age range: {age_range}")

print(f"Minimum value - Average value: {abs(min_age - average_age)}")
print(f"Maximum value - Average value: {abs(max_age - average_age)}")

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

print(len(countries))
middle_country = countries[len(countries) // 2]
print(middle_country)
print(countries.index(middle_country))


if len(countries) % 2 == 0:
  first_countries = countries[:len(countries) // 2 - 1]
  last_countries = countries[len(countries) // 2:]
else:
  first_countries = countries[:len(countries) // 2 + 1]
  last_countries = countries[len(countries) // 2 + 1:]
print(len(first_countries))
  
print(len(last_countries))

print((len(first_countries) + len(last_countries)) == len(countries))

first, second, third, *scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

print(first)
print(second)
print(third)
print(scandic)