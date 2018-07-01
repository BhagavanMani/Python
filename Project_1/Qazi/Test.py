import turtle
tur=turtle.Turtle()
tur.speed(5)
TotalLen=160

box_len=10

def tur_Square_Box(len):
  for i in range(len):
    if i%2==0:
      tur.forward(TotalLen)
      tur.left(90)
      tur.forward(TotalLen/len)
      tur.left(90)
    elif i==len-1:
      tur.forward(TotalLen)
      tur.left(90)
    else:
      tur.forward(TotalLen)
      tur.right(90)
      tur.forward(TotalLen/len)
      tur.right(90)
  

tur_Square_Box(box_len)
tur_Square_Box(box_len)
