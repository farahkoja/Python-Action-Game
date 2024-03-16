#importing python libraries
import pygame
import random
import os
import sys
from os import path

#linking file paths with img folder
img_dir = path.join(path.dirname(__file__), 'img')

pygame.font.init()
#intialization of game
pygame.init()

#game's window dimensions 
WIDTH = 900
HEIGHT = 700
FPS = 60
#display of the screen window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#title of the game
pygame.display.set_caption('The Ultimate Adventure')
#updates part of the screen display
pygame.display.update()
#tracks time 
clock = pygame.time.Clock()

#Increments invaders in screen display
def newinvader():
    i = Invader()
    total_sprites.add(i)
    invaders.add(i)

#shield bar creation with constant variables of length and height
#pct variable decreases every time player collides with invader
def draw_shield(surf, x, y, pct):
    if pct < 0:
        pct = 0
    length = 100
    height = 20
    fill = (pct / 100) * length
    outline_rect = pygame.Rect(x, y, length, height)
    fill_rect = pygame.Rect(x, y, fill, height)
    pygame.draw.rect(surf, WHITE, fill_rect)
    pygame.draw.rect(surf, GREEN, outline_rect, 2)

#displays lives of player on screen
def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        #allows image to have x and y properties
        img_rect = img.get_rect()
        #makes black areas of heart img not visible
        img.set_colorkey(BLACK)
        #hearts are 30 pixels apart
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

#font of title and instructions        
font_name = pygame.font.match_font('Eight-bit dragon')

#displays title and instructions in the middle of screen
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    #allows image to have x and y properties
    text_rect = text_surface.get_rect()
    #location of text
    text_rect.midtop = (x, y)
    #displaying text to screen display
    surf.blit(text_surface, text_rect)
    



#global variables of colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (108, 169, 4)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
ORANGE = (255, 191, 0)
PURPLE = (160,32,240)



#class Game which contains the basic features of the game
class Game:
    def __init__(self):
        pygame.init()
        #the screen of the game
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        #caption of the game
        pygame.display.set_caption('The Ultimate Adventures')
        #the clock of the game
        self.clock = pygame.time.Clock()
        
#class Background for the background of the game
class Background(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite__init__(self)
        #the background image of the game
        self.image = forest_img
        #allows image to have x and y properties
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
#class Player for the player in the game
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #defines the size of the image of the player
        self.image = pygame.transform.scale(player_img, (50, 50))
        #makes black areas of player sprite sheet not visible
        self.image.set_colorkey(BLACK)
        #puts the player image into a rectangle
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        #determines the horizontal speed of player
        self.speedx = 0
        #determines the horizontal speed of player
        self.speedy = 0
        #used for frame rate
        self.frame = 0
        self.images = []
        self.shield = 100
        #determines how many lives does a player has
        self.lives = 3
        #used when the player collides with invader three times
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        #increases shield bar by 1
        self.power = 1
        #the duration of the powerup effect
        self.power_time = pygame.time.get_ticks()
    #updates players position and movement based on user’s input on the keyboard
    def update(self):
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
        #intializes speed
        self.speedx = 0 
        self.speedy = 0
        
        keystate = pygame.key.get_pressed()
        #when the key e is pressed, it moves up by 4
        if keystate[pygame.K_e]:
            self.speedy = -4
        #when the key x is pressed, it moves down by 4
        if keystate[pygame.K_x]:
            self.speedy = +4
        #when the key s is pressed, it moves left by 2
        if keystate[pygame.K_s]:
            self.speedx = -2
        #when the key d is pressed, it moves right by 2
        if keystate[pygame.K_d]:
            self.speedx = +2
        #position of player changes with its movement
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        #it stops the player from moving off the display screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    #shoots arrows from the archery gun class 
    def shoot(self):
        arrow = Archery_gun(self.rect.centerx, self.rect.top)
        total_sprites.add(arrow)
        arrows.add(arrow)
    #hides player from screen every time a heart disappears after an invader player collision
    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 50)

 
#class invader for invaders in the game
class Invader(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #invader images randomly chosen from a list containing all invader images
        self.type = random.choice(invader_images)
        self.image = self.type.copy()
        self.image = pygame.transform.scale(self.image, (70, 70))
        #allows image to have x and y properties
        self.rect = self.image.get_rect()
        #allows invaders to have random starting y positions
        self.rect.y = random.randrange(HEIGHT - self.rect.height)
        self.radius = 5
        #allows invaders to have random starting x positions
        self.rect.x = random.randrange(-100, -40)
        # moves the invaders right by the intial speedx set
        self.speedx = random.randrange(2, 8)
        self.frames = 0
        self.images = [invader_1_img]
        self.radius = int(self.rect.width * .85 / 2)
    def update(self):
        # x-coordinate changes as invader is moving
        self.rect.x += self.speedx
        # resets x-coordinate of the invader every time invader sprite hits the edge of the screen
        if self.rect.right > WIDTH + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.speedx = random.randrange(2, 8)
#creation of a shooting arrow sprite
class Archery_gun(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #image of arrow
        self.image = arrow_img
        self.image = pygame.transform.scale(arrow_img, (35, 12))
        #makes black areas of the arrow image disappear
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        #locating the arrow's starting position
        self.rect.bottom = y
        self.rect.centerx = x
        #arrow travel in horizontal direction by speed 6
        self.speedx = +6
    #updates the position of the arrow will its moving
    def update(self):
        self.rect.x += self.speedx
        #it initializes the position of arrow every time arrow touches edge of screen
        if self.rect.centerx < 0:
            self.kill()
            
#powerup class contains all missing objects of the game
class Powerup(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        # list that has different types of powerups that a player will randomly receive 
        self.type = random.choice(['healing potion', 'ruby', 'emerald', 'gem', 'shield'])
        self.image = missingobjects_images[self.type]
        #makes black areas of missing objects img not visible
        self.image.set_colorkey(BLACK)
        self.type = random.choice(['healing potion', 'ruby', 'emerald', 'gem', 'shield'])
        #allows image to have x and y properties
        self.rect = self.image.get_rect()
        #makes the position of the missing object in the center 
        self.rect.center = center
        #makes missing object move vertically by speed of 2.
        self.speedy = +2
    def update(self):
        #changes the missing object’s position while its moving
        self.rect.y += self.speedy
        #missing object disappears when it collides with the edge of the screen
        if self.rect.top > HEIGHT:
            self.kill()


#displays title and instructions in the beginning of the game and disappears when game starts
def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, 'The Ultimate Adventures', 74, WIDTH / 2,HEIGHT / 7)
    draw_text(screen, 'Instructions ', 44, WIDTH / 2, HEIGHT * 3 / 5)
    draw_text(screen, 'Press any key to begin', 24, WIDTH / 2, HEIGHT * 3 / 4.6)
    draw_text(screen, 'Press the E key to move up', 24, WIDTH / 2, HEIGHT * 3 / 4.3)
    draw_text(screen, 'Press the X key to move down', 24, WIDTH / 2, HEIGHT * 3 / 4.1)
    draw_text(screen, 'Press the S key to move left', 24, WIDTH / 2, HEIGHT * 3 / 3.9)
    draw_text(screen, 'Press the D key to move right', 24, WIDTH / 2, HEIGHT * 3 / 3.77)
    pygame.display.flip()
    #while loop allows the display of instructions when game restarts
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
    
     

#background image
background = pygame.image.load(path.join(img_dir, 'forest.png')).convert()
#allows image to have x and y properties
background_rect = background.get_rect()
DEFAULT_IMAGE_SIZE = (900, 700)
background = pygame.transform.scale(background, DEFAULT_IMAGE_SIZE)
forest_img = pygame.image.load(path.join(img_dir, 'forest.png')).convert()
#player images
player_img = pygame.image.load(path.join(img_dir, 'femalesprite.png')).convert()
#invader 1 image
invader_1_img = pygame.image.load(path.join(img_dir, 'invader 1.png')).convert()
#invader 2 image
invader_2_img = pygame.image.load(path.join(img_dir, 'invader 2.png')).convert()
#invader 3 image
invader_3_img = pygame.image.load(path.join(img_dir, 'invader 3.png')).convert()
#empty list of invader images
invader_images = []
#list of all invader images
invader_list = ['invader 1.png', 'invader 2.png','invader 3.png']
#randomly adds an invader image from the full invader list to the empty invader list to display it to screen
for img in invader_list:
    invader_images.append(pygame.image.load(path.join(img_dir, img)).convert())
#arrow image
arrow_img = pygame.image.load(path.join(img_dir, 'arrow.png')).convert()
#image of archery gun
archery_gun_img = pygame.image.load(path.join(img_dir, 'archery gun.png')).convert()
#image of hearts 
heart_img = pygame.image.load(path.join(img_dir, 'heart.png')).convert()
#dictionary of missing objects
missingobjects_images = {}
#ruby image is added to dictionary of missing objects
missingobjects_images['ruby'] = pygame.image.load(path.join(img_dir, 'item 1.png')).convert()
#size of ruby image is 35x35
missingobjects_images['ruby'] = pygame.transform.scale(missingobjects_images['ruby'], (35, 35))
#emerald image is added to dictionary of missing objects
missingobjects_images['emerald'] = pygame.image.load(path.join(img_dir, 'item 2.png')).convert()
#size of emerald image is 35x35
missingobjects_images['emerald'] = pygame.transform.scale(missingobjects_images['emerald'], (35, 35))
#gem image is added to dictionary of missing objects
missingobjects_images['gem'] = pygame.image.load(path.join(img_dir, 'item 3.png')).convert()
#size of gem image is 35x35
missingobjects_images['gem'] = pygame.transform.scale(missingobjects_images['gem'], (35, 35))
#healing potion image is added to dictionary of missing objects
missingobjects_images['healing potion'] = pygame.image.load(path.join(img_dir, 'item 4.png')).convert()
#size of healing potion image is 35x35
missingobjects_images['healing potion'] = pygame.transform.scale(missingobjects_images['healing potion'], (35, 35))
#shield image is added to dictionary of missing objects
missingobjects_images['shield'] = pygame.image.load(path.join(img_dir, 'item 5.png')).convert()
#size of shield image is 35x35
missingobjects_images['shield'] = pygame.transform.scale(missingobjects_images['shield'], (35, 35))


#game loop
game_over = True
running = True
missingobjects = pygame.sprite.Group()
#When game restarts, instructions are displayed in the start screen
while running:
    if game_over:
        show_go_screen()
        game_over = False
        #All sprite groups are initialized 
        total_sprites = pygame.sprite.Group()
        invaders = pygame.sprite.Group()
        arrows = pygame.sprite.Group()
        player = Player()
        total_sprites.add(player)
        #for loop displays invaders and adds them to invader group
        for i in range(7):
            newinvader()
            i = Invader()
            total_sprites.add(i)
            invaders.add(i)
        score = 0
    clock.tick(FPS)

#shoot arrows
#for loop checks if game is not running, if not it checks if the key for shooting arrows is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type  == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and pygame.K_a:
                player.shoot()

    #total_sprites group updates game state of sprites         
    total_sprites.update()
    # flip function updates all screen display 
    pygame.display.flip()

# check if arrow hits invaders
    # checks for collisions between invaders and arrows groups 
    attacks = pygame.sprite.groupcollide(invaders, arrows, True, True)
    for attack in attacks:
        # increments by attack.radius value from the invader class in the constructor method  
        score += attack.radius
        i = Invader()
        # added to total_sprites and invaders groups 
        total_sprites.add(i)
        invaders.add(i)
        #only 10% chance of a missing object to occur from an invader arrow collision
        if random.random() > 0.9:
            pow = Powerup(attack.rect.center)
            # added to total_sprites and missing objects sprite groups 
            total_sprites.add(pow)
            missingobjects.add(pow)
            
# checks for collisions between player and missing objects groups 
    attack = pygame.sprite.spritecollide(player, missingobjects, True)
    for attack in attacks:
        if attack.type == 'healing potion' or 'shield':
            #shield bar increases if player collides with healing potion of shield
            player.shield += random.randrange(10, 30)
        #if shield bar is full and player collides with missing objects then it stays the same.
        if player.shield >= 100:
            player.shield = 100
        else:
            pass     
#shield and lives
    # checks for collisions between invaders and players groups 
    attacks = pygame.sprite.spritecollide(player, invaders, True, pygame.sprite.collide_circle)
    for attack in attacks:
        #the percentage of the shield bar decreases by a value 
        player.shield -= attack.radius * 2
        newinvader()
        #one heart disappears every time percentage of shield bar is 0
        if player.shield <= 0:
           player.hide()
           player.lives -= 1
           player.shield = 100
    #game ends if player has no hearts left
    if player.lives == 0:
        game_over = True

    
#render
    #original background color of the game
    screen.fill(BLACK)
    #displays the background image
    screen.blit(background, background_rect)
    #displays total_sprites group to the screen
    total_sprites.draw(screen)
    #displays shield bar of width and height and what determines the pct ,is an attribute from player class 
    draw_shield(screen, 6, 6, player.shield)
    #displays lives as heart images at the right side of the screen and what determines the lives, is the lives from the player class 
    draw_lives(screen, WIDTH - 100, 5, player.lives, heart_img)
    #displays score which increments every time invader collides with an arrow.
    draw_text(screen, 'score:' +  str(score), 30, WIDTH /2, 10)
    # updates the entire screen surface of the game.
    pygame.display.flip()

#update
#Some of the window display screen is updated    
pygame.display.update()


#game ends when user exits
pygame.quit()  
