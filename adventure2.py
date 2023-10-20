#Name:
#Date:
#Basic PyGame Setup Code
import pygame,sys,time
from player import Player
from backround import Maze
from buttons import imagebutton
from static import stillimage
from text import customtext

pygame.init()
def swap():
    global done
    done=True
global done
fps = 30
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 800
move_group = pygame.sprite.Group()
maze_group = pygame.sprite.Group()
btn_group = pygame.sprite.Group()
trophy_goal=pygame.sprite.Group()
txt_group=pygame.sprite.Group()
start_group = pygame.sprite.Group()
btnstart=pygame.sprite.Group()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
font = pygame.font.SysFont('Consolas', 20)
henry= Player(40,33,25,25,"images/Smiley.jpg",5)
move_group.add(henry)
start= Maze(WINDOW_WIDTH,WINDOW_HEIGHT,"images/maze_back.png")
start_group.add(start)
maze= Maze(WINDOW_WIDTH,WINDOW_HEIGHT,"images/maze.png")
goal= stillimage(400,750,25,25,"images/goal.png")
trophy_goal.add(goal)
maze_group.add(maze)
btn_ext= imagebutton(440,20,100,50,"images/GREEM.png","images/619.png",exit)
btn_group.add(btn_ext)
btn_srt= imagebutton(280,250,150,70,"images/start.png","images/startclck.png",swap)
btnstart.add(btn_srt)
btn_exit= imagebutton(280,350,150,70,"images/ext.png","images/extclck.png",exit)
btnstart.add(btn_exit)
window.blit(font.render("Text you want to say", True, (0, 0, 0)), (50, 50))
pygame.display.set_caption("Adventure")

done=False
while not done:
    window.fill((255,255,255))
    start_group.draw(window)
    btnstart.draw(window)
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        btnstart.update(pos,event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(fps)
tutor=False    
while done and tutor:
    window.fill((255,255,255))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(fps)
def display():
    window.fill((255,255,255))
    maze_group.draw(window)
    move_group.draw(window)
    btn_group.draw(window)
    trophy_goal.draw(window)

def exit():
    pygame.quit()
    sys.exit()
    
while True:
    display()
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        btn_group.update(pos,event)
      # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
        key_input = pygame.key.get_pressed()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            #If they click the reset button the game will reset

            
                
        
    henry.move()
    if henry.check_hit(maze_group):
        henry.back()
        
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
    