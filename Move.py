import pygame

from Snake import Snake, SnakeNode

MOVEMENT_KEYS = [pygame.K_a, pygame.K_LEFT, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
MOVE_LEFT = [pygame.K_a, pygame.K_LEFT]
MOVE_RIGHT = [ pygame.K_d, pygame.K_RIGHT]
MOVE_UP = [pygame.K_w, pygame.K_UP]
MOVE_DOWN = [pygame.K_s, pygame.K_DOWN]

MOVEMENT_VALUE = 40

def move_snake_all(move_key, snake:Snake, screen):
    head = snake.nodes[0].rect
    if move_key in MOVE_LEFT and head.left != 0:
        move_snake(snake, True, -1)
    elif move_key in MOVE_RIGHT and head.right != screen.get_width():
        move_snake(snake, True, 1)
    elif move_key in MOVE_UP and head.top != 0:
        move_snake(snake, False, -1)
    elif move_key in MOVE_DOWN and head.bottom != screen.get_height():
        move_snake(snake, False, 1)

def move_snake(snake:Snake, x:bool, direction:int):
    move_head(snake.nodes[0],x,direction)
    for index in range(len(snake.nodes)-1,0,-1):
        dir = get_direction(snake.nodes[index].direction)
        move_node(snake.nodes[index],dir)
        lead:SnakeNode = snake.nodes[index-1]
        snake.nodes[index].direction = lead.direction

def move_head(head:SnakeNode, x:bool, direction:int):
    if x:
        head.rect.move_ip(direction * MOVEMENT_VALUE,0)
        if direction == -1:
            head.direction = 'left'
        else:
            head.direction = 'right'
    else:
        head.rect.move_ip(0, direction * MOVEMENT_VALUE)
        if direction == -1:
            head.direction = 'up'
        else:
            head.direction = 'down'


def move_node(node:SnakeNode, x_y:tuple):
    node.rect.move_ip(x_y[0] * MOVEMENT_VALUE, x_y[1] * MOVEMENT_VALUE)

def get_direction(direction:str):
    if direction == 'left':
        return (-1,0)
    if direction == 'right':
        return (1,0)
    if direction == 'up':
        return (0,-1)
    if direction == 'down':
        return (0,1)
    return 0

