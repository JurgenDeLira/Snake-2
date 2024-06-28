import turtle
from ScrfeenClass import Scrfeen
import time
import os
class Serpiente:
    def __init__(self, colorCabeza, colorSegmento):
        self.segmentos = []
        self.cabeza = turtle.Turtle()
        self.cabeza.speed(0)
        self.cabeza.shape("square")
        self.cabeza.color(colorCabeza)
        self.cabeza.penup()
        self.cabeza.goto(0,0)


        self.cabeza.direction = "stop"

        self.colorSegmento = colorSegmento

    def controles(self, ventana, arriba, abajo, izquierda, derecha):
        ventana.listen()
        ventana.onkeypress(self.arriba, arriba)
        ventana.onkeypress(self.abajo, abajo)
        ventana.onkeypress(self.izquierda, izquierda)
        ventana.onkeypress(self.derecha, derecha)

    def arriba(self):
        print("arriba")
        if self.cabeza.direction != "down":
            self.cabeza.direction = "up"
    def abajo(self):
        print("abajo")
        if self.cabeza.direction != "up":
            self.cabeza.direction = "down"
    
    def derecha(self):
        print("derecha")
        if self.cabeza.direction != "left":
            self.cabeza.direction = "right"
    
    def izquierda(self):
        print("izquierda")
        if self.cabeza.direction != "right":
            self.cabeza.direction = "left"

    def movimiento(self, juego, screen):
        if self.cabeza.direction == "up":
            y = self.cabeza.ycor()
            if y < (screen.lado/2-20):
                self.cabeza.sety(y+20)
            else:
                juego.perder = True
        if self.cabeza.direction == "down":
             y = self.cabeza.ycor()
             if y> -(screen.lado/2):
                 self.cabeza.sety(y-20)
             else:
                juego.perder = True
        if self.cabeza.direction == "left":
            x = self.cabeza.xcor()
            if x> -(screen.lado/2):
                self.cabeza.setx(x-20)
            else:
                juego.perder = True
        if self.cabeza.direction == "right":
            x = self.cabeza.xcor()
            if x<(screen.lado/2-20):
                self.cabeza.setx(x+20)
            else:
                juego.perder = True  
    
    def agregarSegmentos(self):
        self.nuevo_segmento = turtle.Turtle()
        self.nuevo_segmento.speed(0)
        self.nuevo_segmento.shape("square")
        self.nuevo_segmento.color(self.colorSegmento)
        self.nuevo_segmento.penup()
        self.segmentos.append(self.nuevo_segmento)
    
    def moverCuerpo(self):
        tamanio = len(self.segmentos)
        for i in range(tamanio - 1, 0, -1):
            x = self.segmentos[i-1].xcor()
            y = self.segmentos[i-1].ycor()
            self.segmentos[i].goto(x,y)
        if tamanio > 0:
            x = self.cabeza.xcor()
            y = self.cabeza.ycor()
            self.segmentos[0].goto(x,y)
    
    def colision(self, serpiente, juego, screen, comida):
        for seg in self.segmentos:
            if seg.distance(self.cabeza) < 20:
                juego.alPerder(serpiente, screen, comida)

class Game:
    perder = False
    puntos = 0
    max_pun = 0
    running = True
    def __init__(self, delay = 0.2):
        self.delay = delay
        registros = self.leer_registros("calificaciones.txt")
        if len(registros) > 0:
            self.jugar, self.max_pun = registros[0]




    def puntaje(self, colorTexto):
        self.texto = turtle.Turtle()
        self.texto.speed(0)
        self.texto.color(colorTexto)
        self.texto.penup()
        self.texto.hideturtle()

        self.texto.goto(0,250)

        self.texto.write("Puntos: 0    Puntaje máximo: {}".format(self.max_pun), align="center", font=("times", 24, "normal"))
    
    def actualizarPuntaje(self, puntos):
        self.puntos += puntos
        if self.puntos > self.max_pun:
            self.max_pun_temp = self.puntos
        self.texto.clear()
        self.texto.write("Puntos: {}    Puntaje máximo: {}".format(self.puntos, self.max_pun), align="center", font=("times", 24, "normal"))

    def resetearPuntaje(self):
        self.puntos = 0 
        self.texto.clear()
        self.texto.color("white")
        self.texto.goto(0,250)
        self.texto.write("Puntos: {}    Puntaje máximo: {}".format(self.puntos, self.max_pun), align="center", font=("times", 24, "normal"))

    def gameOver(self, screen):
        self.texto.clear()
        self.texto.color("red")
        self.texto.write("GAME OVER", align = "center", font = ("times", 40, "bold"))
        screen.ventana.update()
        time.sleep(2)
    def alPerder(self, serpiente, screen,  comida):
        self.perder = False ## Resetear variable para perder
        self.gameOver(screen)
        if self.puntos > self.max_pun:
            self.max_pun = self.puntos
            nombre = turtle.textinput("Ingresar Nombre", "Felicidades! haz superado el máximo puntaje, por favor ingresa tu nombre:")
            self.escribir_en_archivo("calificaciones.txt", nombre+","+str(self.puntos))
        serpiente.cabeza.direction = "stop"
        serpiente.cabeza.goto(0,0)
        for seg in serpiente.segmentos:
            seg.hideturtle()
        serpiente.segmentos.clear() 
        serpiente.controles(screen.ventana,"Up","Down", "Left", "Right")   
        self.resetearPuntaje()
        comida.resetearComida()
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
    def escribir_en_archivo(self, nombre_archivo, contenido):
        directorio_trabajo = os.getcwd()
        ruta = os.path.join(directorio_trabajo, nombre_archivo)

        try:
            if not os.path.exists(ruta):
                with open(ruta, 'w') as archivo:
                    archivo.write(contenido+ '\n')
                print("Se ha crado el archivo")
            else:
                print("el archivo ya existe")
                with open(ruta, 'a') as archivo:
                    archivo.write(contenido+ '\n')
        except PermissionError:
            print("No se tiene permiso para acceder al archivo")
        except Exception as e:
            print(f'Error al crar o escribir archivo: {e}')



######### Código de ejemplo ##############

'''juego = Game(0.5)

scrfeen = Scrfeen(600, 600, "Ejmeplo clase serpiente game", "black")
scrfeen.setArena(400, "red", True)
serpiente = Serpiente("blue","white")

serpiente.controles(scrfeen.ventana, "Up", "Down", "Left", "Right")

juego.puntaje("white")

def actualizar():
    if juego.perder == True:
        juego.alPerder(serpiente, scrfeen)
    else:
        serpiente.movimiento(juego, scrfeen)
        if serpiente.cabeza.direction != "stop":
            serpiente.agregarSegmentos()
            serpiente.colision(juego)
            juego.actualizarPuntaje(1)
    scrfeen.ventana.update()
    serpiente.moverCuerpo()
    scrfeen.ventana.ontimer(actualizar, 100)




actualizar()
scrfeen.ventana.mainloop()'''











