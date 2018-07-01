import turtle
tur=turtle.Turtle()
tur.speed(10)
def drawSq(leng,ang):
    for i in range(4):
      tur.forward(leng)
      tur.left(ang)
AngleTur=20
for i in range(int(360/AngleTur)):
    drawSq(100,90)
    tur.left(AngleTur)

tur.left(10)
for i in range(int(360/AngleTur)):
    drawSq(100,90)
    tur.left(AngleTur)
