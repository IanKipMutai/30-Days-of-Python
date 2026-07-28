age = 21
height = 1.82
vector =  1 +1j

base = input ("Enter the base of the triangle :")
height = input ("Enter the height of the triangle :")
area = 0.5 *float(base)* float(height) 
print("Area of the triangle is :" , area )

# the eqaution y = 2x -2 is in the form of y = mx + c where m is the slope and c is the y intercept
m = 2 # the slope 
c = -2 # the y intercept

#calculating the y-intercept 
y_intyercept = (0 , c)

#calculating the x-intercept
x_intercept =  (0 ,m/-c)

print("The slope of the equation is :" ,m )
print("The y-intercept of the euation is :" ,y_intyercept )
print("The x-intercept of the euation is :" ,x_intercept )


sentence = "I hope this course is not full of jargon"
print("is jargon in the sentence ? :" , "jargon" in sentence)

word_1 = "python"
word_2 = "dragon"
len_word_1 = len(word_1)
len_word_2 = len(word_2)
print(len_word_1 is len_word_2) 