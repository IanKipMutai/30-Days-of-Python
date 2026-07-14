from random import randint
from string import ascii_lowercase

def random_user_ID():
    num =str(randint(300,400))
    num2 = ascii_lowercase[22:]
    return num + num2

print(random_user_ID())


def user_id_gen_by_user():
    num_char = input('Enter number of characters :')

    return [randint(0, 9) for i in range(int(num_char))]

def list_of_hexa_colors():
    color_list ='ABCDEF0123456789'
    count = 0 
    num = 0 
    colours = []
    while count < 6 :
        for i in color_list:
            while num < 6:
                i
          
        
    return colours 

print(list_of_hexa_colors())



    

 
