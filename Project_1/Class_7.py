# Methods of list
# 1 Append
# name=["Mani","Ashish","Prasad","Chandu"]
# print(name)
# print(id(name))
# name.append(".")
# print(name)
# print(id(name))
# # Note id will not change if you appendthe list
# test="Bhagavan"
# print(list(test).count("a"))


# a=[1,2,3]
# b=[4,5,6,7]
# print(id(a))
# print(id(b))
# print(a+b)
# a.extend(b)
# print(a)
# print(b)
# print(id(a))
# print(id(b))

# a=[1,2,3]
# print(a[len(a):])
# a[len(a):]=b
# print(a)   check this

# lst=[1,2,3]
# print(lst.insert(3,"test"))
# lst[3:3]=["four"]
# print(lst)
# lst[3:3]="four"
# print(lst)

# a=[1,2,3]
# a=a.append(4)
# print(a)
# print(type(a))
# note: pop has return value but append returns none

# a=[1,2,3]
# print(a)
# print(id(a))
# print(a.pop())
# print(id(a))

#reverse a string without using reverse()
a="Bhagavan"
b=list(reversed(a))
print(''.join(b))
