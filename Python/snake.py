"""Snake, classic arcade game.



Primera edición Miguel Vázquez

Segunda edición Raúl Ávila

Tercera edicion Yarezzi Garcia

Changes 
- Arrow keys to respond with "A,S,D,W"
- Color of food
- Make the snake faster

"""

from turtle import *
from random import randrange
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

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
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
        square(body.x, body.y, 9, 'yellow')

    square(food.x, food.y, 9,'blue')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'D') #Change the arrow key right to letter D
onkey(lambda: change(-10, 0), 'A') #Change the arrow key left to letter A
onkey(lambda: change(0, 10), 'W') #Change the arrow key up to letter W
onkey(lambda: change(0, -10), 'S') #Change the arrow key down to letter S
move()
done()
