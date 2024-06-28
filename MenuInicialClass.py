import turtle
from ScrfeenClass import Scrfeen
from PIL import Image
from MenuNivelesClass import MenuNiveles
from CalificacionesMenuClass import CalificacionesMenu
from AcercaDeClass import AcercaDe
class MenuInicial():
    def __init__(self, scrfeen, initGame):
        self.pantalla = scrfeen.ventana
        self.scrfeen = scrfeen
        self.initGame = initGame

        self.opciones = ["Iniciar Juego", "Ver Puntajes", "Acerca De"]
        self.opcion_seleccionada = None
        self.opcion_actual = 0


        self.titulo = turtle.Turtle()
        self.titulo.speed(0)
        self.titulo.color("white")
        self.titulo.penup()
        self.titulo.goto(0,250)

        self.titulo.write("Snake Hybridge", align = "center", font = ("Courier",36,"bold") )
        self.titulo.hideturtle()

        self.texto_subtitle = turtle.Turtle()
        self.texto_subtitle.speed(0)
        self.texto_subtitle.color("white")
        self.texto_subtitle.penup()
        self.texto_subtitle.goto(0,210)

        self.texto_subtitle.write("Hybridge 2024", align = "center", font = ("Courier", 24, "normal"))
        self.texto_subtitle.hideturtle()

        self.redimensionar_imagen("hybridge.gif","imagen_redimensionada.gif", 100, 100)

        self.pantalla.addshape("imagen_redimensionada.gif")

        self.imagen = turtle.Turtle()
        self.imagen.speed(0)
        self.imagen.penup()
        self.imagen.shape("imagen_redimensionada.gif")
        self.imagen.goto(0,100)


        self.botones = []

        for i, opcion  in enumerate(self.opciones):
            boton = turtle.Turtle()
            boton.speed(0)
            boton.color("white")
            boton.penup()

            boton.goto(0, i*-100)
            boton.write(opcion, align ="center", font = ("Courier",24, "normal") )
            boton.hideturtle()
            self.botones.append(boton)
        
        self.selector =  turtle.Turtle()
        self.selector.speed(0)
        self.selector.color("yellow")
        self.selector.penup()
        self.selector.shape("square")
        self.selector.shapesize(stretch_wid=1, stretch_len=10)
        self.actualizar_selector()
        self.pantalla.listen()
        self.pantalla.onkeypress(self.mover_abajo, "Down")
        self.pantalla.onkeypress(self.mover_arriba, "Up")
        self.pantalla.onkeypress(self.cambiar_opcion, "Return")
        turtle.mainloop()

    def actualizar_selector(self):
        self.selector.goto(self.botones[self.opcion_actual].xcor(),self.botones[self.opcion_actual].ycor()-10)
        print("Opción actual:", self.opciones[self.opcion_actual])

    def mover_arriba(self):
        if self.opcion_actual > 0:
            self.opcion_actual -= 1
            self.actualizar_selector()
    
    def mover_abajo(self):
        if self.opcion_actual < len(self.opciones)-1:
            self.opcion_actual += 1
            self.actualizar_selector()
    
    def cambiar_opcion(self):
       self.opcion_seleccionada =  self.opciones[self.opcion_actual]

       self.pantalla.clear()
       ventana = Scrfeen(600,600, "Juego de snake", "black")


       if self.opcion_seleccionada.lower() == "iniciar juego":
           menu_niveles = MenuNiveles(ventana, self.backMethod, self.initGame)
       elif self.opcion_seleccionada.lower() == "ver puntajes":
          menu = CalificacionesMenu(ventana, self.backMethod)
       elif self.opcion_seleccionada.lower() == "acerca de":
          menu = AcercaDe(ventana, self.backMethod)
       else:
           print("otro")
           
    def backMethod(self):
        ventana = Scrfeen(600,600, "Juego de snake", "black")
        menu = MenuInicial(ventana,self.initGame )













       
    
    def redimensionar_imagen(self,ruta_origen, ruta_destino, ancho, alto):
        imagen = Image.open(ruta_origen)
        imagen_redimensionada = imagen.resize((ancho, alto))
        imagen_redimensionada.save(ruta_destino)


##### Código ejemplo

def initGame(delay):
    print(delay)


#ventana = Scrfeen(600, 600, "Juego de Snake", "black")

#menu = MenuInicial(ventana,initGame)






