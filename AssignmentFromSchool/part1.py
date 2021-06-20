from turtle import *
from background import bg
shape('turtle')

speed(0)

bg(1)

# 1

penup()

forward(160)
right(90)
forward(182)
left(180)

# 2

pensize(10)
fillcolor('purple')
pendown()
begin_fill()

forward(180)
circle(5, 90)
forward(50)
circle(5, 90)
forward(180)
circle(5, 90)
forward(50)
circle(5, 90)
end_fill()

# 4
backward(3)
left(90)
forward(30)
right(90)
left(5)

fillcolor('red')
begin_fill()
# 5
forward(220)
right(5)
circle(120, 180)
forward(220)
left(90)
forward(257)
end_fill()

# 6
penup()
left(120)
forward(250)
left(30)
fillcolor('blue')
begin_fill()

# 7
pendown()
circle(150, 60)
circle(30, 120)
circle(150, 60)
circle(30, 120)
end_fill()

# 8
penup()
left(30)
forward(45)
right(30)

# 9
fillcolor('cyan')
begin_fill()
circle(100, 60)
circle(20, 120)
circle(100, 60)
circle(20, 120)
end_fill()

# 10
penup()
left(30)
forward(45)
right(30)
fillcolor('white')
begin_fill()
circle(40, 60)
circle(10, 120)
circle(40, 60)
circle(10, 120)
end_fill()

fillcolor('blue')
pencolor('blue')
right(200)
forward(70)





























