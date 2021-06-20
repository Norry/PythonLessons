from turtle import *
from background import bg
shape('turtle')
speed(0)
bg(2)

# магический цвет - '#0a043c'

# 1
penup()
right(90)
forward(75)
left(90)
# 2
pencolor('white')
fillcolor('cyan')
pensize(3)
begin_fill()
# 3
pendown()
circle(75)
penup()
left(90)
forward(15)
right(90)
pendown()
circle(60, -360)
end_fill()
penup()
home()
pendown()
def part():
  pencolor('blue')
  fillcolor('cyan')
  begin_fill()
  forward(27)
  right(90)
  circle(50, 170)
  circle(50, -20)
  left(10)
  circle(80, -70)
  left(30)
  left(30)
  circle(80, -70)
  left(10)
  circle(50, -20)
  circle(50, 170)
  right(90)
  forward(27)
  end_fill()
speed(6)
right(30)
part()
left(60)
part()
left(60)
part()



























































