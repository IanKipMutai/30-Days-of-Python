full_name = 'Ian Mutai'
full_name_to_list = list(full_name)
print(full_name_to_list) 



numbers = [20 ,30 ,50 ,60 ,70]
print(max(numbers))
print(min(numbers))
print(sum(numbers))


print('True and True: ', True and True)




for i in range(1,6):
    print(f'{i} {i**0} {i**1} {i**2} {i**3}')

print('In every programming language it starts with \"Hello, World!\"') 


language = 'Python'
a , b, *rest = language
print(a)
print(b)
print(rest)


word = '   Coding For All      ' 
word_1 = word.strip(' ')
word_2 = word_1.split()
word_3 = ' '.join(word_2)
print(word_3)
print(word)
print(word_1)


my_experience = 'I am enjoying this challenge.\nI just wonder what is next.'
print(my_experience)   
print(my_experience[::-1])

string_name =  'Coding For All'
print(string_name.split())

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.strip('because'))



ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(max(ages))
print(min(ages))
print(sum(ages))

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)
del front_end[1:7]
print(front_end)


countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch , ru , us , *scandic_countries = countries
print(ch)
print(ru)
print(us)
print(scandic_countries)


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)

lst = list(nordic_countries)
lst.pop()
print(lst)

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
Ages = [22, 19, 24, 25, 26, 24, 25, 24]
it_companies.add('Twitter')
print(it_companies)

combination = A.union(B)
print(combination)
A.update(B)
print(A)


Sentence = 'I am a teacher and I love to inspire and teach people.' 
new_Sentence = Sentence.split()
print(new_Sentence)
st_sentence = set(new_Sentence)
print(st_sentence)
print(len(st_sentence))


person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print(person['address']['street'])
print(person.get('skills')[0])


person['address']['county'] = 'Nairobi'

print(person)
print(len(person['address']))

tpl_dictionary = person.items()
print(tpl_dictionary)
print()

keys = person.keys()
values = person.values()
print(keys)
print()
print(values)


students = {
    "Ian":85,
    "Mary":91,
    "John":78,
    "James":95
}
print()

print(max(students))
print()

C = {'a':1,'b':2}
D = {'c':3,'d':4}

print(C)

words = ['apple','banana','apple','orange','banana','apple']

dct = {}
for i in words:
    
    if i not in dct :
        count = 1
        dct[i] = count
    else:
        count+=1
        dct[i] = count

print(dct)



vent = 1 
while vent <= 7 :
    print('#' * vent )
    vent += 1
print()


for p in range(8):
    for s in range(8):
        print(' #' , end = '')
    print()


languages = ['Python', 'Numpy','Pandas','Django', 'Flask'] 
for lan in languages:
    print(lan)
print()

for voom in range(11):
    print(f'{voom} x {voom}  = {voom * voom}')
print()

def is_prime(num_list):
    prime = []
    
    for num in num_list:
        Count = 0
        for i in range(1, 100):
            if num % i == 0 :
                Count+=1
            
        if Count == 2 :
            prime.append(num)
            
    return prime

members = [34,56,23,17,19,99] 
print(is_prime(members))


def check_unique (list_1) :
    
    list_3 = []
    list_2 = list_1.copy()
    for i in range (len (list_1)):
        vount = 0
        if list_1[i] in list_2 :
            vount = list_1.count(list_1[i])
        if vount >= 2 :
            
            print(list_1[i] + 'is already in the list')
        

    

check_unique(['a','b','c','a','b'])

import string
from random import*

def random_userID():
    r_1 = string.ascii_lowercase
    r_2 = string.digits
    r_3 = r_1 + r_2
    ls = []
    mount = 0 
    while mount < 6 :
        a1 = randint(0 , 35)
        num = r_3[a1]
        ls.append(num)
        mount += 1
    return  ''.join(ls)


print(random_userID())

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
ls_t = [num for num in numbers if num > 0 ]
print(ls_t)



list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
man = [i for row in list_of_lists for i in row]
print(man)



countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
cnt = [['country:',country, 'city:',city]  for row in countries for country,city in row ]
print(cnt)

Vountries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
Vames = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
Vumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

kim = map(lambda Vount:Vount.upper(),Vountries)
print(list(kim))

def make_discount(percent):
    def discount(price):
        return price*(1-percent/100)
    return discount 

discount_10 = make_discount(10)
print(discount_10(900))


mames = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_vountries , es , ru = mames
print(nordic_vountries)
print(es)
print(ru)
