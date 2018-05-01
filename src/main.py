'''
@author: robby
'''
import pygame
from pygame import *
import os, sys
import time
import math
from src import MyColors as MC
from src.scripts.textures import Tiles
from src.scripts.globals import Globals
from src.scripts.NPC import Dialog
from src.scripts.NPC import *
from src.scripts.player import Player
from src.scripts.Map_Engine import Map_Engine
from src.scripts.meloonatic_gui import Menu, Font

'''MUSIC
by Eric Matyas

www.soundimage.org
'''

cSec = 0
cFrame = 0
FPS = 0
deltatime = 0
tile_size = 32 

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


terrain = Map_Engine.load_map("gameMap.map")

background = pygame.image.load("graphics\\space_background.png")
Background = pygame.Surface(background.get_size(), pygame.HWSURFACE)
Background.blit(background, (0,0))
del background

logo_img_temp = pygame.image.load("graphics\\logo.png")
logo_img = pygame.Surface(logo_img_temp.get_size(), pygame.HWSURFACE)
logo_img.blit(logo_img_temp, (0,0))
del logo_img_temp

dialog_background = pygame.image.load("graphics\\dialog.png")
Dialog_Background = pygame.Surface(dialog_background.get_size(), pygame.HWSURFACE|pygame.SRCALPHA)
Dialog_Background.blit(dialog_background, (0,0))
Dialog_Background_Width, Dialog_Background_Height = Dialog_Background.get_size()
del dialog_background

end_background = pygame.image.load("graphics\\end_screen.png")
End_Background = pygame.Surface(end_background.get_size(), pygame.HWSURFACE)
End_Background.blit(end_background, (0,0))
del end_background

pygame.time.Clock()


def count_fps():
    global cSec, cFrame, FPS
    if cSec == time.strftime("%S"):
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")
        if FPS>0:
            Globals.deltatime = 1/FPS

# define a main function

     
# initialize the pygame module
pygame.init()
pygame.display.set_caption("Space Pyoneer")
 
# create a surface on screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.HWSURFACE|pygame.DOUBLEBUF)
 
player = Player("Rencu") 
player_w, player_h = player.width, player.height
player_x = (screen_width/2 - player_w/2 - Globals.camera_x) / 32
player_y = (screen_height/2 - player_h/2 - Globals.camera_y) / 32

robot1 = Robot1(name = "RC1", pos = (3300,800), dialog = Dialog(text=["Greetings, I'm RC Model #148.","Nice to meet you."]))
robot2 = Robot2(name = "RC2", pos = (2000,1900), dialog = Dialog(text=["Hi, I'm RC Model #253.","How long has it been...","...Since our departure?"]))
robot3 = Robot3(name = "RC3", pos = (1000,2800), dialog = Dialog(text=["Greetings, I'm RC Model #621.", "I am in for a repair soon.", "I hope I get a new display :)"]))
robot4 = Robot4(name = "RC4", pos = (900,450), dialog = Dialog(text=["..... (*mumble)", "...Where could it have gone?"]))

tincan1 = Tincan1(name = "TC1", pos = (1000,980), dialog = Dialog(text=["Hi, I'm TC Model #982!","... It sure is cold out here..."]))
tincan2 = Tincan2(name = "TC2", pos = (2500,2500), dialog = Dialog(text=["2/0=....", "...ZeroDivisionError~"]))
tincan3 = Tincan3(name = "TC3", pos = (3000,2500), dialog = Dialog(text=["Hi, I'm TC Model #21.....", ".... :3"]))

#INITIALIZE MUSIC
pygame.mixer.music.load("music\\Menu.mp3")
pygame.mixer.music.play(-1)

#INITIALIZE SOUNDS
#pygame.mixer.pre_init(44100, 16, 2, 4096) 
btnSound = pygame.mixer.Sound("sounds\\button-30.wav")


def Play():
    Globals.scene = "game"
    pygame.mixer.music.load("music\\Moonlight-Flying.mp3")
    pygame.mixer.music.play(-1)
def ExitGame():
    global running
    running = False
    
#Initialize GUI Buttons
btnPlay = Menu.Button(text = "Play", rect=(0,0,300,60), tag = ("menu", None))
btnPlay.Left = screen_width/2 - btnPlay.Width/2
btnPlay.Top = screen_height/2 - btnPlay.Height/2
btnPlay.Command = Play

btnExit = Menu.Button(text= "Exit", rect=(0,0,300,60), tag = ("menu", None))
btnExit.Left = btnPlay.Left
btnExit.Top = btnPlay.Top + btnExit.Height + 5
btnExit.Command = quit

menuTitle = Menu.Text(text = "Space Pyoneer", color=MC.Color.DarkCyan, font=Font.Large)
menuTitle.Left, menuTitle.Top = screen_width/2 - menuTitle.Width/2, 0

