import pygame, sys

class thing(pygame.sprite.Sprite):
    def __init__(self, startX,startY,radius,wallColor):
        super().__init__()
        self.image = pygame.Surface([radius*2, radius*2],pygame.SRCALPHA).convert_alpha()
        pygame.draw.rect(self.image,(wallColor),(0,0,radius*2,radius*2))
        self.rect = self.image.get_rect(topleft =(startX,startY))
        self.mask  = pygame.mask.from_surface(self.image)
        
    def move(self):
        t_f_list = {True : 1, False: 0}
        key_input = pygame.key.get_pressed()
        self.movex = (t_f_list[key_input[pygame.K_LEFT]] * -2) + (t_f_list[key_input[pygame.K_RIGHT]] * 2)
        self.movey = (t_f_list[key_input[pygame.K_UP]] * -2) + (t_f_list[key_input[pygame.K_DOWN]] * 2)

        self.rect.x += self.movex
        self.rect.y += self.movey
        
    def back(self):
        self.rect.x -= self.movex
        self.rect.y -= self.movey
