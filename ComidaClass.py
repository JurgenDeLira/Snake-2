import turtle
import random

class Comida:
    def __init__(self, colorComida, screen):
        self.comida = turtle.Turtle()
        self.comida.speed(0)
        self.comida.shape("circle")
        self.comida.color(colorComida)
        self.comida.penup()

        self.comida.goto(0,40)
        self.lado = screen.lado

    def alColisionar(self, serpiente, game):
        if serpiente.cabeza.distance(self.comida) < 20:
            condicion = True

            while condicion:
                x = (random.randint(0,19)*20-(self.lado/2)) 
                y =   (random.randint(0, 19)*20)-(self.lado/2) 
                if len(serpiente.segmentos)> 0:
                    for seg in serpiente.segmentos:
                        if x == seg.xcor() and y == seg.ycor():
                            condicion = True
                            break
                        else:
                            condicion = False
                else:
                    condicion = False
            
            self.comida.goto(x,y)
            game.actualizarPuntaje(10)
            serpiente.agregarSegmentos()
            return True
        else:
            return False

    def resetearComida(self):
        self.comida.goto(0,40)






    

