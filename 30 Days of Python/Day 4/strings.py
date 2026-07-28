challenge = ["Thirty", "Days", "Of", "Python"]
result = " , ".join(challenge)
print(result)

company = "coding for all"
print(len(company))
print(company.upper())
print(company.capitalize())
print(company.swapcase())
print(company.title())

print(company[0:6])
print(company.find("coding"))
print('coding' in company)

print(company.replace('coding' , 'python'))

print(company.split(' '))

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(companies.split(','))

print(company.rfind('l'))
print(company[10])

acronym_1 = 'Python for Everyone'
print(acronym_1.strip('ython'))


challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'

print(company.index('c'))
print(company.find('c'))

exercise = 'You cannot end a sentence with because because because is a conjunction'
print(exercise.find('because'))
print(exercise.index('because'))
print(exercise.rfind('because'))
print(exercise.rfind('e'))
print(exercise.replace('because',''))

print(company.startswith('coding'))

company_2 = '  coding for all  '
print(company_2.strip(' '))
print(company_2)

python_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(python_lib))

sentence = 'I am enjoying this challenge.\nI just wonder what is next.'
print(sentence)

person = 'Name\tAge\tCountry\tCity\nIan\t21\tKenya\tNairobi'
print(person)

radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius %d is %.2f meters square.' %(radius, area))


a = 8
b = 6 

print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} % {b} = {a%b}')
print(f'{a} ** {b} = {a**b}')