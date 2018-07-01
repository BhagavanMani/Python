#50 :Write a Python program to split a string on the last occurrence of the delimiter.
# I/p: 'B,H,A,G,A,V,A,N'
#
# O/P: 'B,A,G,V,A,N','A','N'

# str='B,H,A,G,A,V,A,N'
# print(str.rsplit(',',2))
# print(str.rfind(','))


#49Count and display the vowels of a given text

# vowels='aeiouAEIOU'

# def print_vowels(str):
#     strng=''
#     # vowels_len=((j for j in vowels)for i in str)
#     for i in str:
#         if i in vowels:
#             strng=strng+i
#     return strng
# print(print_vowels('aeiourajkldjsqjfsaio'))

# def print_vowels1(str='aeiourajkldjsqjfsaio'):
#     var=[i for i in str if i in vowels]
#     return  var
# print(print_vowels1())

# print(print_vowels1('aeiourajkldjsqjfsaio'))


#48 Swap comma and dot in a string
# amount = "32.054,23"
# var = amount.maketrans
# print(help(amount.maketrans))
# amount = amount.translate(var(',.', '.,'))
# print(amount)

#47 Write a Python program to lowercase first n characters in a string
# str='BHBSKJHSH'
# n=4
# print(str[:n].lower()+str[n:])


#46 Write a Python program to convert a string in a list
# str='bhcsakbs'
# sep=','
# var=sep.join(str)
# print(var.replace(',',''),type(var))

#45 Write a Python program to check if a string contains all letters of the alphabet.

#44 Write a Python program to check if a string contains all letters of the alphabet.
str='The quick brown fox jumps over the lazy dog'

# str=str.replace(' ','').lower()
# print(str)
# lst=[i for i in str ]
# lst1={i for i in str}
# print(sorted(lst1))
# print(len(lst),len(lst1))
# print(lst)

#43 Write a Python program to print the index of the character in a string. Go to the editor
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2
# str='hdquihqhfqhflkjfkejoifoifr4ohfjhe'
# print(len(str))
# for i,j in enumerate(str):
#     print('current character is {} position is {}'.format(j,i))


#42 Write apython program to count repeated characters in a string. Go to the editor
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2
str='thequickbrownfoxjumpsoverthelazydog'
dict={}
for i in set(str):
    dict[i]=str.count(i)
print(dict)
