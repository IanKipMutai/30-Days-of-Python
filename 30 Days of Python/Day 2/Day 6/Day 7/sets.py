
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['LinkedIn', 'Snapchat'])
print(it_companies)
it_companies.remove('IBM')
print(it_companies)
it_companies.discard('SPACE X')
print(it_companies)


C = A.union(B)
print(C)

A_intersection_B = A.intersection(B)
print(A_intersection_B)

print('Are sets A and B disjoint ? :', A.isdisjoint(B))

A.update(B)
print(A)
B.update(A)
print(B)

symmetric_deiiference = A.symmetric_difference(B)
print(symmetric_deiiference)

del A
del B
del C


set_age = set(age)
print(set_age)