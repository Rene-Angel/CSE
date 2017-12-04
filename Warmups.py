# New python File: Warmups.py

# 12.4.17
# Write a Python program
# which accepts the user's
# first and last name
# and print them in reverse order
# with a space between them.

# def reverse_order(first_name, last_name):
#     print("%s, %s" % (last_name, first_name))
#     print(last_name + " " + first_name)

def reverse_order(first_name, last_name):
    first_name = input("First name")
    last_name = input("Last name")
    print("%s, %s" % (last_name, first_name))