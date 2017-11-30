import random # This should be on line 1
# # This is working
#
# print("Hello World")
#
# # Juan
#
# print(3 + 5)
# print(5 - 3)
# print(3 * 5)
# print(6 / 2)
# print(3 ** 2)
#
# print #  this makes a new line, in python 3.6, it looks like: print()
# print("see if you can figure this out")
# print(13 % 12)
















# print ( ""


# print ("%s?! That's really old!

# Functions


def print_hw():
    print ("Hello world")


print_hw()
print_hw()
print_hw()


def say_hi (name):
    print("Hello %s." % name)
    print("Enjoy your day.")


say_hi("Jhon")


def print_age(name,age):
    print("%s is %d years old" % (name, age))
    age += 1  # age = age + 1
    print("Next year, they will be %d" % age)


print_age("Jhon", 15)


def f(x):
   return x**3 + 4 * x**2 + 7 * x - 4


print(f(3))
print(f(4))
print(f(5))




def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage < 90 and percentage >=80 :
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 50:
        return "F"


    '''write a function called "Happy Bday
    that "sings" (prints) Happy birthday
    
    It must take one perameter called "name"
    '''

def happy_bday(name):
    print("Happy birthday to you" + ",")
    print("Happy birthday to you" + ",")
    print("Happy birthday to %s"% name + ",")
    print("Happy birthday to you" + ",")


    happy_bday("Jhon")


# Loops

for num in range(10):
    print(num + 1)

# DO NOT RUN!!!
a = 1
while a <= 10:
    print(a)
    a += 1


# Random Numbers


print(random.randit(0, 100))
