#########STRINGS#######

#A sstr values is a string of zero or more 8 bit character
#A unicode value is a sting of zero or more 32 bit unicode characters

'''
most unicode literals are similar or identical except that unicode literals are preceded
with letters u for Ex:
'abc' is type int
u'abc' is type unicode
'''

# print (type ("abc"))
# print (type (u"abc"))
# print (chr(97))
# print (ord('A'))

''' 
\b removes one char before (8 bit)
 \t for tab space (9 bit)
 \" for double quote in a string (34 bit)
 \' for single quote in a string (39 bit)
 \\ for \ in a string (92)
'''
#
# print ("Bhagavan\bMani")
# print ('Bhagavan\tMani')
# print ('Bhagavan\"Mani')
# print ('Bhagavan\'Mani')
# print ('Bhagavan\\Mani')
#
str="BhagavanMani"
print(str)
# print (len (str))
# print (str.center(25))
# print (str.center(25).index('B'))
# print (len(str.center(25)))
# print (str.center(5))
# print (len(str.center(5)))
#
# # ljust/rjust is  string method to adjust the length of string by filling with white spaces
# #they will never return shorter string . If length isn't enough, it just retuns the original value
# print (str.rjust(50))
# print (str.ljust(50))
# strTab='     '+str+'        ' #5+str+8
# print (strTab)
# print (len(strTab))
# '''
# strip/lstrip/lstrip removes leading or trailing white spaces
# '''
# print (strTab.rstrip())
# print (strTab.lstrip())
# print (len(strTab.rstrip()))
# print (len(strTab.lstrip()))
# print (strTab.strip())
# print (len(strTab.strip()))

'''
count(...) method of builtins.str instance
    S.count(sub[, start[, end]]) -> int
>>Return the number of non-overlapping occurrences of substring sub in
  string
'''

i=10
print(str.count('a'))#always takes string as variable
# print (str.count(i))
# print(help(str.count))
print(str.count('an'))
print(str.count('an',1,9))
print(str.index(('a')))
print(str.rindex('a'))

#find(), rfind() locate a string with in a string. If it didn find the match it returns -1
#>>find() will find the first occurance of given substring from the BEGINING
#>>rfind() will find the first occurance of given substring from the END
'''
find(...) method of builtins.str instance
    S.find(sub[, start[, end]]) -> int
'''
# print(help(str.find))
# print (str.find('a'))
# print (str.rfind('a'))

str1='Hello Mr.X'
print(str1.replace('Hello','Hi'))
print(str1)

# t=('i',)
# print (type(t))
# print (str.startswith('B'))
# print (str.startswith('b'))
# print (str.startswith(u'B'))
# print (str.endswith(u'B'))
# print (str.endswith(t))

k=123
# print (str.lower())
# print (str.upper())
# # print (k.upper())

str1='Bhagavan143Mani'
# k='1234'
# print (str.isalpha())
# print (str1.isalpha())
# print (str.isupper())
# print (str.islower())
# print (str1.upper().isupper())
# print (str.lower().islower())
# print (k.isdigit())
# print(str1.isdigit())

line=" 1.4 ,8.6 ,-3.30 4.29, 124"
# print (help(str.split))
'''
split(...) method of builtins.str instance
    S.split(sep=None, maxsplit=-1) -> list of strings
'''
# print (line.split())
# print (line.split(','))
# print (line.split(',',1))
# print (line.split(',',2))

# str='B,H,A,G,A,V,A,N'
# print(str.split(',',2))
# print(str.rsplit(',',2))


#Strings dont have del method


#JOIN method is to join the elements of a list with given separator

lst=['B','h','a','g','a','v','a','n']
str_fromList=''.join(lst)
print(str_fromList)
# print(str_fromList.split(','))
# str_fromList=''.join(lst)
# print(str_fromList)
# test=[]
# for i in str_fromList:
#     test.append(i)
# print(test)
