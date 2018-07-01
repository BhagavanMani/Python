# from test import char_count
# # print(char_count("Bhagavan"))
# print(char_count("Bhagavan"))


# x = "google.com"
# y = {i:x.count(i) for i in x}
# print(y)
# lst=[1,2,3,4,5]
# lst.insert(0 , 0)
# print(lst)

# lc_test=[ i  for i in range (1,100) if i%5==0 if i%7==0]
#
# print(lc_test)
# var1=[]
# for i in range(3):
#     var2=[]
#     for j in range(3):
#         var2.append((i,j))
#     var1.append(var2)
# print(var1)
# col=4;row=4
# var1=[]
# var2=[]
# lc_mat=[var1.append(var2.append((i+1,j+1))) for j in range(col) for i in range(row)]
# print(var2)
# def mat_2d():
#     var1=[]
#     for i in range(3):
#         var2=[]
#         for j in range(3):
#             var2.append((i,j))
#         var1.append(var2)
#     return var1
# # print(mat_2d())
#
# lst=[[(i,j)for j in range(4)]for i in range(3)]
# print(lst)
#
# print(dir(lst))

# import  pdb
# # lst="bhaagavan"
# pdb.set_trace()
# for i in lst:
#     print(i)
# def transmit_to_space(message):
#     "This is the enclosing function"
#     print("I am here 1")
#     def data_transmitter():
#         "The nested function"
#         print("I am here 2")
#         print(message)
#     print("I am here 3")
#     data_transmitter()
#     print("I am here 4")
#
# import  pdb
# # lst="bhaagavan"
# pdb.set_trace()
# print(transmit_to_space("Test message"))

# def print_msg(msg):
# # This is the outer enclosing function
#
#     def printer():
# # This is the nested function
#         print(msg)
#
#     printer()
#
# # We execute the function
# # Output: Hello
# print_msg("Hello")
import  pdb
def print_msg(msg):
# This is the outer enclosing function
    print("I am here 1")
    def printer():
        print("I am here 2")
# This is the nested function
        print(msg)
    print("I am here 3")
    return printer  # this got changed
    print("I am here 4")
# Now let's try calling this function.
# Output: Hello
pdb.set_trace()
another = print_msg("Hello") #printer()
# print("I am here 5")
# del print_msg
# # print(print_msg("Hello"))
another()

# print (dir(pdb))
# print("I am here 6")

