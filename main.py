from turtle import *

t = Turtle()
# Exercicio 1
t.forward(300)
t.stamp()
t.backward(600)
t.left(180)
t.stamp()
t.backward(300)
t.right(90)
t.forward(300)
t.stamp()
t.backward(600)
t.left(180)
t.stamp()

t.penup()
t.goto(250,200)
t.pendown()

# triangulo
color1 = textinput("Obter cor", "digite sua cor de preferência") 
t.fillcolor(color1)  
t.begin_fill()
for _ in range(3):
    t.forward(100) 
    t.left(120) 
t.end_fill()

   

t.penup()
t.goto(-250,-200)
t.pendown()

# octagono
color2 = textinput("Obter cor", "digite sua cor de preferência")
t.color("orange")
t.fillcolor(color2)
t.begin_fill()
for _ in range(4):
    t.fd(100)
    t.left(45)
    t.forward(100)
    t.left(45)
t.end_fill()
t.penup()
t.goto(250,-200)
t.pendown()

# trapezio
color3 = textinput("Obter cor", "digite sua cor de preferência")
t.fillcolor(color3)
t.begin_fill()
for _ in range(3):
    t.fd(100)
    t.left(45)
t.end_fill()


t.left(90)
t.forward(250)


t.penup()
t.goto(-250,200)
t.pendown()

# diamante
color4 = textinput("Obter cor", "digite sua cor de preferência")
t.color("pink")
t.fillcolor(color4)
t.begin_fill()
for _ in range(4):
    t.fd(100)
    t.left(90)
    t.fd(50)
t.end_fill()

mainloop()