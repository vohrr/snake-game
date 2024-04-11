import pygame
from Snake import Snake

def draw_start_screen(screen:pygame.Surface):
    big_font = pygame.font.SysFont(None, 240)
    small_font = pygame.font.SysFont(None, 72)
    title = big_font.render('SNAKE', True, 'green')
    play_button = small_font.render('Press Enter to play', True, 'red')
    screen.fill('black')
    screen.blit(title, (screen.get_width()/2-300,screen.get_height()/2-160))
    screen.blit(play_button, (screen.get_width()/2-220,screen.get_height()/2+80))


def draw_game_over_screen(screen:pygame.Surface, snake:Snake):
    big_font = pygame.font.SysFont(None, 240)
    small_font = pygame.font.SysFont(None, 72)
    game_over = big_font.render('GAME OVER', True, 'red')
    score = small_font.render('Your Score: ' + str(len(snake.nodes)*100),True, 'green')
    screen.fill('black')
    screen.blit(score, (screen.get_width()/2-175,screen.get_height()/2+80))
    screen.blit(game_over, (screen.get_width()/2-500,screen.get_height()/2-160))