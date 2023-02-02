import turtle as t_module
from turtle import Screen
t_module.colormode(255)
from random import choice

cat = t_module.Turtle()
cat.hideturtle()
cat.speed("fastest")
number_of_dots =100

color_list = [(240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71)]
cat.penup()
cat.setheading(255)
cat.forward(300)
cat.setheading(0)

for dot_count in range(1,number_of_dots + 1):
  cat.dot(20,choice(color_list))
  cat.forward(50)

  if dot_count % 10 == 0:
    cat.setheading(90)
    cat.forward(50)
    cat.setheading(180)
    cat.forward(500)
    cat.setheading(0)