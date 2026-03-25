from turtle import *
from random import randint

t = Turtle()
t.speed(5)
# plano cartesiano
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



# triangulo
def triangulo(color1,x,y,tamanho):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(color1)  
    t.begin_fill()
    for _ in range(3):
        t.forward(tamanho) 
        t.right(120) 
    t.end_fill()
    return
tamanho1 = randint(10,100)
x1 = randint(150,300)
y1 = randint(150,300)
color1 = textinput("Obter cor", "digite sua cor de preferência") 
triangulo(color1,x1,y1,tamanho1)



#octagono
def octagono(x,y,color,tamanho):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(8):
        t.fd(tamanho)
        t.right(45)
    t.end_fill()
    return
tamanho2 = randint(10,100)
x2 = randint(-300,0)
y2 = randint(200,300)
color2 = textinput("Obter cor", "digite sua cor de preferência")
octagono(x2,y2,color2,tamanho2)




# trapezio
color3 = textinput("Obter cor", "digite sua cor de preferência")
def trapezio(cor,x,y,tamanho):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(color3)
    t.begin_fill()
    for _ in range(3):
        t.fd(tamanho)
        t.right(45)
    t.end_fill()

tamanho3 = randint(10,100)
x3 = randint(150,300)
y3 = randint(-200,-100)
trapezio(color3,x3,y3,tamanho3)


# diamante
color4 = textinput("Obter cor", "digite sua cor de preferência")
def diamante(cor,x,y,tamanho):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(cor)
    t.begin_fill()
    for _ in range(4):
        t.fd(tamanho)
        t.right(90)
    t.end_fill()
tamanho4 = randint(10,100)
x4 = randint(-300,-150)
y4 = randint(-300,-150)
diamante(color4,x4,y4,tamanho4)

mainloop()