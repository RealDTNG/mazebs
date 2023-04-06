#importing pygame
import pygame

#Starting x spot
x_loca = (location)

#Starting y spot
y_loca = (location)

# dic name--True=1----False=0----->Creating a dictionary that takes a true and false and retuns a 1 and 0 respectively
t_f_list = {True : 1, False: 0}

#value name---pygame check if keys down---->Create a variable that is set to all the key values to see if it is up or down via True and False respectively 
key_input = pygame.key.get_pressed()

#setting a variable named speed to what we want the speed of the object
speed = (speed_value)
 
#x-var---dic name-value name-----key Left---speed value--dic name-value name------key Right---speed value      
movex = (t_f_list[key_input[pygame.K_LEFT]] * -speed) + (t_f_list[key_input[pygame.K_RIGHT]] * speed)

#y-var---dic name-value name-----key Up---speed value--dic name-value name------key Down---speed value 
movey = (t_f_list[key_input[pygame.K_UP]] * -speed) + (t_f_list[key_input[pygame.K_DOWN]] * speed)

#x-location + x-speed = new x-location
x_loca += movex

#y-location + y-speed = new y-location
y_loca += movey