import pygame

FOOD_EATEN = pygame.USEREVENT + 1
DT = 150

def initialize_window():   
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.5625)
    pygame.display.set_caption('Snake')
    return pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

def initialize_clock():
    return pygame.time.Clock()

def get_dt():
    return DT

def startup():
    pygame.init()
    return initialize_window()
