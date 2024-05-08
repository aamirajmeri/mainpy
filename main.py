# num_char = len(input("What's your name ?"))
# #print(type(num_char))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")




#******** DAY - 2 *********#
# street_name = "Abbey Road"
# print(street_name[4] + street_name[7])

# a = int(848)
# print(type(a))

# print(80 + float(111.5))
# print(str(80) + str(100))

# result = 4 / 8
# result /= 8
# print(result)

# x = int(input("Enter your name"))
# print(type(x))



# The preceding code trusts that everything after the colon (:) is a temperature. The string is split at :, which produces a list of two items. Using [-1] on the list returns the last item, which is the temperature in this example.
# If the text is irregular, you can't use the same splitting methods to get the value. You must loop over the items and check to see whether the values are of a certain type. Python has methods that help check the type of string:



# mars_temperature = "The highest temperature on Mars is about 30 C"
# for item in mars_temperature.split():
#     if item.isnumeric():
#         print(item)