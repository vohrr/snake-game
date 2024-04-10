import pygame
from pygame import Rect
from Snake import Snake, SnakeNode, MOVEMENT_VALUE
from Initialize import FOOD_EATEN


MOVE_RIGHT = [ pygame.K_d, pygame.K_RIGHT]
MOVE_LEFT = [pygame.K_a, pygame.K_LEFT]
MOVE_UP = [pygame.K_w, pygame.K_UP]
MOVE_DOWN = [pygame.K_s, pygame.K_DOWN]
MOVEMENT_KEYS = [pygame.K_a, pygame.K_LEFT, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]

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
        current_node = snake.nodes[index]
        current_node.move()
        lead:SnakeNode = snake.nodes[index-1]
        current_node.direction = lead.direction

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

def check_collision(snake:Snake, food:Rect):
    
    if snake.nodes[0].rect.colliderect(food):
        pygame.event.post(pygame.event.Event(FOOD_EATEN))
        snake.grow()
    
    if len(snake.nodes) > 1 and snake.nodes[0].rect.collidelist(snake.nodes[1:]) != -1:
        pygame.event.clear
        pygame.event.post(pygame.event.Event(pygame.QUIT))

