#PRINT
print("Hello World");
print("*" * 11);

#VARIABLES
students_count = 1000
rating = 4.9
is_published = True #boolean values in python start with a capital letter
course_name = "Python Programming"

#STRINGS
message = """
Hello World
This is a multi-line string
"""
#length
message_length = len(message)
#as array
first_letter = message[0] #H
last_letter = message[-1] #g
#slice
slice_message = message[0:5] #Hello
message[0:] #Hello World This is a multi-line string
message[:5] #Hello
message[:] #Hello World This is a multi-line string
#escape sequence 
course = "Python \\,\',\",\nProgramming\""
#formatting
first_name = "John"
last_name = "Doe"
full_name = f"{first_name} {last_name}" #John Doe
#string methods
cohort = "  new programming  "
upper_case = cohort.upper() #  NEW PROGRAMMING  
lower_case = cohort.lower() #  new programming  
title_case = cohort.title() #  New Programming  
strip = cohort.strip() #new programming
left_strip = cohort.lstrip()  #new programming  
right_strip = cohort.rstrip()  #  new programming
index_of_character = cohort.find("pro") #8
replace_character = cohort.replcae("pro","PrO") #  new PrOgramming
character_exist = "pro" in cohort #True
character_not_exist = "pro" not in cohort #False

#NUMBERS
integer = 1
floats = 1.1
complexs = 1 + 2j

division = 10 / 3 #3.3333333
integer_division = 10 // 3 #3
remainder = 10 % 3 #1
exponent = 10 ** 3 #1000

#augmented assignment operator
x = 1
x += 3 #4

#methods
import math
round = round(3.9)  #4
absoulte = abs(-1.22) #1.22
ceiling = math.ceil(3.22) #4

#TYPE CONVERSION
y = input("y: ") #input y is a string
type_of_y = type(y)
int(y)
float(y)
bool(y)
str(y)

#TRUTHY and FALSY
#falsy --> "", 0, None
#truthy --> anything else