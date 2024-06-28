import turtle
from ScrfeenClass import Scrfeen
import webbrowser

class AcercaDe:
    def __init__(self, scrfeen, backMethod):
        self.screen = scrfeen
        self.backMethod = backMethod

        self.titulo = turtle.Turtle()
        self.titulo.speed(0)
        self.titulo.color("white")
        self.titulo.penup()
        self.titulo.goto(0,250)

        self.titulo.write("Acerca De", align = "center", font = ("Courier",36, "bold"))
        self.titulo.hideturtle()
        self.agregar_boton_atras()
        self.screen.ventana.onscreenclick(self.ir_atras, btn = 1)

        content_text = ("Sumérgete en la Programación Orientada a Objetos (POO) mientras disfrutas del juego clásico. "
           "Cada aspecto, desde la serpiente hasta la comida, es un objeto interactivo. "
           "Únete a nosotros para aprender y divertirte mientras exploras este fascinante cruce "
           "entre programación y entretenimiento.")
        content = turtle.Turtle()
        content.speed(0)
        content.color("white")
        content.penup()
        content.hideturtle()

        lines = self.dividir_texto(content_text,40)
        y_coor = 180
        for line in lines:
            content.setposition(-250,y_coor)
            content.write(line, align = "left", font= ("Courier", 20))
            y_coor -= 25

        text_hiper = turtle.Turtle()
        text_hiper.speed(0)
        text_hiper.color("blue")
        text_hiper.penup()
        text_hiper.hideturtle()
        text_hiper.setposition(0, -150)
        text_hiper.write("Haz click aquí para concer más", align = "center", font = ("Courier", 20, "normal"))

        turtle.mainloop()

    def agregar_boton_atras(self):
        boton_atras = turtle.Turtle()
        boton_atras.speed(0)
        boton_atras.color("white")
        boton_atras.penup()
        boton_atras.goto(-260, 260)
        boton_atras.write("<", align = "center", font= ("Courier", 24, "normal"))
        boton_atras.hideturtle()
    def ir_atras(self, x,y):
        if -270 <x<-250 and 250 < y <280:
            self.screen.ventana.clear()
            return self.backMethod()
        elif -150 < y < -130 and -250 < x < 250:
            webbrowser.open("https://hybridge.education")

        
    def dividir_texto(self, content,text_lenght):
        words = content.split()
        lines = []
        current_line = ""
        for word in words:
            if len(current_line) + len(word) <= text_lenght:
                current_line += word + " "
            else:
                lines.append(current_line)
                current_line = word + " "
        lines.append(current_line)
        return lines

            



    
#Código de ejemplo

def backMtd():
    print("atrás")

#ventana = Scrfeen(600,600,"Juego de Snake", "black")

#menu = AcercaDe(ventana, backMtd)