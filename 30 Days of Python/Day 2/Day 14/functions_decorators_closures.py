countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for count in countries:
    print(count)
print()
for nam in names :
    print(nam)
print()
for num in numbers:
    print(num)
print()


def make_upper(count):
    return count.upper()

result = map(make_upper , countries)
print(list(result))


def change_to_square(x):
    return x*x
square = map(change_to_square, numbers)
print(list(square))


def contains_land(reg):
    if "land" in reg:
        return False
    else:
        return True
regions = filter(contains_land , countries)
print(list(regions))


def six_characters(place):
    if len(place) <= 6 :
        return True
    else :
        return False 
    
char = filter(six_characters , countries)
print(list(char))



def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_upper = func.upper()
        return make_upper
    return wrapper

def greet():
    return 'Welcome to Python'

mambo = uppercase_decorator(greet)
print(mambo())

@uppercase_decorator
def greetings():
    return 'hello world'
print(greetings())

