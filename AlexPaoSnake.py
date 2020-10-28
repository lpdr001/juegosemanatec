""" Alejandro Hernández De la Torre / Lidía Paola Diaz Ramita """

from turtle import *
from random import randrange, random
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def insidef(food):
    "Return True if food inside boundaries."
    return -200 < food.x < 190 and -200 < food.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'blue')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9,'orange')

    square(food.x, food.y, 9, 'purple')
    if insidef(food):
        food.y = 1+ randrange(-4,2) * 15 
        food.x = 1+ randrange(-4,2) * 15
    else:
        if food.y > 170: food.y = 170
        elif food.y < -360: food.y = -360
        if food.x > 420: food.x = 420
        elif food.x < -420: food.x = -420    
    update()
    ontimer(move,110)

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
