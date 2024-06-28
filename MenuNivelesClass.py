import turtle
from ScrfeenClass import Scrfeen

class MenuNiveles:

    def __init__(self, scrfeen,backMethod, initGameMethod):
        self.pantalla = scrfeen.ventana
        self.screen = scrfeen

        self.niveles = ["Fácil", "Normal", "Dificil"]

        self.nivel_seleccionada = None
        self.nivel_actual = 0

        self.backMethod = backMethod
        self.initGameMethod = initGameMethod

        self.titulo = turtle.Turtle()
        self.titulo.speed(0)
        self.titulo.color("white")
        self.titulo.penup()
        self.titulo.goto(0,250)

        self.titulo.write("Menú niveles", align = "center", font = ("Courier",36, "bold"))
        self.titulo.hideturtle()


        self.texto_nivel = turtle.Turtle()
        self.texto_nivel.speed(0)
        self.texto_nivel.color("white")
        self.texto_nivel.penup()
        self.texto_nivel.goto(0,210)

        self.texto_nivel.write("Selecciona el nivel del juego", align = "center", font = ("Courier",24, "normal"))
        self.texto_nivel.hideturtle()
        self.agregar_boton_atras()

        self.botones = []

        for i, opcion in enumerate(self.niveles):
            boton = turtle.Turtle()
            boton.speed(0)
            boton.color("white")
            boton.penup()
            boton.goto(0, i * -100)
            boton.write(opcion, align = "center", font = ("Courier", 24, "normal"))
            boton.hideturtle()
            self.botones.append(boton)
        self.selector = turtle.Turtle()
        self.selector.speed(0)
        self.selector.color("yellow")
        self.selector.penup()
        self.selector.shape("square")
        self.selector.shapesize( stretch_wid=1, stretch_len=5)
        self.actualizar_selector()
        self.pantalla.listen()

        self.pantalla.onkeypress(self.mover_arriba, "Up")
        self.pantalla.onkeypress(self.mover_abajo, "Down")
        self.pantalla.onkeypress(self.cambiar_nivel, "Return")
        self.pantalla.onscreenclick(self.ir_atras, btn = 1)


        

        







        turtle.mainloop()
    def agregar_boton_atras(self):
        boton_atras = turtle.Turtle()
        boton_atras.speed(0)
        boton_atras.color("white")
        boton_atras.penup()
        boton_atras.goto(-260,260)
        boton_atras.write("<", align= "center", font = ("Courier",24, "normal") )
        boton_atras.hideturtle()
    def actualizar_selector(self):
        self.selector.goto(self.botones[self.nivel_actual].xcor(), self.botones[self.nivel_actual].ycor()-10)
        print("Nivel actual:", self.niveles[self.nivel_actual])
    def mover_arriba(self):
        if self.nivel_actual > 0:
            self.nivel_actual -= 1
            self.actualizar_selector()
    def mover_abajo(self):
        if self.nivel_actual < len(self.niveles)-1:
            self.nivel_actual += 1
            self.actualizar_selector()
    def cambiar_nivel(self):
        self.nivel_seleccionada = self.niveles[self.nivel_actual]
        self.pantalla.clear()
        if self.nivel_seleccionada.lower() == "fácil":
            self.initGameMethod(0.3)
        elif self.nivel_seleccionada.lower() == "normal":
            self.initGameMethod(0.2)
        elif self.nivel_seleccionada.lower() == "dificil":
            self.initGameMethod(0.1)
        else:
            self.initGameMethod(0.2)
    def ir_atras(self, x,y):
        if -270 <x<-250 and 250 < y <280:
            self.pantalla.clear()
            return self.backMethod()




######## código de ejemplo     

def initGame(delay):
    print("init ", delay)

def backMethod():
    print("back")





#ventana = Scrfeen(600, 600, "Juego de Snake", "black")
#menu = MenuNiveles(ventana,backMethod, initGame)

       
