# lst=['bhavavan','Ashish','Chandu']
# print(lst)
# copy_list_1=lst
# copy_lst=lst[:]  #shallow copy
# print(copy_list_1)
# print(copy_lst)
# print(id(lst))
# print(id(copy_list_1))
# print(id(copy_lst))
from copy import deepcopy
a=[1,2,[3]]
b=a
c=a[:]
d=deepcopy(a)
e=deepcopy(b)
f=deepcopy(a[:])


print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
print(id(f))
print(id(a[2]))
print(id(b[2]))
print(id(c[2]))
print(id(d[2]))
print(id(e[2]))
print(id(f[2]))
print(id(a[0]))
print(id(b[0]))
print(id(c[0]))
print(id(d[0]))
print(id(e[0]))
print(id(f[0]))

# a[2]=15
#
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))
# print(id(e))
# print(id(f))
# print(id(a[2]))
# print(id(b[2]))
# print(id(c[2]))
# print(id(d[2]))
# print(id(e[2]))
# print(id(f[2]))


lst=[1,2,3]
print(lst*4)
print([lst]*4)

print(lst)
print([lst])
