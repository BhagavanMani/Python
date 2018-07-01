#04012018

import sys
# for i in sys.path:
#     print (i)
# print(help((sys)))

#
# #Number to binary
# Down to up
#
# Num/2       Quo      Rem
# 21/2        10       1
# 10/2        5        0
# 5/2         2        1
# 2/2         1        0
# 1/2         0        1
#
# 8/2         4        0
# 4/2         2        0
# 2/2         1        0
# 1/2         0        1
#
# Binary of 21 is   1 0 1 0 1
# Binary of 8 is    0 1 0 0 0
#
# 21 & 8            0 0 0 0 0

# Binary to Num      0*2^4+0*2^3+0*2^2+0*2^1+0*2^0
#                     0+0+0+0+0  =0
#
# print (21 & 8)
#
# #Binary to Number
#
# 2/2         1       0
# 1/2         0       1
#
#
# 3/2         1       1
# 1/2         0       1
#
# Binary of 2 is    1       0
# Binary of 3 is    1       1
#
#  2& 3             1       0
# Number for 1 0 is ---> 1*2^1+0*2^0=2+0=2
#
# 2|3               1       1
# Number for 1 1 is---> 1*2^1+1*2^0=2+1=3

print(8<<1)
# Binary of 8 is   0 1 0 0 0
#  8<<1 shifts by 1 digit -->  1 0 0 0 0
# Now number for the above biary is  1*2^4+0+0+0+0= 16

print (8<<2)

# It shifts all binary code by 2 digits left
