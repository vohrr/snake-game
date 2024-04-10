
import pygame
from pygame import Rect
from Move import MOVEMENT_KEYS, move_snake_all, check_collision
from Initialize import FOOD_EATEN, startup
import random
from Snake import Snake, SnakeNode

food_spawned = False
current_direction = None

#game loop
def snake_run(screen):
    run = True
    global food_spawned
    global current_direction
    snake = Snake(screen)
    while run:
        #refresh & redraw
        screen.fill('black')
        if not food_spawned:
            food = new_food(snake)
            food_spawned = True
        draw_snake(snake)
        pygame.draw.rect(screen, 'red', food)
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = not run
            if event.type == pygame.KEYDOWN:
                process_input(event.key,snake,food)
            if event.type == FOOD_EATEN:
                food_spawned = False
        pygame.display.flip()
    #close game    
    pygame.quit()

def process_input(key,snake:Snake, food:Rect):
    #movement
    if key in MOVEMENT_KEYS:
        move_snake_all(key,snake,screen)
        check_collision(snake,food)

#generate a coordinate that will be equal to our snake's size and have the same pixel centers        
def new_food(snake:Snake):    
    x_cells = screen.get_width() / 40 - 1
    y_cells = screen.get_height() / 40 - 1
    x_coordinate = random.randint(0,int(x_cells)) * 40
    y_coordinate = random.randint(0,int(y_cells)) * 40
    food_candidate = pygame.Rect((x_coordinate,y_coordinate,40, 40))
    if food_candidate.collidelist(snake.nodes) != -1:
        return new_food(snake)
    else: 
        return food_candidate
           
def draw_snake(snake:Snake):
    for segment in snake.nodes:
        pygame.draw.rect(screen, 'green', segment.rect)


screen = startup()
snake_run(screen)
