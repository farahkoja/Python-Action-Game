import pygame
import random
import os
import sys
from os import path


img_dir = path.join(path.dirname(__file__), 'img')

pygame.font.init()
#intialization 
pygame.init()
pygame.mixer.init()

#window creation
WIDTH = 900
HEIGHT = 700
FPS = 60







screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Ultimate Adventure')
pygame.display.update()
clock = pygame.time.Clock()
##gameQuit = False
##while not gameQuit:
##    for event in pygame.event.get():
##        print(event)
def newinvader():
    i = Invader()
    total_sprites.add(i)
    invaders.add(i)

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

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img.set_colorkey(BLACK)
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)
        
font_name = pygame.font.match_font('Eight-bit dragon')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
    

#sprite folder
##sprite_folder = os.path.dirname(__file__)
##boy_folder = os.path.join(sprite_folder, 'boy')




#colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (108, 169, 4)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
ORANGE = (255, 191, 0)
PURPLE = (160,32,240)



# Sprite creation
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('The Ultimate Adventures')
        self.clock = pygame.time.Clock()
##        self.level = Level()
##        background_image_1 = pygame.image.load('img/sprite_walk_2.png').convert()
        

class Background(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite__init__(self)
        self.image = forest_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
GRAVITY = 1
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT
jumping = False    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
##        player_image = pygame.image.load().convert()
        self.image = pygame.transform.scale(player_img, (50, 50)) 
        self.image.set_colorkey(BLACK)
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0
        self.frame = 0
        self.images = []
        self.shield = 100
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.item1_img = item1_img
        self.item2_img = item2_img
        self.item3_img = item3_img
        self.item4_img = item4_img
        self.power = 1
        self.power_time = pygame.time.get_ticks()
        self.rect.x = 0
        self.rect.y = 0
        self.jump_height = 20
        self.gravity = 1
        self.y_velocity = jump_height
        self.jumping = False
        self.player_y = HEIGHT - 50
        self.player_x = WIDTH - 50
    def update(self):
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
        self.speedx = 0 
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        #jump
        if keystate[pygame.K_e]:
            self.jumping = True
        if self.jumping:
            self.player_y -= self.y_velocity
            self.y_velocity -= self.gravity
            if self.y_velocity < -self.jump_height:
                self.jumping = False
                self.y_velocity = self.jump_height
                self.image = player_img.get_rect(center=(self.player_x, self.player_y))
            else:
                self.image = player_img.get_rect(center=(self.player_x, self.player_y))
                
        if keystate[pygame.K_x]:
            self.speedy = +4
        if keystate[pygame.K_s]:
            self.speedx = -2
        if keystate[pygame.K_d]:
            self.speedx = +2
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    def shoot(self):
        arrow = Archery_gun(self.rect.centerx, self.rect.top)
        total_sprites.add(arrow)
        arrows.add(arrow)
    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)

    
        
        
        

