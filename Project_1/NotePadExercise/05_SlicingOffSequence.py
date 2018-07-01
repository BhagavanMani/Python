#Slicing of sequence

s='Bhagavan Mani'
# print s[:]		#Bhagavan Mani
# print s[2:] 	#agavan Mani
# print s[:4]		#Bhag
# print s[::]		#Bhagavan Mani
# print s[::4]	#B---a--- ---i-->Ba i
# print s[4::]	#avan Mani
# print s[::2]	#B-a-a-a- -a-i -->Baaa ai
# print s[2::]	#agavan Mani
# print s[::-1]	#inaM navagahB
# print s[::-2]	#i-a- -a-a-a-B--> ia aaaB #as simple as reverse of s[::2]
# print s[:3]+s[3:] #==s
# print s[2:6] 	#agav
# print s[2:6:1]	#agav
# print s[2:6:-1] # ''
# print s[6:2:-1] #avag
# print s[2:6:2] 	#aa
# print s[6:2:-2]	#aa
# print s[4::2]	#aa ai



# print s[4::-1]	#End Index Dafaluts begining of the string
# #agahB
# print s[:4:-1] 	#Begining Index defaults to the end of the string
# #inaM nav

# print s[2:4]
# s[2:4]='ax'
# n=range(5)
# print n[1:3]
# n[1:3]=[6,7]
# print n
# n[::2]=[-1,-3,-5]
# print n
# n[::2]=[0,1,2,3,] #throws error

a=range(4)
s=['Bhagavan','Mani','Honey','Bhagavan']
s1="Bhagavan"
# print a[::2]
# del a[::2]
# print a








