'''
Created on Apr 24, 2018

@author: robby
'''
import pygame
from src.scripts.textures import Tiles

Floor = Tiles.Load_Texture("graphics\\Space_grid.png", 32)
Grass_Stone = Tiles.Load_Texture("graphics\\Grass_Stone.png", 32)
Grass = Tiles.Load_Texture("graphics\\Grass.png", 32)
Rock = Tiles.Load_Texture("graphics\\Rock.png", 32)
Shrub = Tiles.Load_Texture("graphics\\shrub.png", 32)
Flower = Tiles.Load_Texture("graphics\\flower.png", 32)
Cliffside = Tiles.Load_Texture("graphics\\cliffside.png", 32)
Tree1 = Tiles.Load_Texture("graphics\\tree1.png", 32)
Tree2 = Tiles.Load_Texture("graphics\\tree2.png", 32)

Texture_Tags = {"1": Floor, "2": Grass_Stone, "3": Grass, "4": Rock, "5": Shrub, "6": Flower, "7": Cliffside,"8":Tree1,"9":Tree2}

class Map_Engine:
    
    @staticmethod
    def add_tile(tile, pos, addTo):
        addTo.blit(tile, (pos[0] * 32, pos[1] * 32))
        
    @staticmethod
    def load_map(file):
        with open(file, "r") as mapfile:
            map_data = mapfile.read()
        map_data = map_data.split("-")
        
        map_size = map_data[len(map_data) - 1]
        map_data.remove(map_size)
        map_size = map_size.split(",")
        map_size[0] = int(map_size[0]) * 32
        map_size[1] = int(map_size[1]) * 32
    
        tiles = []
        
        for tile in range(len(map_data)):
            map_data[tile] = map_data[tile].replace("\n", "")
            tiles.append(map_data[tile].split(":"))
        
        for tile in tiles:
            tile[0] = tile[0].split(",")
            pos = tile[0]
            for p in pos:
                pos[pos.index(p)] = int(p)
            tiles[tiles.index(tile)] = (pos, tile[1])
        
        terrain = pygame.Surface(map_size, pygame.HWSURFACE)
        
        for tile in tiles:
            if tile[1] in Texture_Tags:
                Map_Engine.add_tile(Texture_Tags[tile[1]], tile[0], terrain)
                
            if tile[1] in Tiles.Blocked_Types:
                Tiles.Blocked.append(tile[0])   
            
            if tile[1] in Tiles.Crop_Types:
                Tiles.Crops.append(tile[0])
            
            if tile[1] in Tiles.Seed_Types:
                Tiles.Seeds.append(tile[0])
            
            if tile[1] in Tiles.Grass_Types:
                Tiles.Grass.append(tile[0])
                
        return terrain
        