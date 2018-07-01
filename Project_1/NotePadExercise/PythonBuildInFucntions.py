##Source : https://www.programiz.com/python-programming/methods/built-in/


#1) abs(): abs(num)
'''The abs() method returns the absolute value of the given number. If the number is a complex number, abs() returns its magnitude.'''
# random integer
integer = -20
print('Absolute value of -20 is:', abs(integer))

#random floating number
floating = -30.33
print('Absolute value of -30.33 is:', abs(floating))

complex = (3 - 4j)
print('Magnitude of 3 - 4j is:', abs(complex))

##################################################################

# 2) any() : any(iterable)
'''The any() method returns True if any element of an iterable is true. If not, this method returns False.'''
##It works similarlily with List,tuple and sets
l = [1, 3, 4, 0]
print(any(l))

l = [0, False]
print(any(l))

l = [0, False, 5]
print(any(l))

l = []
print(any(l))

# Strings work on below way
s = "This is good"
print(any(s))

# 0 is False
# '0' is True
s = '000'
print(any(s))

s = ''
print(any(s))

#Dict works on below way
d = {0: 'False'}
print(any(d))

d = {0: 'False', 1: 'True'}
print(any(d))

d = {0: 'False', False: 0}
print(any(d))

d = {}
print(any(d))

# 0 is False
# '0' is True
d = {'0': 'False'}
print(any(d))


##################################################################
## 3) ll(): all(iterable)
'''The all() method returns True when all elements in the given iterable are true. If not, it returns False.'''

#Note: In all() empty return TRUE.

##################################################################
## 4) ascii() : ascii(object)
'''The ascii() method returns a string containing a printable representation of an object. It escapes the non-ASCII characters in the string using \x, \u or \U escapes.'''

normalText = 'Python is interesting'
print(ascii(normalText))

otherText = 'Pythön is interesting'
print(ascii(otherText))

print('Pyth\xf6n is interesting')

randomList = ['Python', 'Pythön', 5]
print(ascii(randomList))
