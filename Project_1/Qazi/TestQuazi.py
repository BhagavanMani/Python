str='Bhagavan | CenduitServices | Sr Software Engineer | Bhagavan | CenduitServices | Sr Software Engineer'
count=str.count('|')
print(count)
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
temp=0
for i in range(count+1):
    if temp==count:
        ind=len(str)+1
    else:
        ind=str.index('|')
    name=str[:ind]
    str=str[ind+1:].strip()
    print(name)

    temp=temp+1

