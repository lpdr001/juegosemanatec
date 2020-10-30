""" Alejandro Hernández De la Torre / Lidia Paola Díaz Ramirez """
from turtle import *
from freegames import vector
import turtle

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(4):
        forward(end.x - start.x)
        left(90)
    end_fill()

def circle(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y) #Punto de partida a Start
    down()
    begin_fill()
    turtle.circle(end.x - start.x) #Función que dibuja un circulo donde lo pide el usuario
    
    end_fill() #Termina el llenado

def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y) #Punto de partida Start
    down()
    begin_fill() #Comienza el llenado de la figura 
    for count in range(2): # Ejecuta el cilo dos veces 
        forward (end.x - start.x) #Si el contador es par, es una linea horizontal
        left (90) # Gira 90 grados
        forward(end.y - start.y) #Si el contador es impar,es una linea vertical
        left(90) #Gira 90 grados para completar la figura
    end_fill() #Termina la figura
    
def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y) #Punto de partida Start
    down()
    begin_fill() #Comienza el llenado de la figura 
    for count in range(3): #Ya que es una figura de 3 lados, el ciclo se ejecuta 3 veces
        forward(end.x - start.x)  #Cada lado medirá la diferencia entre el X de end y de start
        left(120) #Gira 120 grados (360/3 Lados) a la izquierda
    end_fill() #Termina de llenar
    
def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']
    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 400, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')

#Onkey asigna una función a un caracter específico
#Se usa lambda debido a que onkey requiere una función que no tenga parametros
onkey(lambda: color('red'), 'R')  #Asigna el color red a 'R'
onkey(lambda: color('pink'), 'P') #Asigna el color pink a 'P'
onkey(lambda: color('blue'), 'B') #Asigna el color blue a 'B'
onkey(lambda: color('black'), 'N') #Asigna el color black a 'N'
onkey(lambda: color('yellow'), 'Y') #Asigna el color yellow a 'Y'
onkey(lambda: color('green'), 'G') #Asigna el color greeb a 'G'
onkey(lambda: store('shape', line), 'l') #Asigna la figura linea a 'l'
onkey(lambda: store('shape', square), 's') #Asigna la figura de cuadrado a 's'
onkey(lambda: store('shape', circle), 'c') #Asigna la figura de círculo a 'c'
onkey(lambda: store('shape', rectangle), 'r') #Asigna la figura de rectangulo a 'r'
onkey(lambda: store('shape', triangle), 't') #Asigna la figura triagulo a 't'
done()
