# this is just for practice window 
import pygame
import sys
import time

# variabes
black = (0,0,0)
white = (255,255,255)
screen_w = 500
screen_h = 500
Fps = pygame.time.Clock()

screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("experiment window".upper())


def draw_board():

    pygame.draw.line(screen,black,(screen_w/2-60,100),(screen_w/2-60,400),5)
    pygame.draw.line(screen,black,(screen_w/2,100),(screen_w/2,400),5)
    pygame.draw.line(screen,black,(80,screen_h/2+35),(400,screen_h/2+35),5)
    pygame.draw.line(screen,black,(80,screen_h/2-35),(400,screen_h/2-35),5)





def main():

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()





        screen.fill(white)
        # drawings goes here
       

        pygame.display.flip()
        Fps.tick(60)

    pygame.quit()


main()
















