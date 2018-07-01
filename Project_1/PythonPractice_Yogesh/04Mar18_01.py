
# Count() --> ~ is method
#  |      S.count(sub[, start[, end]]) -> int
#  |      Return the number of non-overlapping occurrences of substring sub in
#  |      string S[start:end].  Optional arguments start and end are
#  |      interpreted as in slice notation.

# str='Hello World'
# # print(str.count('l'))
# # print(help(str))
# str_rev=''.join(list(reversed(str)))
# print('string reverse is {}, and type is {}'.format(str_rev,type(str_rev)))
# print(len(str),len(str_rev))
# print(str.split()) --Default delimeter is <space>


#
# srt="5+5+6+7+1+21+1"
# print(srt.split("+"))
# strJoin=srt.split("+")
# sep='+'
# print(sep.join(strJoin))



str1='Hello World'
print(len(str1))
print(str1.count('l'))
print(str1.index('l'))
print(str1.rindex('l'))
print(str1[9])

print(str1.upper())
print(str1.lower())
# find() will returns the first occurance of the string passed as argument
print(str1.find('W'))
print(str1.find('o'))

print(str1.replace('Hel','Bal'))  # Replace is not permanent effect
print(str1)


#ASCII value of given num/char  --->It takes as string
print(ord('1'))
