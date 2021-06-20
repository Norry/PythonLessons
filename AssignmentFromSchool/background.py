from turtle import *

def bg(color):
  if color == 1:
    fillcolor('#ffdf6b')
  elif color == 2:
    fillcolor('#0a043c')
  elif color == 3:
    fillcolor('#a65f2b')
  penup()
  forward(190)
  left(90)
  forward(170)
  pendown()
  begin_fill()
  for i in range(4):
    circle(20, 90)
    forward(340)
  end_fill()
  penup()
  fillcolor('black')
  home()
  pendown()