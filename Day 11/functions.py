def add_two_numbers(num1 , num2):
    sum = num1 + num2
    return sum
print(add_two_numbers(67,76))

def area_of_circle(radius):
    area = 3.142 *radius**2
    return area
print(area_of_circle(10))

def add_all_nums(*nums):
    total = 0
    for num in nums:
        if isinstance(num, (int, float)):
            print(f'{num} is a real number .')
            total += num
            
        else:
            return 'Enter Real numbers'

    
    return total

print(add_all_nums(10,20,40,56))


def convert_celsius_to_fahrenhite(celsius):
    farenhite = (celsius * 9/5) + 32
    return f'{celsius} C when conveted to F is {farenhite}'

print(convert_celsius_to_fahrenhite(25))


def print_list(items):
    
    for ls in items :
        print(ls)
    
fruits = ['mangoes','banans','oranges']

print_list(fruits)



def reverse_list(numbers):
    ls = []
    for num in numbers:
        ls.append(num)
    ls.reverse()
    return ls

numb = [23,45,67,89,21,99]
print(reverse_list(numb))