class Invader(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
##        self.type = random.choice(['invader1', 'invader2', 'invader3'])
        self.image = invader_1_img
        self.image = pygame.transform.scale(invader_1_img, (70, 70)) 
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(HEIGHT - self.rect.height)
        self.radius = 5
        self.rect.x = random.randrange(-100, -40)
        self.speedx = random.randrange(2, 8)
        self.frames = 0
        self.images = []
        self.radius = int(self.rect.width * .85 / 2)
##        self.rect.center = (WIDTH / 2, HEIGHT / 2)
##        self.rect.left = (WIDTH / 4, HEIGHT / 4)
        
##        self.image.set_colorkey(WHITE)    
    def update(self):
        self.rect.x += self.speedx
        if self.rect.right > WIDTH + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
##            self.rect.y = random.randrange(-100, -40)
            self.speedx = random.randrange(2, 8)
##    def invader_1(self):
##        self.image = pygame.image.self.load().convert()
##        self.speedx = +2
####    def invader_2(self):
####        self.image = pygame.image.self.load().convert()
####        self.speedx = +4
####    def invader_3(self):
####        self.image = pygame.image.self.load().convert()
####        self.speedx = +6
class Archery_gun(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = arrow_img
        self.image = pygame.transform.scale(arrow_img, (35, 12))     
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
##        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedx = +3
    def update(self):
        self.rect.x += self.speedx
        if self.rect.centerx < 0:
            self.kill()

class MissingObject(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['item 1.png', 'item 2.png', 'item 3.png', 'item 4.png'])
##        archery_image = pygame.image.self.load(r'C:\Users\OYO Arabia\OneDrive\Desktop\Computing\Python\computer sci coursework\img\archery gun.png').convert_alpha()
        self.image = missing_objects_images[self.type]
        self.image = pygame.transform.scale(item1_img, (35, 12))     
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
##        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
##        self.rect.center = center
        self.speedx = 3
        
    def update(self):
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT:
            self.kill()

class Shield(pygame.sprite.Sprite):
    def __init__(self, center):
         pygame.sprite.Sprite.__init__(self)
         self.image = pygame.transform.scale(shield_img, (20, 50)) 
         self.rect = self.image.get_rect()
         self.image.set_colorkey(BLACK)
         self.rect.center = (WIDTH / 2, HEIGHT / 2)
         self.speedx = 0
         self.speedy = 0
         self.frame = 0

def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, 'The Ultimate Adventure', 64, WIDTH / 2,HEIGHT / 4)
    draw_text(screen, 'Instructions ', 22, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, 'Press the S key to begin', 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
    
        


background = pygame.image.load(path.join(img_dir, 'forest.png')).convert()
background_rect = background.get_rect()
DEFAULT_IMAGE_SIZE = (900, 700)
background = pygame.transform.scale(background, DEFAULT_IMAGE_SIZE)
forest_img = pygame.image.load(path.join(img_dir, 'forest.png')).convert()
player_img = pygame.image.load(path.join(img_dir, 'femalesprite.png')).convert()
playerjump_img = pygame.image.load(path.join(img_dir, 'femalejump.png')).convert()
invader_1_img = pygame.image.load(path.join(img_dir, 'invader 1.png')).convert()
invader_2_img = pygame.image.load(path.join(img_dir, 'invader 2.png')).convert()
invader_3_img = pygame.image.load(path.join(img_dir, 'invader 3.png')).convert()
arrow_img = pygame.image.load(path.join(img_dir, 'arrow.png')).convert()
archery_gun_img = pygame.image.load(path.join(img_dir, 'archery gun.png')).convert()
item1_img = pygame.image.load(path.join(img_dir, 'item 1.png')).convert()
item2_img = pygame.image.load(path.join(img_dir, 'item 2.png')).convert()
item3_img = pygame.image.load(path.join(img_dir, 'item 3.png')).convert()
item4_img = pygame.image.load(path.join(img_dir, 'item 4.png')).convert()
heart_img = pygame.image.load(path.join(img_dir, 'heart.png')).convert()
missing_objects_images = {}
missing_objects_images['item 1'] = pygame.image.load(path.join(img_dir, 'item 1.png')).convert()
missing_objects_images['item 1'] = pygame.transform.scale(missing_objects_images['item 1'], (35, 35))
missing_objects_images['item 2'] = pygame.image.load(path.join(img_dir, 'item 2.png')).convert()
missing_objects_images['item 2'] = pygame.transform.scale(missing_objects_images['item 2'], (35, 35))
missing_objects_images['item 3'] = pygame.image.load(path.join(img_dir, 'item 3.png')).convert()
missing_objects_images['item 3'] = pygame.transform.scale(missing_objects_images['item 3'], (35, 35))
missing_objects_images['item 4'] = pygame.image.load(path.join(img_dir, 'item 4.png')).convert()
missing_objects_images['item 4'] = pygame.transform.scale(missing_objects_images['item 4'], (35, 35))



#game loop
game_over = True
running = True
while running:
    if game_over:
        show_go_screen()
        game_over = False
        total_sprites = pygame.sprite.Group()
        invaders = pygame.sprite.Group()
        arrows = pygame.sprite.Group()
        missing_objects = pygame.sprite.Group()
        player = Player()
        total_sprites.add(player)
        for i in range(7):
            newinvader()
            
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type  == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and pygame.K_a:
                player.shoot()

            
        
        
            
                
                
    total_sprites.update()
    pygame.display.flip()

    attacks = pygame.sprite.groupcollide(invaders, arrows, True, True)
    for attack in attacks:
        if random.random() > 0.85:
            missingobjects = MissingObject(attack.rect.center)
            total_sprites.add(missingobjects)
            missing_objects.add(missingobjects)    
        newinvader()
        
        
    

    attacks = pygame.sprite.spritecollide(player, invaders, True, pygame.sprite.collide_circle)
    for attack in attacks:
        player.shield -= attack.radius * 2
        newinvader()
        if player.shield <= 0:
           player.hide()
           player.lives -= 1
           player.shield = 100


    attacks = pygame.sprite.spritecollide(player, missing_objects, True)
    for attack in attacks:
        if attack.type == 'item 1':
            player.shield += random.randrange(11, 31)
            if player.shield >= 80:
                player.shield = 80
        if attack.type == 'item 2':
            player.shield += random.randrange(11, 31)
            if player.shield >= 80:
                player.shield = 80
        if attack.type == 'item 3':
            player.shield += random.randrange(11, 31)
            if player.shield >= 80:
                player.shield = 80
        if attack.type == 'item 4':
            player.shield += random.randrange(11, 31)
            if player.shield >= 80:
                player.shield = 80
        

    if player.lives == 0:
        game_over = True

    
        
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    total_sprites.draw(screen)
    draw_shield(screen, 6, 6, player.shield)
    draw_lives(screen, WIDTH - 100, 5, player.lives, heart_img)
    pygame.display.flip()
    
#jump event








    
   
#score board
##font_name = pygame.font.match_font('Eight-bit dragon')
##def draw_text(surf, text, size, x, y):
##    font = pygame.font.Font(font_name, size)
##    text = font.render(text, True, WHITE)
##    text_rect = text.get_rect()
##    text_rect.midtop = (x, y)
##    surf.blit(text, text_rect)

pygame.display.update()



pygame.quit()  
