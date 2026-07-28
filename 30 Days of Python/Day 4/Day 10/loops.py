for number in range(11):
    print(number)

count = 0
while count < 11 :
    print(count)
    count+=1

for num in range(10,-1,-1):
    print(num)


Count = 10 
while Count >= 0 :
    print(Count)
    Count-=1

 

i = 1
j = 1
m = 8

while i<=7 and j<=7 :
    print('#'*j)
    i+=1
    j+=1


while i <= 8 :
    while j <= 8:
        print('# ' * 8)
        j+=1
    i+=1  


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)



for rows in range(8):
    for columns in range(8):
        print('# ', end='')
    print()



for num in range(11):
    result = num*num
    print(f"{num} * {num} = {result}" )


skills = ['Python', 'Numpy','Pandas','Django', 'Flask']
for skill in skills :
    print(skill)


for integers in range(101):
    result = integers % 2
    if result != 0:
        continue
    print(integers)

for integers in range(101):
    result = integers % 2
    if result == 0:
        continue
    print(integers) 

sum = 0
for num in range(101):
    sum += num 
    
print(f'The sum of all numbers is {sum}')

total_sum = 0
sum_even = 0
sum_odd = 0 

for Numbers in range(101):
    result = Numbers % 2
    if result == 0 :
        sum_even += Numbers
    else:
        sum_odd += Numbers 

total_sum = sum_even + sum_odd
print(f'The sum of all even and odd numbers between 0 and 100 is {total_sum}')
print(f'The sum of all even numbers is {sum_even}')
print(f'The sum of all odd numbers is {sum_odd}')









    


        



