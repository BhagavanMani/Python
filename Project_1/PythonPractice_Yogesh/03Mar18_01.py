# cmp(a,b)
# if a>b return 1
# elif a<b return -1
# else a=b return 0

# coerce is function which will convert the arguments to similar datatype
# print(coerce(2,3.0))
# Note: cmp and coerce functions are not present in python 2.x
#  abs() gives absolute value of a number
print(dir(int))
print(dir(str))
print(help(str.index))
a=4
print(a.bit_length())


print (abs(-1))
print (abs(-3.6))

print(6/16,6//16, 16/6, 16//6)
print(6//16,6%16,1%16,26%100)

# HexaDecimal (16) [0 to 15]
#
# 1 - 9   10 11 12 13 14 15
# 1 - 9   A  B  C  D  E  F

print(hex(201))
#
# dec         quo     rem
# 201/16      12      9
# 12/16       0       12
#
# Hex(201)-->0x (12)9
#         ---->c9
# Hex(201)-->0x c9

print(hex(101))
print(101//16,101%16)

# dec         quo     rem
# 101/16       6       5
# 6/16         0       6
#
# Hex(101)-->0x 65

print(oct(9))

# Octacl Number(8)-- Same ass Hexa Only we need to divde with 8 instead of 16

# oct(9)
# num     quo     rem
# 9/8     1       1
# 1/8     0       1

# octal of 9 is 0o 11
