from random import *
from turtle import *
from freegames import path
import string

# Se inicia el contador para poder usarlo despues
contador = 0
car = path('car.gif')
tiles = list(range(32))*2
state = {'mark': None}
hide = [True] * 64


def square(x, y):
    "Draw white square with black outline at (x, y)." 
    up()
    goto(x, y)
    down()
    color('white', 'purple')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    global contador
    contador = contador + 1
    spot = index(x, y)
    mark = state['mark']
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        # Aquí se abre un contador para poder contar los pares volteados
        w = 0
        w += 1
        if w == 32:
            goto(0,0)
            write("FINISHEEEEED", font=('HELVETICA', 60, 'bold'))
        print (w)

    
def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        # Aquí se hace una condicional por numeros para centrar los numeros
        if tiles[mark] <= 9 :
            goto(x  + 18, y + 8)
        elif tiles[mark] <= 19 :
            goto(x  + 10, y +8 )
        else :
            goto(x  + 12, y + 8 )        
        color('black')
        write(tiles[mark], font=('Helvetica', 20, 'bold'))
    goto(-260,-30)    
    write(contador, font= ('Helvetica' , 20 , 'bold'))    
    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(560, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
