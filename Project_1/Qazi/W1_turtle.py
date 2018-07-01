# # print(7/2)
# # print(7%2)
# # print(7//2)
#
#
# import turtle
# # turtleVar=turtle.Turtle()
# # turtleVar.forward(90)
# # turtleVar.left(90)
# # turtleVar.forward(90)
# # turtleVar.left(90)
# # turtleVar.forward(90)
# # turtleVar.left(90)
# # turtleVar.forward(90)
# #
# # print(turtleVar)
#
# tur=turtle.Turtle()
# def tur_fun(len):
#     tur.forward(len)
#     tur.left(90)
#     tur.forward(len)
#     tur.left(90)
#     tur.forward(len)
#     tur.left(90)
#     tur.forward(len)
#     tur.left(90)
#     return tur
#
#
#
#
# import turtle
# tur=turtle.Turtle()
#
# #full lenght sq
# def tur_fun(len):
#     tur.forward(len)
#     tur.left(90)
#     tur.forward(len)
#     tur.left(90)
#     tur.forward(len)
#     tur.left(90)
#     tur.forward(len)
#     tur.left(90)
#
# #making four box out of full lenght
# def tur_innrFn(num):
#   # tur_fun(num)
#   tur.forward(num/2)
#   tur.left(90)
#   tur.forward(num)
#   tur.left(90)
#   tur.forward(num/2)
#   tur.left(90)
#   tur.forward(num/2)
#   tur.left(90)
#   tur.forward(num)
#   tur.right(90)
#   tur.forward(num/2)
#   tur.right(90)
#   # tur.left(180)
#
# def tur_innerFour(num):
#   num=num/2
#   tur_innrFn(num)
#   tur.forward(num)
#   tur.left(180)
#
#
# def tur_lastFour(num):
#   tur_innerFour(num)
#   tur.forward(num/2)
#   tur_innerFour(num)
#   tur.left(90)
#   tur.forward(num/2)
#   tur_innerFour(num)
#   tur.right(90)
#   tur_innerFour(num)
#   tur.right(90)
#   tur.forward(num/2)
#   tur.right(90)
#   tur.forward(num/2)
#   tur.right(180)
#
#
# num=200
# tur_fun(num)  #full sq
# tur_innrFn(num) #make inner 4 sq
# tur.forward(num)
# tur.left(180)
# tur_lastFour(num)
#
# num=num/2
# tur_lastFour(num)
# tur.forward(num)
# tur_lastFour(num)
# tur.left(90)
# tur.forward(num)
# tur.right(90)
# tur_lastFour(num)
#
# tur.right(180)
# tur.forward(num)
# tur.left(180)
# tur_lastFour(num)
#
#
# num=100
# while num >=0:
#     if num!=0:
#         print(num)
#     else:
#         print("Boom!!")
#     num-=1


import turtle
tur=turtle.Turtle()
tur.speed(20)
TotalLen=190

box_len=10 #Always Even and shoule be div by TotalLen
box_wid=5  #Always Even and shoule be div by TotalLen
i=0
j=1
def tur_Square_Box(len,var):
  for i in range(len):
    if i%2==var:
      tur.forward(TotalLen)
      tur.left(90)
      tur.forward(TotalLen/len)
      tur.left(90)
    else:
      tur.forward(TotalLen)
      tur.right(90)
      tur.forward(TotalLen/len)
      tur.right(90)
  tur.forward(TotalLen)
  tur.right(90)
tur_Square_Box(box_len,i)
tur_Square_Box(box_wid,j)


