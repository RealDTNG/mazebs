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
cirx = 100
ciry = 100
key_input = ""
def display():
    window.fill((255,255,255)) #White background
    circle = pygame.draw.circle(window,(0,0,0),(cirx,ciry), 50)
    
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
            
test_list = {True : 1, False: 0}
 
while True:
    display()
    key_input = pygame.key.get_pressed()
    
    cirx += test_list[key_input[pygame.K_LEFT]] * -5
    cirx += test_list[key_input[pygame.K_RIGHT]] * 5
    ciry += test_list[key_input[pygame.K_UP]] * -5
    ciry += test_list[key_input[pygame.K_DOWN]] * 5


    gridHelp(window,500,500)
    for event in pygame.event.get():
    # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw