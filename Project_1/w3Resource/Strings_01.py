##01
## Write a Python program to calculate the length of a string
# str="Bhagavan"
# count=0
# for num in str:
#     count+=1
# print("Length of {0} is:{1}".format(str,count))

# def str_len(str):
#     count=0
#     for char in str:
#         count+=1
#     return count
# print(str_len("Bhagavan"))


##02
### Write a Python program to count the number of characters (character frequency) in a string.
# str="Bhagavan"
# lst=[]
# for char in str:
#     lst=lst+[char]
# myset=set(lst)
# last=[]
# for i in myset:
#     last=last+[{i:str.count(i)}]
# print(last)

# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         print(n,keys)
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(char_frequency('Bhagavan'))


# def char_count_1(str_1):
#     y={i:str_1.count(i) for i in str_1}
#     return(y)
# print(char_count_1("Bhagavan"))

##03
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. Go to the editor
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

# strng=input("Please enter your string:")
# if len(strng)>=4:
#     expRes=strng[:2]+strng[-2::]
# elif len(strng)==3:
#     expRes=strng[:2]+strng[-1]
# elif len(strng)==2:
#     expRes=strng+strng
# elif len(strng)<=1:
#     expRes="Empty String"
# print(expRes)

# def string_both_ends(str):
#   if len(str) < 2:
#     return ''
#
#   return str[0:2] + str[-2:]

##03
##  Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor
# Sample String : 'restart'
# Expected Result : 'resta$t'
# def firstOccReplace(strn,
#                     ):
#     var=strn[0]
#     str1=var
#     for char in strn[1:]:
#         if char==var:
#             char=replc
#             str1=str1+char
#         else:
#             char
#             str1=str1+char
#     return print(str1)
# firstOccReplace("BhagaBanB","$")

# mystr ="Bhagavan"
# # mystr = input('Enter a string:')
# # print(mystr[0],end='')
# print(mystr[1:].replace(mystr[0],'$'))

##04
#  Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Go to the editor
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'
# def SwapFrstTwoChar2Str(a="BhMani",b="AsWani"):
#     c=b[0:2]+a[2:]+" "+a[0:2]+b[2:]
#     return print(c)
# SwapFrstTwoChar2Str()

# str1 = 'abc'
# str2 = 'xyz'
# str3 = str1.replace(str1[0:2], str2[0:2])
# str4 = str2.replace(str2[0:2], str1[0:2])
# print(str3, str4)


## 05
## Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3,
# leave it unchanged. Go to the editor

# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

def AddING_RepLY(str1):
    if len(str1)<3:
        return str1
    elif str1[-3:]=='ing':
        str2=str1[:-3]+'ly'
        return str2
    else:
        str1=str1+"ing"
        return str1
print(AddING_RepLY("Bhsajkly"))





