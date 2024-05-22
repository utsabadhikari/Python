# Python can be used to convert the tye of variables 
"""
int() = for conversion of string to a integer
float() = for conversion of string to flaot 
bool() =for conversion of string to boolean value
"""

# Type conversion in Python:To find your age 
year = int(input("Please input your birth year:\n"))
age = 2024- int(year)
print("Your are " + str(age) + " years old.")

"""
In Formatted string form.The following rogram can be written as:

year = int(input("Please input your birth year:\n"))
age = 2024- int(year)
print(f"You are {age} years old.")

In the above formatted string version of the program "f" is used to define a formatted string prefix in a string .
we use"{}"to dynamically insert values into your string. 
"""
