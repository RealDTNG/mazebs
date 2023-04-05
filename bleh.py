# Dawson Hoyle
# March 31 2023
# Basic PyGame Setup Code
import pygame,sys


pygame.init()
# Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
#Setup of Starting objects
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("God make this my last maze game")
cirx = 250
ciry = 250
#Done walls
WALLS = []
WALLS.append((200, 220, 20, 71))
WALLS.append((200, 200, 150, 20))
WALLS.append((200, 276, 70, 20))
WALLS.append((330, 276, 20, 76))
WALLS.append((200, 352, 150, 20))
#To do walls
WALLS.append((0, 0, 0, 0))
WALLS.append((0, 0, 0, 0))
WALLS.append((0, 0, 0, 0))
WALLS.append((0, 0, 0, 0))
WALLS.append((0, 0, 0, 0))
WALLS.append((0, 0, 0, 0))
WALLS.append((0, 0, 0, 0))
WALLS.append((0, 0, 0, 0))
WALLS.append((0, 0, 0, 0))
WALLS.append((0, 0, 0, 0))

key_input = ""
def display():
    global circle
    window.fill((255,255,255)) #White background
    for wall in WALLS:
        pygame.draw.rect(window,(247, 72, 72), wall)
    circle = pygame.draw.circle(window,(82, 242, 114),(cirx,ciry), 15)
    
    
def gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT):
        spacer = 10
        font = pygame.font.SysFont('Consolas', 10)
        for gridX in range(0, WINDOW_WIDTH, spacer):        
            window.blit(pygame.transform.rotate(font.render(str(gridX), True, (0, 0, 0)),90),(gridX,0))
        for gridY in range(0, WINDOW_HEIGHT, spacer):
            window.blit(font.render(str(gridY), True, (0, 0, 0)), (0, gridY))
        for gridX in range(0, WINDOW_WIDTH, spacer):
            pygame.draw.line(window,(255,0,0),(gridX,0),(gridX,WINDOW_HEIGHT))
        for gridY in range(0, WINDOW_HEIGHT, spacer):
            pygame.draw.line(window,(255,0,0),(0,gridY),(WINDOW_WIDTH,gridY)) 
            
            
t_f_list = {True : 1, False: 0}

display()
while True:
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_r]:
        cirx = 250
        ciry = 250
    movex = (t_f_list[key_input[pygame.K_LEFT]] * -2.5) + (t_f_list[key_input[pygame.K_RIGHT]] * 2.5)
    movey = (t_f_list[key_input[pygame.K_UP]] * -2.5) + (t_f_list[key_input[pygame.K_DOWN]] * 2.5)
    if movey and movex != 0:
        movex = movex/1.7
        movey = movey/1.7  
    cirx += movex
    ciry += movey  
    if 0 > cirx:
        cirx = 1
    elif cirx > 500:
        cirx = 499
    if 0 > ciry:
        ciry = 1
    elif ciry > 500:
        ciry = 499
   
    display()
    for wall in WALLS:
        if circle.colliderect(wall):
            cirx -= movex
            ciry -= movey
            display()


    gridHelp(window,500,500)
    for event in pygame.event.get():
    # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw