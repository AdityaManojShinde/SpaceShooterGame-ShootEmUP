import pygame
import random
import sys

pygame.init()
pygame.mixer.init()
# colors

red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
yello = (255,255,0)

# variables
screen_w = 1000
screen_h = 800
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption('SPACE SHOOTER made by aditya shinde')
clock = pygame.time.Clock()
en = pygame.image.load('enemy.png')
'''
list_enemy = []
for i in list_enemy:
    x = random.randrange(35,150)
    y = random.randrange(35,150)
    list_enemy.append(x,y)
'''

enemy = pygame.transform.scale(en,[150,150])

sh = pygame.image.load('ship.PNG')
ship = pygame.transform.scale(sh,[100,100])


bk =pygame.image.load('space_backg.png')
background = pygame.transform.scale(bk,[screen_w,screen_h])


bu = pygame.image.load('bullet.png')
bullet_img = pygame.transform.scale(bu,[10,35]).convert()

shoot_sound = pygame.mixer.Sound('laser.wav')
blast_sound = pygame.mixer.Sound('explosion.wav')

pygame.mixer.music.load('back_music.wav')
pygame.mixer.music.set_volume(0.4)

# get mouse cursor invisible when on screen
pygame.mouse.set_visible(False)

# functons and classes
font_name = pygame.font.match_font('arial')
back_g = pygame.image.load('background.jpg')
new_background = pygame.transform.scale(back_g,[screen_w,screen_h])

def draw_text(surf,text,size,x,y):

    font = pygame.font.Font(font_name,size)

    text_surface = font.render(text,True,white)

    text_rect = text_surface.get_rect()

    text_rect.midtop = (x,y)

    surf.blit(text_surface,text_rect)



class Ship(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = ship

        self.rect = self.image.get_rect()
        # make a circle for collusion
        self.radius = 20
        #pygame.draw.circle(self.image,red,self.rect.center,self.radius)

        self.rect.x = screen_w / 2

        self.rect.y = screen_h -  110

        self.helth = 100

        self.life = 3

    def update(self):
        pos = pygame.mouse.get_pos()

        self.rect.centerx = pos[0]
        # set boundry
        if self.rect.right > screen_w:

            self.rect.right = screen_w
        elif self.rect.left < 0:

            self.rect.left = 0

    def shoot(self):
        
        bullet = Bullet(self.rect.centerx,self.rect.top)

        all_sprite.add(bullet)

        bullet_group.add(bullet)

        shoot_sound.play()

    




class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = enemy 
        self.rect = self.image.get_rect()
        # make a circle for collusion
        self.radius = int(self.rect.width/2)
        #pygame.draw.circle(self.image,red,self.rect.center,self.radius)

        # set random places and speed for enemy
        self.rect.x = random.randrange(screen_w - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(1,3)
        self.speedx = random.randrange(-3,3)


    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # reset the enemy to the top
        if self.rect.top > screen_h + 10 or self.rect.left < -25 or self.rect.right > screen_w + 10: 

            self.rect.x = random.randrange(screen_w - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,8)

       


    def enemy_size(self):
        x = random.randrange(50,200)
        y = random.randrange(50,200)
        big_enemy = pygame.transform.scale(enemy,[x,y])
        self.radius = int(self.rect.width/2)
        self.image = big_enemy




# bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = bullet_img
        #self.image.fill(green)    
        self.rect = self.image.get_rect()
        # set the position of the bulllet   
        self.rect.bottom = y 
        self.rect.centerx = x
        self.speedy = -10

    def update(self):

        self.rect.y += self.speedy
        # kill the bullet if it move top of the screen
        if self.rect.bottom < 0:
            self.kill()


def draw_helth(srf,x,y,hel): 

    if hel < 0:
        hel = 0
    bar_length = 200
    bar_hight = 10
    color =  green
    fill = (hel/100)*bar_length
    out_rect = pygame.Rect(x,y,bar_length,bar_hight)
    fill_rect = pygame.Rect(x,y,fill,bar_hight)
    if hel < 100:
        color = yello
    
    pygame.draw.rect(srf,color,fill_rect)
    pygame.draw.rect(srf,white,out_rect,2)





# stars animation

def star_animation():

    for i in range(50):

        x = random.randrange(0,screen_w)
        y = random.randrange(0,screen_h)

        pygame.draw.circle(screen,white,[x,y],2)

def controler():
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    pygame.draw.circle(screen,white,[x,y],30)
    pygame.draw.circle(screen,blue,[x,y],25)
   
def new_group():

    e = Enemy()
    e.enemy_size()
    all_sprite.add(e)
    enemy_group.add(e)




def ship_lives():
    new_ship = pygame.transform.scale(ship,[80,80])
    '''
    
    ''' 
    if player.life == 3:   
        screen.blit(new_ship,[screen_w-100,10]),
        screen.blit(new_ship,[screen_w-200,10]),
        screen.blit(new_ship,[screen_w-300,10]),   
    
        
    elif player.life == 2:    
        #screen.blit(new_ship,[screen_w-100,10]),
        screen.blit(new_ship,[screen_w-200,10]),
        screen.blit(new_ship,[screen_w-300,10]),   
    
    elif player.life == 1:     
        #screen.blit(new_ship,[screen_w-100,10]),
        #screen.blit(new_ship,[screen_w-200,10]),
        screen.blit(new_ship,[screen_w-300,10]),   
    
    
player = Ship()
# groups to store enemy and player sprites
bullet_group = pygame.sprite.Group()
all_sprite = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
all_sprite.add(player)

# set enemy number
for i in range(8):
    new_group()


score = 0
pygame.mixer.music.play(loops=-1)
# main loop
while True:
 
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                player.shoot()
               



   


    all_sprite.update()
    # all function goes here

    # check if enemy hit the player

    hits = pygame.sprite.groupcollide(enemy_group,bullet_group,True,True)
    # create new group after being hit
    for hit in hits:

        score += 10
        blast_sound.play()
        new_group()
    
    hits = pygame.sprite.spritecollide(player,enemy_group,True, pygame.sprite.collide_circle)

    # if enemy hits player exit
    for hit in  hits:
        
        player.helth  -= 10
        blast_sound.play()
        new_group()
        if player.helth <= 0:
            player.life -= 1
            if player.life > 0:
                player.helth = 100
            elif player.life == 0:
                sys.exit()

    screen.fill(black)
    # all drawings goes here
    screen.blit(background,[0,0])
    
    star_animation()
    all_sprite.draw(screen)
    # draw text
    draw_text(screen,str(score),30,screen_w/2,10)
    draw_helth(screen,5,5,player.helth)
    ship_lives()
    controler()
    
  

    pygame.display.flip()
    clock.tick(60)



pygame.quit()