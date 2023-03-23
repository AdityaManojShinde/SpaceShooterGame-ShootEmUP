# NOW THIS IS NOT A CALCULATOR

import pygame
import sys
import clock

screen_w = 600
screen_h = 600
color = (255,255,255)

screen = pygame.display.set_mode((screen_w,screen_h))
pygame.dispaly.set_caption("AMS")



def main():
    work = False
    while not work :

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()



        screen.fill(colour)




        pygame.display.flip()


    pygame.quit()









