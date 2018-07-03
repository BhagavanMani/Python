stn='Bhagavan | CenduitServices | Sr Software Engineer | Bhagavan | CenduitServices | Sr Software Engineer'
# count=str.count('|')
# print(count)
#Bhagavan
# ind=str.index('|')
# name=str[:ind]
# print(name)
#
# str=str[ind+1:].strip()
# ind=str.index('|')
# name=str[:ind]
# print(name)
#
# str=str[ind+1:].strip()
# ind=len(str)+1
# name=str[:ind]
# print(name)

def splitToDiffWords(str, delm, pos=0):
    ''' This function will skip the delimiter value'''
    temp = 0
    count = str.count(delm)
    lst = []
    if pos > 0:
        str = str[pos:]
    if delm in str:
        for i in range(count + 1):
            if temp == count:
                ind = len(str) + len(delm)
            else:
                ind = str.index(delm)
            name = str[:ind]
            str = str[ind + len(delm):].strip()
            if name.strip()!='':
              lst.append(name)
            temp = temp + 1
        return lst
    else:
        return 'Passed delimiter is not present in the given string'

stn = 'Bhagavan | Cenduit | Sr Software Engineer | Bhoom | Bhoommm | Bhoooommmmmmm...!!'
# print(splitToDiffWords(stn, '|'))
print(splitToDiffWords(stn, 'om'))


