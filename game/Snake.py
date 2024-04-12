
from typing import List
from pygame import Rect
import pygame

MOVEMENT_VALUE = 40
        
class SnakeNode:
    direction:str = None
    rect:Rect = None

    def __init__(self, direction, rect):
        self.direction = direction
        self.rect = rect

    def move(self):
        x_y = self.get_direction()
        self.rect.move_ip(x_y[0] * MOVEMENT_VALUE, x_y[1] * MOVEMENT_VALUE)

    def get_direction(self):
        direction = self.direction
        if direction == 'left':
            return (-1,0)
        if direction == 'right':
            return (1,0)
        if direction == 'up':
            return (0,-1)
        if direction == 'down':
            return (0,1)
        return 0

class Snake:
    nodes:List[SnakeNode] = []

    def __init__(self,screen):
        self.nodes.append(SnakeNode(None,pygame.Rect(((screen.get_width()-80)/2,screen.get_height()/2,MOVEMENT_VALUE,MOVEMENT_VALUE))))

    def grow(self):
        current_tail:SnakeNode = self.nodes[-1]
        if current_tail.direction == 'left':
            new_tail = SnakeNode(current_tail.direction, pygame.Rect((current_tail.rect.right, current_tail.rect.top, MOVEMENT_VALUE, MOVEMENT_VALUE)))
        elif current_tail.direction == 'right':
            new_tail = SnakeNode(current_tail.direction, pygame.Rect((current_tail.rect.left-MOVEMENT_VALUE, current_tail.rect.top, MOVEMENT_VALUE, MOVEMENT_VALUE)))
        elif current_tail.direction == 'up':
            new_tail = SnakeNode(current_tail.direction, pygame.Rect((current_tail.rect.left, current_tail.rect.bottom, MOVEMENT_VALUE, MOVEMENT_VALUE)))
        elif current_tail.direction == 'down':
            new_tail = SnakeNode(current_tail.direction, pygame.Rect((current_tail.rect.left, current_tail.rect.top-MOVEMENT_VALUE, MOVEMENT_VALUE, MOVEMENT_VALUE)))
        self.nodes.append(new_tail)