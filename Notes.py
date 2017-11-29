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
