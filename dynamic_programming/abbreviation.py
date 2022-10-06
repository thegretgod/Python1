"""
https://www.hackerrank.com/challenges/abbr/problem
You can perform the following operation on some string, :

1. Capitalize zero or more of 's lowercase letters at some index i
   (i.e., make them uppercase).
2. Delete all of the remaining lowercase letters in .

Example:
a=daBcd and b="ABC"
daBcd -> capitalize a and c(dABCd) -> remove d (ABC)
"""

also want to do the same thing for LUA and eventually C#. I would like to use the same example. I used the analogy of cooking to make an intro to computer programming course, so I guess I could go with that, but I don't exactly know how I would incorporate all of the following constructs.

I could do the whole boring data base thing, but it's boring.

Currently the examples are unrelated.

Here is what I have so far:


# -*- coding: utf-8 -*-
print "Python Examples\n --By The Tutorial Doctor\n"

## PRINTING

print 'Hello'

print 'Hello','Editorial'

# Concatenate/Append text (gives errors if not strings)
print 'Hello' + 'Folks'

print 'Hello' + ' Folks' # have to add your own space

print 27


# VARIABLES
#There are different types of variables: character, string, integer, float, boolean, array/list, dictionary, and a few others.

# A character
at = "@"

# A string
name = 'Jackie'

# An integer
favorite_number = 4

# A float
height = 6.5

# A boolean
IamCool = True 

# You can assign a new value to a variable
IamCool = False 

# An array
array_of_colors = ['red','orange','yellow','green','blue','indigo','violet']
array_of_numbers = [23,13.4,1,782]
mixed_array = ['Zillow',34.9,True,798]

# A dictionary
description = {'eyeColor':'brown','physique':'muscled','demeanor':'confident'}
print description['eyeColor']
print description['physique']
print description['demeanor']

# EXTRA

# ID of a variable
print id(name)

#####

# STRINGS
# A string is string of characters 

## Empty string
first_name = ""
last_name = ""


## Asign a value to a string
first_name = "joe"
last_name = "shmo"
occupation = "Truck Driver"


## Adding strings (concatenation)
print first_name + last_name

## Adding a space between string variables
print first_name + " " + last_name

## Starting a new line (escape characters)
print first_name + "\n" + last_name 

## Adding variables inside of a string (string formatting)
print "Hello %s" %(first_name)

## Multiple variables inside of a string
print "Hello %s %s" %(first_name,last_name)

## There is another way to format strings
greeting = 'Hello {name}, my name is {myname}'
print greeting.format(name='Joseph',myname='Joey')

## Print a string several times
print first_name * 4

## Get index of a string
## Indices begin at 0
print first_name[0]
print first_name[1]
print first_name[2]

## A multi-line string
"""Multi-Line strings are sometimes used as multi-line comments, since python doesn't have syntax for multi-line comments."""


# STRING FUNCTIONS
print first_name.capitalize()
print len(occupation) 

#####

# INTEGERS
# An integer is a whole number

number1 = 12
number2 = 144
number3 = "67" #not an integer

#Add
print number1 + number2

#Subtract
print number2 - number1

#Multiply
print number1 * number2

#Divide
print number2/number1

#Exponents
print number2**number1
#Same
print pow(number2,number1)

#Square root
print number2**(1/2.0)

#Order of operations
print (number1 + number2) * 3 + (number1**3)

# Increment an integer
number1 = number1 + 1
print number1

# Convert a string to an integer
number3 = int(number3)

#####

#FLOAT
# A float is a decimal. Many of the integer operations can be applied to floats.
pi = 3.14
print pi
#####

# TUPLES
## Tuples are like lists, but cannot be changed (they are immutable).

x = 0
y = 1


## Create a Tuple
position = (50,200)


## Get tuple index
print position[x]

#####

# LISTS/Array
# Called a list in python.

# Create a list
Clients = ['Cierra','Lisa','Ibrahim','Eric','Nancy','Terry','Sarah']
print Clients

Employees = ['Eric','Margaret','Paul','Ole','Yul']
print Employees

### LIST FUNCTIONS
# List Index
print Clients[0]

# List index range
print Clients[0:4]

# Append to a list
Clients.append('Joe')
print Clients
#Same as:
#Clients[len(Clients):] = ['Joe'].

# Remove from a list
Clients.remove('Joe')
print Clients

# Insert item into a list at a location
Clients.insert(0,'Lee')
print Clients

# Reverse a list
Clients.reverse()
print Clients

# Sort a list
Clients.sort()
print Clients

# Remove an item at a location
Clients.pop(0)
print Clients

# Return the index of an item in the list
print Clients.index('Lee')

# Extend a list with another list
Clients.extend(Employees)
print Clients
# Same as:
#Clients[len(Clients):] = Clients

# Count how many times an item appears in a list
print Clients.count('Lisa')


### EXTRA

# Loop through a list
for item in Clients:
	print item
	
#Remove a list from a list
for i in Clients:
		if i in Employees:
			Clients.remove(i)
print Clients

#####

### DICTIONARIES/Associative array

# Create a dictionary (dictionary_name = {key:value})
inventory = {'light':'flashlight'}
print inventory


# Print the value of a key
print inventory['light']


# Update Dictionary 
inventory.update({'map':'New York'})
inventory.update({'phone':'Flip Phone'})
print inventory


# Update the key if it is already in the dictionary
inventory.update({'map':'Atlanta'})
inventory.update({'map':'New York'})
print inventory['map']


# Get all keys (outputs as a list)
print inventory.keys()


# Get all values (ouptuts as a list)
print inventory.values()


# Copy dictionary items as a list of tuples
# Basically converts a dictionary to a a list of tuples.  
print inventory.items()


# Length of a dictionary
print len(inventory)
def abbr(a: str, b: str) -> bool:
    """
    >>> abbr("daBcd", "ABC")
    True
    >>> abbr("dBcd", "ABC")
    False
    """
    n = len(a)
    m = len(b)
    dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(m + 1):
            if dp[i][j]:
                if j < m and a[i].upper() == b[j]:
                    dp[i + 1][j + 1] = True
                if a[i].islower():
                    dp[i + 1][j] = True
    return dp[n][m]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
