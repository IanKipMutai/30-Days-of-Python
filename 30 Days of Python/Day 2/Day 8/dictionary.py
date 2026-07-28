dog = {}
dog['name'] = 'Chase'
dog['color']= 'Brown'
dog['breed'] = 'Rotwiller'
dog['legs'] = 4
dog['age'] = 2

student = {
    'first name': 'Ian',
    'last name': 'Mutai',
    'gender': 'male',
    'age': 20,
    'marital status': 'single',
    'skills': ['Python', 'JavaScript', 'HTML', 'CSS'],
    'country': 'Kenya',
    'city': 'Nairobi',
    'address': 'Nyayo Estate'
}

print(len(student))
print(student['skills'])

student['skills'].append('Django')
student['skills'].append('Flask')
student['skills'].append('React')
print(student['skills'])

print(student.keys())

print(student.values())

print(student.items())

student.popitem()
print(student)

print(dog)
del dog 
print(dog)

