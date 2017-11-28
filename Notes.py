# This is working
print("Hello World")

# Rene-Angel Jaime
# (This is python 2.7)

print(3 + 5)
print(5 - 3)
print(3 * 5)
print(6 / 2)
print(3 ** 2)

print # This makes a new line. In python 3.6, it lokks like: print()
print("See if you can figure this out")
print(5 % 3)

car_name = "Chris's car"
car_type = "Tesla"
car_cylinders = 8
car_mpg = 9000.1

# Inline printing
print("I have a car called the %s" % car_name)
print("I have a car called the %s. It's a %s." % (car_name, car_type))

#Asking for input
name = input("What is your name? ") #In python 3, it is called input()
print("Hello %s." % name)

age = input("How old are you? ")
print("%s?! Wow, you belong in a retirement home!" % age)