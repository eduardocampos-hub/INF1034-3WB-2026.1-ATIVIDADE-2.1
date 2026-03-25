from turtle import *

t = Turtle()

# desenhando um quadrado
def desenhaQuadrado(x,y,cor,tamanho):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.fillcolor(cor)
    t.begin_fill()
    for _ in range(4):
        t.fd(tamanho)
        t.right(90)
    t.end_fill()
    return

desenhaQuadrado(200,300,"red",200)
desenhaQuadrado(-200,-300,"green",200)
desenhaQuadrado(200,-300,"blue",100)
desenhaQuadrado(-200,300,"yellow",300)
mainloop()
