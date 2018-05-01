'''
Created on Apr 23, 2018

@author: robby
'''
import pygame
from src.scripts.textures import Tiles
from src.MyColors import Color
import math

def export_map(file):
    map_data = ""
    
    max_x, max_y = 0, 0
    
    for t in tile_data:
        if t[0] > max_x:
            max_x = t[0]
        if t[1] > max_y:
            max_y = t[1]
    
    for tile in tile_data: 
        map_data = map_data + str(int(tile[0]/32)) + "," + str(int(tile[1]/32)) + ":" + tile[2] + "-"
    
    map_data = map_data + str(int(max_x/32)) + "," + str(int(max_y/32))
    
    #Write File
    with open(file, "w") as mapfile:
        mapfile.write(map_data)

def load_map(file):
    global tile_data
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
        tiles[tiles.index(tile)] = [pos[0] * 32, pos[1] * 32, tile[1]]
    tile_data = tiles

window = pygame.display.set_mode((800,600), pygame.HWSURFACE)
pygame.display.set_caption("Map Editor")
clock = pygame.time.Clock()


txt_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

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


mouse_pos = 0
mouse_x, mouse_y = 0, 0

map_width, map_height = 100 * 32, 100 * 32

selector = pygame.Surface((32,32), pygame.HWSURFACE|pygame.SRCALPHA)
selector.fill(Color().WithAlpha(100, Color.CornflowerBlue))



tile_data = []

camera_x, camera_y = 0, 0
camera_move = 0

brush = "1"
for x in range(0, map_width, 32):
    for y in range(0, map_height, 32):
        tile_data.append([x, y, "3"])

isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            
        #Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                camera_move = 1 
            elif event.key == pygame.K_DOWN:
                camera_move = 2
            elif event.key == pygame.K_LEFT:
                camera_move = 3
            elif event.key == pygame.K_RIGHT:
                camera_move = 4
                
            if event.key == pygame.K_1:
                brush = "r"
            elif event.key == pygame.K_2:
                selection = input("Brush Tag: ")
                brush = selection
            
            if event.key == pygame.K_s:
                export_map("gameMap.map")
                print("Map Saved")
            if event.key == pygame.K_l:
                load_map("gameMap.map")
                print("Map Loaded")
                     
        elif event.type == pygame.KEYUP:
                camera_move = 0
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = math.floor(mouse_pos[0] / 32) * 32
            mouse_y = math.floor(mouse_pos[1] / 32) * 32
        if event.type == pygame.MOUSEBUTTONDOWN:
            tile = [mouse_x - camera_x, mouse_y - camera_y, brush]
            
            if not brush == "r":
                    tile_data.append(tile)
            else:
                if brush == "r":
                    #remove tile
                    for t in tile_data:
                        if t[0] == tile[0] and t[1] == tile[1]:
                            tile_data.remove(t)
                            print("Tile removed")
            '''
            found = False
            for t in tile_data:
                if t[0] == tile[0] and t[1] == tile[1]:
                    found = True
                    break
            if not found:
                if not brush == "r":
                    tile_data.append(tile)
            else:
                if brush == "r":
                    #remove tile
                    for t in tile_data:
                        if t[0] == tile[0] and t[1] == tile[1]:
                            tile_data.remove(t)
                            print("Tile removed")
                else:
                    print("A tile already placed there")
            '''       
    if camera_move == 1:
        camera_y += 32      
    elif camera_move == 2:
        camera_y -= 32 
    elif camera_move == 3:
        camera_x += 32
    elif camera_move == 4:
        camera_x -= 32            
    
    window.fill(Color.Blue)
    
    #Draw Map
    for tile in tile_data:
        try:
            window.blit(Texture_Tags[tile[2]], (tile[0] + camera_x, tile[1] + camera_y))
        except:
            pass
    
    #Draw Tile Highlighter
    window.blit(selector, (mouse_x, mouse_y))
    
    pygame.display.update()

pygame.quit()