import pygame, sys
import random
import os


#window creation
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('The Ultimate Adventures')
pygame.display.update()
clock = pygame.time.Clock()
gameQuit = False
while not gameQuit:
    for event in pygame.event.get():
        print(event)
pygame.quit()
quit()




#sprite folder
sprite_folder = os.path.dirname(__file__)
boy_folder = os.path.join(sprite_folder, 'boy')



WIDTH = 460
HEIGHT = 580
FPS = 60

#intialization 
pygame.init()
pygame.mixer.init()


#colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


# Level creation
class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.player_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
    def run(self):
        self.visible_sprites.draw(self.display_surface)

# Game creation
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('The Ultimate Adventures')
        self.clock = pygame.time.Clock()
        self.level = Level()
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill('blue')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)






# Sprite creation
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('C:\\Users\\OYO Arabia\\OneDrive\\Desktop\\Computing\\Python\\computer sci coursework\\boy\\sprite_walk_2.png').convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
    def control(self, x, y):
        self.movex += x
        self.movey += y

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

total_sprites = pygame.sprite.Group()
player = Player()
total_sprites.add(player)

#game loop



total_sprites.update()

screen.fill(BLACK)
total_sprites.draw(screen)

pygame.display.flip()

pygame.quit()


    
