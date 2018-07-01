# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

i=1
num=999
sum3=0
sum5=0
sum35=0
while(i<=num):
    if(i%3==0):
        sum3=sum3+i
    if(i%5==0):
        sum5=sum5+i
    if(i%5==0 and i%3==0):
        sum35=sum35+i
    i=i+1
sum=sum3+sum5-sum35
print(sum3,sum5,sum35,sum)

# print(10//3)
sumAdd=0
sumSub=0
for i in range(1000):
    if i%3==0 or i%5==0:
        sumAdd+=i
        # print(sumAdd)

print(sumAdd)







