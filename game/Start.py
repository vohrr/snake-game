import pygame

def draw_start_screen(screen:pygame.Surface):
    big_font = pygame.font.SysFont(None, 240)
    small_font = pygame.font.SysFont(None, 72)
    title = big_font.render('SNAKE', True, 'green')
    play_button = small_font.render('Press Enter to play', True, 'red')
    screen.fill('black')
    screen.blit(title, (screen.get_width()/2-300,screen.get_height()/2-160))
    screen.blit(play_button, (screen.get_width()/2-220,screen.get_height()/2+80))