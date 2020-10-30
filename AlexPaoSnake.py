from turtle import *
from random import randrange, random
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#Colores para la víbora y la comida
SnakeColor = ['blue', 'green','orange', 'purple', 'black']
FoodColor = ['blue', 'green','orange', 'purple', 'black']

#El color se escogera al azar
i = randrange(0,5)
j = randrange(0,5)

#Ciclo para que los colores no sean iguales
while i == j:
    j = randrange(0,5)


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'pink')
        update()
        print('Fin del juego')
        exit()

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9,SnakeColor[i])
    square(food.x, food.y, 9, FoodColor[j])   
    update()
    ontimer(move,110)

def move_food():
    #Mueve la comida una posición de forma aleatoria
    #Movimientos de comida
    moveList = [[10,0],[-10,0],[0,10],[0,-10],[10,10],[-10,-10],[-10,10],[10,-10]]
    #Se realiza un movimiento al azar
    indx = randrange (0,8)
    #Se cambia el valor de comida
    food.x += moveList[indx][0]
    food.y += moveList[indx][1]

    #Revisa si en la comida se sale
    if not inside(food) or food == snake[-1]:
        #Si se cumple cualquiera de estas condiciones la comida anula el movimiento anterior 
        if indx%2 == 0:
            food.x += moveList[indx+1][0]
            food.y += moveList[indx+1][1]
            food.x += moveList[indx+1][0]
            food.y += moveList[indx+1][1]
        else:
            food.x += moveList[indx-1][0]
            food.y += moveList[indx-1][1]
            food.x += moveList[indx-1][0]
            food.y += moveList[indx-1][1]
             
    ontimer(move_food, 600)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
