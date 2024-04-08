
import pygame
from pygame import Rect
from Move import MOVEMENT_KEYS, move_snake_all 
from Initialize import startup
import random

from Snake import Snake, SnakeNode
#game window
#game loop
#event handler
food_spawned = False
current_direction = None

#we need a snake node class, it will contain the Rect object but also the current direction each node is 
#how do we handle changes in direction? does that get included in the move loop? 
###yes, keep a pointer to the previous nodes direction and shift it down the snake

def main(screen):
    #game loop
    run = True
    global food_spawned
    global current_direction
    snake = Snake(screen)
    food = new_food()
    while run:
        #refresh & redraw
        screen.fill('black')
        if not food_spawned:
            food = new_food()
            food_spawned = True
        draw_snake(snake)
        pygame.draw.rect(screen, 'red', food)
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = not run
            if event.type == pygame.KEYDOWN:
                process_input(event.key,snake,food)
        pygame.display.flip()
    #close game    
    pygame.quit()


def process_input(key,snake:Snake, food:Rect):
    #movement
    if key in MOVEMENT_KEYS:
        move_snake_all(key,snake,screen)
        check_collision(snake,food)

#generate a coordinate that will be equal to our snake's size and have the same pixel centers        
def new_food():    
    x_cells = screen.get_width() / 40 - 1
    y_cells = screen.get_height() / 40 - 1
    x_coordinate = random.randint(0,int(x_cells)) * 40
    y_coordinate = random.randint(0,int(y_cells)) * 40
    return pygame.Rect((x_coordinate,y_coordinate,40, 40))

def check_collision(snake:Snake, food:Rect):
    global food_spawned
    global current_direction
    
    if snake.nodes[0].rect.colliderect(food):
        food_spawned = False
        grow_snake(snake, current_direction)
    
    #if snake[0].rect.collidelist(snake):
        #pygame.quit()
        
#current direction is used to append the next node of the snake to the tail
#current direction is NOT the current direction of the head, its the current direction of the LAST INDEX
def grow_snake(snake:Snake, direction:str):
    current_tail:SnakeNode = snake.nodes[-1]
    #TODO: implement so that the new tail is added properly based on current direction of old tail
    if current_tail.direction == 'left':
        new_tail = SnakeNode(direction,pygame.Rect((current_tail.rect.right,current_tail.rect.top,40,40)))
    elif current_tail.direction == 'right':
        new_tail = SnakeNode(direction,pygame.Rect((current_tail.rect.left,current_tail.rect.top,40,40)))
    elif current_tail.direction == 'up':
        new_tail = SnakeNode(direction,pygame.Rect((current_tail.rect.left,current_tail.rect.top,40,40)))
    elif current_tail.direction == 'down':
        new_tail = SnakeNode(direction,pygame.Rect((current_tail.rect.left,current_tail.rect.bottom,40,40)))
    
    snake.nodes.append(new_tail)


def draw_snake(snake:Snake):
    for segment in snake.nodes:
        pygame.draw.rect(screen, 'green', segment.rect)


screen = startup()
main(screen)
