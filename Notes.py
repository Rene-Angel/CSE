# This is working
# print("Hello World")
#
# Rene-Angel Jaime
# (This is python 2.7)
#
# print(3 + 5)
# print(5 - 3)
# print(3 * 5)
# print(6 / 2)
# print(3 ** 2)
#
# print # This makes a new line. In python 3.6, it lokks like: print()
# print("See if you can figure this out")
# print(5 % 3)
#
# car_name = "Chris's car"
# car_type = "Tesla"
# car_cylinders = 8
# car_mpg = 9000.1
#
# # Inline printing
# print("I have a car called the %s" % car_name)
# print("I have a car called the %s. It's a %s." % (car_name, car_type))
#
# #Asking for input
# name = input("What is your name? ") #In python 3, it is called input()
# print("Hello %s." % name)
#
# age = input("How old are you? ")
# print("%s?! Wow, you belong in a retirement home!" % age)

# Functions


# def print_hw():
#     print("Hello World")


# print_hw()
# print_hw()
# print_hw()


# def say_hi(name):  # name is parameter
#     print("Hello %s." % name)
#     print("Enjoy your day.")


# say_hi("John")


# def print_age(name, age):
#     print("%s is %d years old." % (name, age))
#     age += 1  # age = age + 1
#     print("Next year, they will be %d" % age)


# print_age("John", 15)


# def f(x):
#     return x ** 3 + 4 * x ** 2 + 7 * x - 4


# print(f(3))
# print(f(4))
# print(f(5))


# If statements


# def grade_calc(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80:
#         return "B"
#     elif percentage >= 70:
#         return "C"
#     elif percentage >= 60:
#         return "D"
#     else:
#         return "F"


# '''Write a function called "happy_bday"
# that "sings" (prints) Happy birthday

# It must take one parameter called "name"
# '''


# def happy_bday(name):
#     print("Happy Birthday to you" + ",")
#     print("Happy Birthday to you" + ",")
#     print("Happy Birthday to " + name + ",")
#     print("Happy Birthday to you" + ".")

# happy_bday("John")


# Loops


# for num in range(1000000):
#     print(num + 1)

# DO NOT RUN!!!
# a = 1
# while True:
#     print(a)

# a = 1
# while a < 10:
#     print(a)
#     a += 1

# Random numbers

# import random # This should be on line 1
# print(random.randint(0, 100))

# Comparisons
print(1 == 1)  # Is 1 equal to 1?
print(1 != 2)  # Is 1 not equal to 2?
print(10 <= 15)
print(not False)

# Recasting

c = '1'
print(c == 1)
print(int(c) == 1) # Both are ints
print(c == str(1)) # Both are strings

# The input command ALWAYS gives a string
