import pygame
import const 
import random 
from  renderer import Renderer

class Bonus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.renderer = Renderer()
        
        self.type = const.bonus_type[random.randint(0,len(const.bonus_type)-1)]
        self.surface = pygame.Surface([200, 200])
        

        bonus = pygame.image.load("images/bonus.png")  
        self.image = pygame.transform.scale(bonus, (150, 150))

        #self.surface = pygame.Surface([40,40]) # 繪製畫布
        #self.surface.fill((255,255,255,0))


        # self.x = random.randint(0, self.renderer.map_width)
        # self.y = random.randint(0, self.renderer.map_height)
        self.x = random.randint(0, 1200)               
        self.y = random.randint(0, 1200)


        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        

