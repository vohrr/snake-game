
from pygame import Rect
import pygame

class Snake:
    nodes = []

    def __init__(self,screen):
        self.nodes.append(SnakeNode(None,pygame.Rect(((screen.get_width()-80)/2,screen.get_height()/2,40,40))))
        
class SnakeNode:
    direction:str = None
    rect:Rect = None

    def __init__(self, direction, rect):
        self.direction = direction
        self.rect = rect