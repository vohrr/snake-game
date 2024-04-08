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
    for node in snake.nodes:
        if x:
            node.rect.move_ip(direction * MOVEMENT_VALUE,0)
            if direction == -1:
                node.direction = 'left'
            else:
                node.direction = 'right'
        else:
            node.rect.move_ip(0, direction * MOVEMENT_VALUE)
            if direction == -1:
                node.direction = 'up'
            else:
                node.direction = 'down'
