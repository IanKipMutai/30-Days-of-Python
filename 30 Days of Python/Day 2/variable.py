first_name = 'Ian'
last_name = 'Mutai'
full_name = first_name + ' ' + last_name
country_name = 'Kenya'
city_name = 'Nairobi'
age = 21
year = 2026
is_married = False
is_true = True
is_light_on = True
school_name , course_name , student_year, = 'KCA University', 'Software Engineering', '2nd Year'


print(type(first_name))  # Output: <class 'str'>
print(type(last_name))   # Output: <class 'str'>
print(type(full_name))   # Output: <class 'str'>
print(type(country_name))  # Output: <class 'str'>
print(type(city_name))  # Output: <class 'str'>
print(type(age))  # Output: <class 'str'>
print(type(year))  # Output: <class 'str'>
print(type(is_married))  # Output: <class 'bool'>
print(type(is_true))  # Output: <class 'bool'>
print(type(is_light_on))  # Output: <class 'bool'>
print(type(school_name))  # Output: <class 'str'>
print(type(course_name))  # Output: <class 'str'>
print(type(student_year))  # Output: <class 'str'>

len_first_name = len(first_name)
len_last_name = len(last_name)
print(len_first_name)  # Output: 3
print((len_first_name, len_last_name))  # Output: -1


num_one = 34
num_two = 23
remainder = num_one % num_two
print('Remainder:', remainder)  