logo = Menu.Image(bitmap = logo_img)
# define a variable to control the main loop
running = True
 
# main loop
while running:

         
    # event handling, gets all event from the eventqueue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not Globals.dialog_open:
                Globals.camera_move = 1
                player.facing = "north"
            elif event.key == pygame.K_DOWN and not Globals.dialog_open:
                Globals.camera_move = 2
                player.facing = "south"
            elif event.key == pygame.K_LEFT and not Globals.dialog_open:
                Globals.camera_move = 3
                player.facing = "west"
            elif event.key == pygame.K_RIGHT and not Globals.dialog_open:
                Globals.camera_move = 4
                player.facing = "east"
            if event.key == pygame.K_ESCAPE:
                if Globals.dialog_open == False:
                    Globals.dialog_open = True
                    Globals.active_dialog = Dialog(text=["*Pause. Press [Esc] to unpause"])
                    for npc in NPC.AllNPCs:
                        npc.Timer.Pause()
                        npc.walking = False
                else:
                    Globals.dialog_open = False
                    Globals.active_dialog.Page = 0
                    Globals.active_dialog = None
                    for npc in NPC.AllNPCs:
                        if not npc.Timer.Active:
                            npc.Timer.Start()
                            
            if event.key == pygame.K_BACKSPACE:
                if Globals.dialog_open:
                    if(Globals.seed_flag == 1):
                        Globals.seed_flag = 0
                        Globals.dialog_open = False
                        if Globals.seed_count > 0:
                            Globals.seed_count -= 1
                        break
                    elif(Globals.crop_flag == 1):
                        Globals.crop_flag = 0
                        Globals.dialog_open = False
                        break
                    elif(Globals.grass_flag == 1):
                        Globals.grass_flag = 0
                        Globals.dialog_open = False
                        break   
                    
                    if Globals.active_dialog.Page < len(Globals.active_dialog.Text)-1:
                        Globals.active_dialog.Page += 1
                    else:
                        Globals.dialog_open = False
                        Globals.active_dialog.Page = 0
                        Globals.active_dialog = None
                        for npc in NPC.AllNPCs:
                            if not npc.Timer.Active:
                                npc.Timer.Start()
                                
            if event.key == pygame.K_SPACE:
                if Globals.dialog_open:
                    #HANDLE DISPLAY SEED TIME
                    if(Globals.seed_flag == 1):
                        Globals.seed_flag = 0
                        Globals.dialog_open = False
                        if(Globals.time_left==0):
                            pass
                        break
                    #HANDLE TAKE CROP
                    elif(Globals.crop_flag == 1):
                        Globals.crop_flag = 0
                        Globals.dialog_open = False
                        Globals.crop_count +=1
                        
                        break
                    #HANDLE PLANT SEED
                    elif(Globals.grass_flag == 1):
                        Globals.grass_flag = 0
                        Globals.dialog_open = False       
                        Globals.time_left = 3000
                        if Globals.seed_count >= 20:
                            Globals.seed_count = 20
                        else:
                            Globals.seed_count += 1
                        break   
                    
                    if Globals.active_dialog.Page < len(Globals.active_dialog.Text)-1:
                        Globals.active_dialog.Page += 1
                    else:
                        Globals.dialog_open = False
                        Globals.active_dialog.Page = 0
                        Globals.active_dialog = None
                        for npc in NPC.AllNPCs:
                            if not npc.Timer.Active:
                                npc.Timer.Start()
                
                else:
                    npc_priority = 0
                    for npc in NPC.AllNPCs:
                        npc_x = npc.X / 32
                        npc_y = npc.Y / 32
                        if player_x >= npc_x-2 and player_x<=npc_x+2 and player_y>=npc_y-2 and player_y<= npc_y+2:
                            #Player next to NPC
                            if player.facing == "north" and npc_y < player_y:
                                Globals.dialog_open = True
                                Globals.active_dialog = npc.dialog
                                npc.Timer.Pause()
                                npc.walking = False
                            elif player.facing == "south" and npc_y > player_y:
                                Globals.dialog_open = True
                                Globals.active_dialog = npc.dialog
                                npc.Timer.Pause()
                                npc.walking = False
                            elif player.facing == "west" and npc_x < player_x:
                                Globals.dialog_open = True
                                Globals.active_dialog = npc.dialog
                                npc.Timer.Pause()
                                npc.walking = False
                            elif player.facing == "east" and npc_x > player_x:
                                Globals.dialog_open = True
                                Globals.active_dialog = npc.dialog
                                npc.Timer.Pause()
                                npc.walking = False
                                
                            #play Robot sound
                            pygame.mixer.music.load("sounds\\Robot-blip.mp3")
                            pygame.mixer.music.play(1)
                            time.sleep(0.5)
                            pygame.mixer.music.load("music\\Moonlight-Flying.mp3")
                            pygame.mixer.music.play(-1)
                            npc_priority = 1
                    if npc_priority == 0:
                        if Tiles.Seed_At((round(player_x), round(player_y))):
                            Globals.dialog_open = True
                            Globals.seed_flag = 1
                        elif Tiles.Crop_At((round(player_x), round(player_y))):
                            Globals.dialog_open = True
                            Globals.crop_flag = 1
                        elif Tiles.Grass_At((round(player_x), round(player_y))):
                            Globals.dialog_open = True
                            Globals.grass_flag = 1
                        
                    
                                
        elif event.type == pygame.KEYUP:
            Globals.camera_move = 0
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if(event.button == 1):
                for btn in Menu.Button.All:
                    if btn.Tag[0] == Globals.scene and btn.Rolling:
                        if btn.Command != None:
                            btn.Command()
                        btnSound.play()
                        btn.Rolling = False
                        break
                    
    if Globals.scene == "game":     
        if Globals.camera_move == 1:
            if not Tiles.Blocked_At((round(player_x), math.floor(player_y))):
                Globals.camera_y += 200*Globals.deltatime      
        elif Globals.camera_move == 2:
            if not Tiles.Blocked_At((round(player_x), math.ceil(player_y))):
                Globals.camera_y -= 200*Globals.deltatime 
                
        elif Globals.camera_move == 3:
            if not Tiles.Blocked_At((math.floor(player_x), round(player_y))):
                Globals.camera_x += 200*Globals.deltatime
               
        elif Globals.camera_move == 4:
            if not Tiles.Blocked_At((math.ceil(player_x), round(player_y))):
                Globals.camera_x -= 200*Globals.deltatime
        #background   
        
        player_x = (screen_width/2 - player_w/2 - Globals.camera_x) / 32
        player_y = (screen_height/2 - player_h/2 - Globals.camera_y) / 32
        
        screen.blit(Background, (0,0))
        
        #LOAD TERRAIN
        
        
        screen.blit(terrain, (Globals.camera_x, Globals.camera_y))
        
        for npc in NPC.AllNPCs:
            npc.Render(screen)
            
        player.render(screen, (screen_width/2 - player_w/2, screen_height/2 - player_h/2))
        
        crop_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)
        crop_overlay = crop_font.render("Crops:"+str(Globals.crop_count), True, MC.Color.Goldenrod)
        screen.blit(crop_overlay, (120, 0))
        
        seed_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)
        seed_overlay = seed_font.render("Seeds:"+str(Globals.seed_count), True, MC.Color.Goldenrod)
        screen.blit(seed_overlay, (240, 0))
        
        crop_goal_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)
        crop_goal_overlay = crop_goal_font.render("Crop Goal:"+str(Globals.crop_goal), True, MC.Color.Goldenrod)
        screen.blit(crop_goal_overlay, (360, 0))
            
        
        if Globals.dialog_open:
            screen.blit(Dialog_Background, (screen_width /2 - Dialog_Background_Width/ 2, screen_height - Dialog_Background_Height - 2))
            if(Globals.grass_flag == 1):
                lines = "Plant/Take Seed?"
                screen.blit(Font.Default.render(lines, True, MC.Color.White), (130, (screen_height-Dialog_Background_Height) + 5))
                
            elif(Globals.seed_flag == 1):
                
                lines = "Seed harvest time left: " + str(round(Globals.time_left/100)) + " parasecs"
                screen.blit(Font.Default.render(lines, True, MC.Color.White), (130, (screen_height-Dialog_Background_Height) + 5))

            elif(Globals.crop_flag == 1):
                lines = "Take Crop?"
                screen.blit(Font.Default.render(lines, True, MC.Color.White), (130, (screen_height-Dialog_Background_Height) + 5))
            
            elif(Globals.active_dialog != None):
                lines = Globals.active_dialog.Text[Globals.active_dialog.Page]
                #for line in lines: 
                    #DRAW TEXT TO SCREEN
                screen.blit(Font.Default.render(lines, True, MC.Color.White), (130, (screen_height-Dialog_Background_Height) + 5))
                

    #show fps    
        
    elif Globals.scene == "menu":
        screen.fill(MC.Color.Fog)
        
        logo.Render(screen)
        menuTitle.Render(screen)
        
        for btn in Menu.Button.All:
            if btn.Tag[0] == "menu":
                btn.Render(screen)
        
    fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)
    fps_overlay = fps_font.render("FPS:"+str(FPS), True, MC.Color.Goldenrod)
    screen.blit(fps_overlay, (0,0))  

    if (Globals.time_left> 0):
        Globals.time_left -= 1
    if (Globals.time_left<= 0):
        Globals.time_left = 0  
        
    if Globals.crop_goal<=Globals.crop_count:
        screen.blit(End_Background, (100,200))
        pygame.display.update()    
        time.sleep(3)
        sys.exit()
      
    pygame.display.update()      
    
    count_fps()
        
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
