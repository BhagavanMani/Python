d1=dict()
d2=dict(age=10,name='Harsha')
d3=dict({1:'One',2:'Two',3:'Three'})
# d4=dict(age=10,name='Harsha',{1:'One',2:'Two'})
d4=dict({1:'One',2:'Two',3:'Three'},age=10,name='Harsha')

#Tuple of two item list
d5=dict(([1,'One'],[2,'Two'],[3,'Three']))
d6=dict(([1,'One'],[2,'Two'],[3,'Three']),age=10,name='Harsha')

#List of two item list
d7=dict([[1,'One'],[2,'Two'],[3,'Three']])
d8=dict([(1,'One'),(2,'Two'),(3,'Three')])
d9=dict([[1,'One'],[2,'Two'],[3,'Three']],age=10,name='Harsha')

#Tuple of two character string
d10=dict(('ab','cd','ef'))


#List of two character string
d11=dict(['ab','cd','ef'])
print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
print(d6)
print(d7)
print(d8)
print(d9)
print(d10)
print(d11)

