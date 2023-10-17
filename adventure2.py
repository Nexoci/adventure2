#Name:
#Date:
#Basic PyGame Setup Code
import pygame,sys,time
from player import Player
from backround import Maze
import buttons

pygame.init()
fps = 30
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 800
move_group = pygame.sprite.Group()
maze_group = pygame.sprite.Group()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
font2= pygame.font.SysFont('Arial', 20)
henry= Player(40,33,25,25,"images/Smiley.jpg",5)
move_group.add(henry)
maze= Maze(WINDOW_WIDTH,WINDOW_HEIGHT,"images/maze.png")
maze_group.add(maze)
btn_ext=()
pygame.display.set_caption("Adventure")
def display():
    window.fill((255,255,255))
    maze_group.draw(window)
    move_group.draw(window)

    
while True:
    display()
    for event in pygame.event.get():
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
    