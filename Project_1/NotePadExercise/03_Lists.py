###########LISTS######
lst=[]
for i in range(6):
    lst.append(i)
print(lst)

lst1=[]
for i in "BhagavanMani":
    # lst1.append(i)
    lst1.insert(len(lst1),i)
print(lst1)
print(enumerate(lst))
print(list(enumerate(lst)))

for ind,val in enumerate(lst1,start=3):
    print("Index is {}, Values is {}".format(ind,val))

# print(min(lst),max(lst),sum(lst))
# print(min(lst1),max(lst1))
# print(len(lst),len(lst1))
#
# print(lst1.index('M'))

# print(2 in lst, 12 in lst)
# print(2 not in lst, 12 not in lst)

# print(lst+lst1)
# print(lst1+lst)


#append() will always append at last position
#insert(P,V) to insert a single vallue into arbitary position we use this method, here V can a list, it iwll create list comprehension
#intead of having list inside list we can use extend to add one list elements into others
# lst.extend(lst1)
# print(lst)
# lst.insert(-1,lst1)
# print(lst)

# # print(lst.index(lst1))
# # print(lst1.count('a'),lst1.count('an'))
# lst[-2]=[1,2,3,12,13]
# lst[-1]=[1,2,3,12,13]
# del lst[0:2]
# print(lst)

#remove(V) removes the FIRST element of list, if there is one
# lst.remove(lst1)
# print(lst)
# lst.remove([1,2,3,12,13])
# print(lst)
# print(lst1 in lst)
# lst.remove(lst1)
# print(lst)

# poped=lst.pop()
# print(poped,lst)
# poped=lst1.pop(1)
# print(poped,lst1)


# lst2=[1,2,3,1,3,5,7,7,8]
# print(lst2)
# lst2.sort()
# print(lst2)
# # lst2.sort(reverse=1)
# lst2.sort(reverse=True)
# print(lst2)
lst.reverse()
print(lst)
lst1.reverse()
print(lst1)

#sort will sort 1st caps next small
#to sort or reverse permanently
# lst3=['a','vdhj','C','a' ,'a','vdhj','c','a']
# # print(lst3)
# lst3.sort()
# print(lst3)
# lst3.sort(reverse=1)
# print(lst3)
#
# lst_rev=reversed(lst)
# lst1_rev=reversed(lst1)
# print(lst_rev)
# print(lst1_rev)
#
# lst_sort=sorted(lst)
# lst1_sort=sorted(lst1)
# print(lst_sort)
# print(lst1_sort)



# lst4=[1,2,3,1,3,5,7,7,8,'a','vdhj','c','a']


# lst=['B','h','a','g','a','v','a','n']
# str_fromList=','.join(lst)
# print(str_fromList)
# str_fromList=''.join(lst)
# print(str_fromList)
