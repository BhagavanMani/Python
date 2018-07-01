# #
#
# a={}.fromkeys('key1')
# b={}.fromkeys(['key1'])
# c={}.fromkeys(['key1','key2'],[1,2])
# d={}.fromkeys(['key1','key2'],'default')
# e={}.fromkeys(('key1','key2'),'Test')
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
#
# a={1:2,3:4}
# print(a.get(6))
# print(a.get(1,'Not Present'))
# print(a.get(6,'Not Present'))
# print(a)
#
# print(a.setdefault(6,'six'))
# print(a)
#note:iteritem method is not available in 3.6

 # print(help(iter))

 #note in dict pop argument is required
#
# b={1:2,2:3}
# print(b.pop(1))
# # print(b.pop())
#
# a={4:2,2:3,1:6,6:7}
# print(a.popitem())
# print(a)



a={1:2,3:3}
b={4:2,5:3}
c=a+b #unsupported operand type(s) for +: 'dict' and 'dict'
print(c)
