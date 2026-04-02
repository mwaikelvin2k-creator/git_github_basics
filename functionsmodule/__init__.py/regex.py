# REGEX
# This is a pattern written in special language that describes what a piece of text should look like.The developer writes the pattern then python checks if your data  matches the pattern.
# To use regex in python **import re** a built in module in python.
# There are four key functions:
# 1. re.match() - checks for a match at the beginning of a string
# 2. re.search() - searches in the string for a pattern.
# 3. re.fullmatch() - searches to see that the entire string match a pattern.
# 4. re.findall() - Finds all matches in a string.

## REGEX BUILDING BLOCKS
# They are symbols that help construct a regex pattern.
# . (wildcard) - returns any single character except the new line.
# \d (digit) - returns any digit [0-9]
# \w (word) - returns word characters (letters/digits/underscores)
# \s (white space) - return space, tab or newline
# [abc] (character class) - returns any one of a or b or c
# [a-z] (range) - returns any lowercase letter.
# [^ abc] (negated class) - returns everything except a,b and c
# ^ (start anchor) - returns start of a string.
# $ (end anchor) - returns the end of a string.
# * (Zero or more) - match the character zero or more times.
# + (one or more) - matches one or more characters.
# > (optional) - repeats previus characters zero or one time.
# {n} - Exactly n times.
# {n,m} - repeat n to m times.
# ? (optional)- makes a certain pattern optional.


import re
# Check if a string contains only digits.
pattern = r'\d+'
string1 = '2345'
string2 = 'abcsd'
string3 = 'abc123'
string4 = ''

print(re.fullmatch(pattern,string1).group(), 'True')
print(re.fullmatch(pattern,string2))
print(re.fullmatch(pattern,string3))
print(re.fullmatch(pattern,string4))


#find first phone number

import re
text = 'call us on 0712323231 or 0111323232'
pattern = r'\d{10}'

print(re.search(pattern, text))
print(re.search(pattern, text).group())
print(re.findall(pattern, text))

import re
text2 = 'call us on 0712-323-232 or 0111-323-233'
pattern = r'\d{4}-\d{3}-\d{3}'

print(re.search(pattern, text2).group())
print(re.findall(pattern, text2))

import re
text3 = ['0712345678','0723-123-456','0787 654 321','0798/673/214']
pattern = r'^07\d{2}[- /]?\d{3}[- /]?\d{3}$'
for cont in text3:
    if re.fullmatch(pattern, cont):
        print('Valid kenyan number')
    else:
        print('not a Kenyan number')

## Assignment +254 and 01
# solve the pattern below

names_list = ['Fr@ncis','st3v3','3v3','l3w1$']
pattern = r'^.{3,7}'
for name in names_list:
    if re.findall(pattern, name):
        print(name,'Valid name')
    else:
        print('Input Invalid')  
        

import re
from datetime import datetime

def validate_name(name):
    if not name:
        raise ValueError("Name cannot be empty.")
    if not re.match(r'^[A-Za-z ]+$', name):
        raise ValueError("Name can only contain letters and spaces.")

def validate_email(email):
    if not email:
        raise ValueError("Email cannot be empty.")
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        raise ValueError("Invalid email format.")

def validate_dob(dob):
    if not dob:
        raise ValueError("Date of birth cannot be empty.")
    try:
        datetime.strptime(dob, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

# Student registration
name = input("Enter your name: ")
email = input("Enter your email address: ")
dob = input("Enter your date of birth (YYYY-MM-DD): ")

try:
    validate_name(name)
    validate_email(email)
    validate_dob(dob)
    
    # If all validations pass, store the data in the database
    print("Student registration successful!")
    # Code to store the data in the database goes here
    
except ValueError as e:
    print(f"Error: {str(e)}")


