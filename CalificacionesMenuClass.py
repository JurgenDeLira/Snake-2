import turtle
from ScrfeenClass import Scrfeen

class CalificacionesMenu:
    def __init__(self, screen, backMethod):
        self.screen = screen
        self.backMethod = backMethod

        self.titulo = turtle.Turtle()
        self.titulo.speed(0)
        self.titulo.color("white")
        self.titulo.penup()
        self.titulo.goto(0,250)

        self.titulo.write("Puntuaciones", align = "center", font = ("Courier",36, "bold"))
        self.titulo.hideturtle()
        self.agregar_boton_atras()
        self.screen.ventana.onscreenclick(self.ir_atras, btn = 1)
        self.showRegisters()
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
    
    def leer_registros(self, nombre_archivo):
        registros = []
        try:
            with open(nombre_archivo, 'r') as file:
                for linea in file:
                    
                    nombre, puntuacion = linea.strip().split(',')
                    print(nombre, puntuacion)
                    registros.append((nombre, int(puntuacion)))

        except FileNotFoundError:
            print("El archivo no existe.")

        registros_ordenados = sorted(registros, key = lambda x:x[1], reverse=True )[:5]
        return registros_ordenados

    def ajustar_posicion(self,nombre, x, y, turtle_txt):
        umbral_ancho = 40
        tamano_fuente = 20
        fragmentos = []

        while len(nombre )> 0:
            fragmento = nombre[:umbral_ancho]
            nombre = nombre[umbral_ancho:]
            fragmentos.append(fragmento)
        for i, fragmento in enumerate(fragmentos):
            turtle_txt.penup()
            turtle_txt.goto(x, y - i * (tamano_fuente+5))
            turtle_txt.write(fragmento, align = "center", font = ("Courier", tamano_fuente, "normal"))

    def showRegisters(self):
        registros = self.leer_registros("calificaciones.txt")
        register_text = turtle.Turtle()
        register_text.speed(0)
        register_text.penup()
        register_text.hideturtle()

        if not registros:
            register_text.color("white")
            register_text.write("Aún no hay registros por mostrar", align="center", font= ("Courier", 20,"normal" ))
        
        else:
            y = 150
            for i, (nombre, puntuacion)  in enumerate(registros):
                register_text.penup()
                register_text.color("white" if i == 0 else "red")
                self.ajustar_posicion(f"{i+1}.Nombre: {nombre}, Puntuación:{puntuacion}", 0, y, register_text)
                y  -= 80












# código de ejemplo


def backMtd():
    print("atrás 2342344")

#ventana = Scrfeen(600,600,"Juego de Snake", "black")
#menu = CalificacionesMenu(ventana, backMtd)