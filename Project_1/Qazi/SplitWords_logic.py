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


def splitToDiffWords(str,delm,pos=0):
    temp=0
    count=str.count(delm)
    lst=[]
    if pos>0:
        str=str[pos:]
    for i in range(count+1):
        if temp==count:
            ind=len(str)+1
        else:
            ind=str.index(delm)
        name=str[:ind]
        str=str[ind+1:].strip()
        lst.append(name)
        temp=temp+1
    return lst
print(splitToDiffWords(stn,'|',5))



