# # The prime factors of 13195 are 5, 7, 13 and 29.
# #
# # What is the largest prime factor of the number 600851475143 ?
#
num=600851475143;div=3
var2=""
while num%2==0:
    num=num/2
    var2=var2+",2"
while div<=num:
    if num%div==0:
        var2=var2+","+str(div)
        num=num/div
    div=div+2
if var2[0]==',':
    var2=var2[1:-1]
print(var2)


# from math import sqrt
#
# primes = set([2])
# value = 3
# number = 317584931803
# while value < sqrt(number):
#     isPrime = True
#     for k in primes:
#         if value % k == 0:
#             isPrime = False
#             value += 2
#     if isPrime:
#         primes.add(value)
#         if number % value == 0:
#             print (value)
#             number /= value
# print (number)
