# Dawson Hoyle
# March 31 2023
# Basic PyGame Setup Code
import pygame,sys
from maze_img import Maze
from player import thing


pygame.init()
# Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

#Setup of Starting objects
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)

maze_map = pygame.image.load('maze_map.png')
map = Maze(0, 0, 500, 500, maze_map)
map_g = pygame.sprite.Group()
map_g.add(map)

player = thing(220, 220, 15,(82, 242, 114))
player_g = pygame.sprite.Group()
player_g.add(player)

pygame.display.set_caption("God make this my last maze game")
key_input = ""


def display():
    global circle
    window.fill((255,255,255)) #White background
    map_g.draw(window)
    player_g.draw(window)
            

display()
while True:
    player.move()
    display()
    if pygame.sprite.spritecollide(player, map_g, False, collided=pygame.sprite.collide_mask):
        player.back()
        display()

    for event in pygame.event.get():
    # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw