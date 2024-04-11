
import pygame
from pygame import Rect, Surface
from Move import MOVEMENT_KEYS, move_snake_all, check_collision
from Initialize import ENTER_KEY, START_GAME, FOOD_EATEN, get_dt, initialize_clock, startup
import random
from Start import draw_start_screen
from Snake import Snake

food_spawned = False
current_direction = None

def start_screen(screen):
    run = True
    while run:
        draw_start_screen(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                process_input(event.key, None, None)
            if event.type == START_GAME:
                run = not run
        pygame.display.flip()
        clock.tick(60)
#game loop
def snake_run(screen:Surface, clock):
    run = True
    time_elapsed = 0
    global food_spawned
    global current_direction
    snake = Snake(screen)
    while run:
        time_elapsed += clock.get_time()
        #refresh & redrw
        screen.fill('black')
        if not food_spawned:
            food = new_food(snake)
            food_spawned = True
        if  time_elapsed >= get_dt():
            time_elapsed = 0
            move_snake_all(current_direction, snake, screen)
            check_collision(snake,food)
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
        clock.tick(60)
    #close game    
    pygame.quit()

def process_input(key,snake:Snake, food:Rect):
    global current_direction
    #movement
    if key in MOVEMENT_KEYS:
        current_direction = key
    if key == ENTER_KEY:
        pygame.event.post(pygame.event.Event(START_GAME))
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
clock = initialize_clock()
start_screen(screen)
snake_run(screen, clock)
