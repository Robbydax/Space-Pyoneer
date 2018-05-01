'''
Created on Apr 17, 2018

@author: robby
'''
import pygame
from src.scripts.NPC import *
pygame.init()

class Player:
    
    def __init__(self, name):
        self.name = name
        self.facing = "south"
        sprite = pygame.image.load("graphics\\Rencu.png")
        size = sprite.get_size()
        self.width = size[0]
        self.height = size[1]
        
        #get player faces
        self.faces = get_faces(sprite)
    
    def render(self, surface, pos):
        surface.blit(self.faces[self.facing], pos)
        