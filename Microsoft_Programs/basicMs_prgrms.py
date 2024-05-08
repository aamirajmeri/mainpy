# x = 'This is a string'
# print(x) # outputs: This is a string
# print(type(x)) # outputs: <class 'str'>
# y = "This is also a string"

# x = input("Enter your name")
# print(type(x))

# x = int(input("Enter a number"))
# print(type(x))

# x = 5
# print("Enter a number is" + str(x))

# sum = 1 + 7
# a = sum * 4
# print(a)


#####.......Operators ***

# l_side = 4
# r_side = 2
# l_side / r_side




#******** Date ******

# from datetime import date
# date.today()
# datetime.date(2024, 5, 6)
# print(date.today())
# 2024-05-06
# print("Today's date is:" + str(date.today()))
# Today's date is:2024-05-06



# parsecs = 11
# lightyears = parsecs * 3.26
# print(f"{parsecs} +  your parsecs is  + {lightyears} + the lightyears is")
#                 OR
# parsecs = 11
# lightyears = parsecs * 3.26
# print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")


# import sys

# print(sys.argv)
# print(sys.argv[0]) # program name
# print(sys.argv[1]) # first arg
# print(sys.argv[2]) # second arg


# name = input("Enter your name:")
# print("Greeting " + name)


##....... print("calculator program")
# first_number = input("first number: ")
# second_number = input("second number: ")
# print(first_number + second_number)

# print("string")
# a = "string"
# print(type(a))



#******* 7 - 5 - 24 ******#

# if else statements

# a = 88
# b = 43
# if a >= b:
#   print(a)
# else:
#   print(b)


# a = 44
# b = 44
# if a <= b:
#   print("a is less than or equal to b")
# elif a == b:
#   print("a is equal to b")



# a = 88
# b = 44
# if a < b:
#   print("a is less than b")
# elif a > b:
#   print("a is greater than b")
# else:
#   print("a is equal to b")


# a = 16
# b = 25
# c = 27
# if a > b:
#   if a > c:
#     print("a is greater than b & b is greater than c")
#   else:
#     print("a is greater than b & less than c")
# elif a == b:
#   print("a is equal to b")
# else:
#   print("a is less than b")


# a = 23
# b = 34
# if a == 34 or b == 34:
#   print(a + b)

# a = 23
# b = 34
# if a == 34 and b == 34:
#   print(a + b)


#*************     QUESTIONS   *****************#   And Operator
# For this step you will be presented with the goal for the exercise, followed by an empty cell. Enter your Python into the cell and run it. The solution is at the bottom of the exercise.

# Add the code to the cell below to create two variables: object_size and proximity. Set object_size to 10 to represent 10m3. Set proximity to 9000.
# Then add the code to display a message saying Evasive maneuvers required if both object_size is greater than 5 and proximity is less than 1000. Otherwise display a message saying Object poses no threat.

# object_size = 10
# proximity = 9000

# if object_size > 5 and proximity < 1000:
#   print("evasive maneuvers required")
# else:
#   print("Object poses no threat")




# print("temperatures and facts about the moon".title())


# heading = "temperatures and facts about the moon"
# heading_upper = heading.title()
# print(heading_upper)


# temperatures = "Daylight: 260 F Nighttime: -299 F"
# temperatures_list = temperatures.split()
# print(temperatures_list)

# temperatures = "Daylight: 260 F\n Nighttime: -299 F"
# temperatures_list = temperatures.split('\n')
# print(temperatures_list)

# print("Moon" in "This text will describe facts and challenges with space travel")


# temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
# print(temperatures.find("Moon"))   


# temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
# print(temperatures.find("Mars"))
# 64th Position where "Mars" appears in the string.
                 # # OR (another method content to use .count() method which returns the total number of occurrences of a substring in a string))
# temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
# print(temperatures.count("Mars"))
# print(temperatures.count("Moon"))

# print("This is Aamir".upper())

# #******* NOTE ********#
# When you're searching for and checking content, a more robust approach is to lowercase a string so that casing doesn't prevent a match. For example, if you're counting the number of times the word the appears, the method wouldn't count the times where The appears, even though they're both the same word. You can use the .lower() method to change all characters to lowercase.





#*********** STRINGS  ***********#

# fact = "The Moon has no atmosphere"
# print(fact)

# fact = "The moon has no atmosphere."
# fact + "No sound can be heard on the Moon."

# fact = "The moon has no atmosphere."
# fact + "No sound can be heard on the Moon."


# fact = "The moon has no atmosphere."
# fact + "No sound can be heard on the Moon."
# print(fact)


# fact = "the moon has no atmosphere."
# two_facts = fact + "No sound can be heard on the moon."
# print(two_fact)