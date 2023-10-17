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
move_group = pygame.sprite.Group
maze_group = pygame.sprite.Group
font2= pygame.font.SysFont('Arial', 20)
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
henry= Player(40,40,35,35,"images/Smiley.jpg",2)
move_group.add(henry)
maze= Maze(WINDOW_WIDTH,WINDOW_HEIGHT,"images/maze.png")
maze_group.add(maze)
pygame.display.set_caption("Adventure")
def display():
    window.fill((255,255,255))
    #move_group.draw(window)
    maze_group.draw(window)
    #Placing Control Images and Text to help the player

    
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
    
    #move_group.move()
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
    