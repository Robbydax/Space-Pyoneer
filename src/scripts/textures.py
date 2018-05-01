'''
Created on Apr 17, 2018

@author: robby
'''
import pygame
import src

pygame.init()

class Tiles:
    
    Blocked = []
    
    Crops = []
    
    Seeds = []
    
    Grass = []
    
    Blocked_Types = ["4", "7", "8", "9"]
    
    Crop_Types = ["6"]
    
    Seed_Types = ["5"]
    
    Grass_Types = ["3"]
    
    @staticmethod
    def Grass_At(pos):
        if list(pos) in Tiles.Grass:
            return True
        else:
            return False
    
    @staticmethod
    def Seed_At(pos):
        if list(pos) in Tiles.Seeds:
            return True
        else:
            return False
    
    @staticmethod
    def Crop_At(pos):
        if list(pos) in Tiles.Crops:
            return True
        else:
            return False
    
    @staticmethod
    def Blocked_At(pos):
        if list(pos) in Tiles.Blocked:
            return True
        else:
            return False
        
    @staticmethod
    def Load_Texture(file, Size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (Size, Size))
        surface = pygame.Surface((Size, Size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0,0))
        return surface
    
    
    
    

    