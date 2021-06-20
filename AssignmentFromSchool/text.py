from turtle import *

def M(color):
  fillcolor(color)
  begin_fill()
  pendown()
  forward(10)
  right(45)
  forward(15)
  left(90)
  forward(15)
  right(45)
  forward(10)
  right(90)
  forward(40)
  right(90)
  forward(10)
  right(90)
  forward(30)
  left(135)
  forward(15)
  right(90)
  forward(15)
  left(135)
  forward(30)
  right(90)
  forward(10)
  right(90)
  forward(40)
  right(90)
  penup()
  end_fill()

def I(color):
  fillcolor(color)
  begin_fill()
  pendown()
  for i in range(2):
    forward(10)
    right(90)
    forward(40)
    right(90)
  penup()
  end_fill()
  
def N(color):
  fillcolor(color)
  begin_fill()
  pendown()
  forward(10)
  right(60)
  forward(22.5)
  left(150)
  forward(20)
  right(90)
  forward(10)
  right(90)
  forward(40)
  right(90)
  forward(10)
  right(60)
  forward(22.5)
  left(150)
  forward(20)
  right(90)
  forward(10)
  right(90)
  forward(40)
  right(90)
  penup()
  end_fill()

def E(color):
  fillcolor(color)
  begin_fill()
  pendown()
  forward(20)
  for i in range(2):
    right(90)
    forward(8)
    right(90)
    forward(10)
    left(90)
    forward(8)
    left(90)
    forward(10)
  right(90)
  forward(8)
  right(90)
  forward(20)
  right(90)
  forward(40)
  right(90)
  penup()
  end_fill()

def C(color):
  fillcolor(color)
  begin_fill()
  pendown()
  forward(20)
  right(90)
  forward(10)
  right(90)
  forward(10)
  left(90)
  forward(20)
  left(90)
  forward(10)
  right(90)
  forward(10)
  right(90)
  forward(20)
  right(90)
  forward(40)
  right(90)
  penup()
  end_fill()

def R(color):
  fillcolor(color)
  begin_fill()
  pendown()
  forward(30)
  right(90)
  forward(20)
  right(90)
  forward(10)
  left(135)
  forward(15)
  right(45)
  forward(10)
  right(90)
  forward(10)
  right(90)
  forward(10)
  left(45)
  forward(15)
  left(135)
  forward(20)
  right(90)
  forward(10)
  right(90)
  forward(40)
  penup()
  end_fill()
  
  right(120)
  forward(12)
  left(30)
  
  fillcolor('#a65f2b')
  begin_fill()
  pendown()
  for i in range(4):
    forward(10)
    right(90)
  penup()
  end_fill()
  
  left(150)
  forward(12)
  right(150)

def A(color):
  fillcolor(color)
  begin_fill()
  pendown()
  forward(30)
  right(90)
  forward(40)
  right(90)
  forward(10)
  right(90)
  forward(15)
  left(90)
  forward(10)
  left(90)
  forward(15)
  right(90)
  forward(10)
  right(90)
  forward(40)
  penup()
  end_fill()
  
  right(120)
  forward(12)
  left(30)
  
  fillcolor('#a65f2b')
  begin_fill()
  pendown()
  for i in range(4):
    forward(10)
    right(90)
  penup()
  end_fill()
  
  left(150)
  forward(12)
  right(150)

def F(color):
  fillcolor(color)
  begin_fill()
  pendown()
  forward(10)
  for i in range(2):
    forward(10)
    right(90)
    forward(8)
    right(90)
    forward(10)
    left(90)
    forward(8)
    left(90)
  right(90)
  forward(8)
  right(90)
  forward(10)
  right(90)
  forward(40)
  right(90)
  penup()
  end_fill()

def T(color):
  fillcolor(color)
  begin_fill()
  pendown()
  forward(30)
  right(90)
  forward(10)
  right(90)
  forward(10)
  left(90)
  forward(30)
  right(90)
  forward(10)
  right(90)
  forward(30)
  left(90)
  forward(10)
  right(90)
  forward(10)
  right(90)
  penup()
  end_fill()