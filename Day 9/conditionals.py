age = int(input('Enter your age : '))
if age >= 18 :
    print("You are old enough to drive .")
else :
    balance = 18 - age 
    print(f"You need to wait {balance} more years to drive .")



my_age = 20 
your_age = int(input('Enter your age : '))

if my_age > your_age :
    diff = my_age - your_age 
    if diff ==1 :
        print('year')
    else:
        print('years')

    print(f"I am {diff} years older than you .")

else :
    diff =your_age - my_age
    if diff ==1:
        print('year')
    else:
        print('years')

    print(f"You are {diff} years older than me .") 




fruits = ['banana', 'orange', 'mango', 'lemon']
enter_fruit = input(' Enter a fruit :').strip(' ').lower()
if enter_fruit in fruits :
    print("That fruit already exists in the list . ")
else :
    fruits.append(enter_fruit)
    print(fruits)  





person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': [ 'Javascript', 'React','Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
    }


if 'skills' in person :
    print(f'Middle skill : {person["skills"][len(person['skills'])//2]}')
    print('Flask' in person['skills'])


if person['skills'] == ['Javascript', 'React'] :
    print('He is a frontend developer')
elif person['skills'] == ['Node','MongoDB' ,'Python'] :
    print('He is a backend developer ')
elif person['skills'] == ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']:
    print('He is a fullstack developer')
else:
    print('Unknown title')
