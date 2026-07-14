numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positive_numbers = [num for num in numbers if num > 0]
print(positive_numbers)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [numbers for row in list_of_lists for numbers in row]
print(flattened_list)


multiple = [(i, 1, i*1, i**2, i**3, i**4, i**5, i**6 ) for i in range(11)]
print(multiple)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [republic for row in countries for city in row for republic in city ]
flattened_countries

ls = flattened_countries[0]
abbreviation = ls[0:3].upper()
flattened_countries.insert(1,abbreviation)

ls_1 = flattened_countries[3]
abbreviation = ls_1[0:3].upper()
flattened_countries.insert(4,abbreviation)

ls_2 = flattened_countries[6]
abbreviation = ls_2[0:3].upper()
flattened_countries.insert(7,abbreviation)

flattened_countries = "Finland, FIN, Helsinki\n Sweden, SWE, Stockholm\n Norway, NOR, Oslo"

flattened_countries = [line.split(',') for line in flattened_countries.split('\n')]

print(flattened_countries)

