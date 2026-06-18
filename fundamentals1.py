#OPERATORS

#comparision
# >, <, >=, <=, ==, !=

#logical
# and, or, not

#CONDITIONALS
temprature = 35
if temprature > 30:
    print("it is hot ooutside")
elif temprature > 20:
    print("it is good outside")
else:
    print('wear a jacket')
print("thermostat is working good")

#ternerary operator
age = 23
if age >= 18:
    message = 'Eligible'
else:
    message = 'not eligible'

message = "Eligible" if age >= 18 else "not eligible"
print(message)

#LOOPS

#For Loop
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 4):
    print("Attempt", number, number * ".")

for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

#for-else
succesful = True

for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")
    if succesful:
        print("success")
        break

failed = False
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")
    if failed:
        print("failed")
        break
else:
    print("success")

#iterable
#range, strings, arrays are iterable items

for x in [1,3,5,7]:
    print(x)

for x in "Python Programming":
    print(x)

#While Loop
number = 0

while number < 6:
    print(number)
    number += 1

#FUNCTIONS
time_of_day = "morning"

def greet(time_of_day):
    print(f"good {time_of_day}")

greet(time_of_day)

#keyword arguments
greet(time_of_day="afternoon")

#xargs -- unknown number of arguments

def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

print(multiply(1,2,3,4,5))