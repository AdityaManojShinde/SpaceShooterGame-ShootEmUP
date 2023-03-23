import pygame
import random 


red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)

screen_w = 600
screen_h = 600
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption('AMS WINDOW')
pygame.mouse.set_visible(False)



  

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # game logic
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    

    
    #all drawings
    screen.fill(white)
    

    pygame.draw.rect(screen,red,[x,y,50,50],0)


    
    pygame.display.flip()


pygame.quit()




