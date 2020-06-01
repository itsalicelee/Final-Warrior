import pygame
import const 
import random

class Bonus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.type = const.bonus_type[random.randint(0,len(const.bonus_type)-1)]
        self.surface = pygame.Surface([200, 200])
        
        if self.type == "score":
            self.image = pygame.image.load("images/bonus/bonus_score.png")

        elif self.type == "shoes":
            self.image = pygame.image.load("images/bonus/bonus_shoe.png")

        elif self.type == "heart":
            self.image = pygame.image.load("images/bonus/bonus_heart.png")

        else:
            pass

        #self.surface = pygame.Surface([40,40]) # 繪製畫布
        #self.surface.fill((255,255,255,0))


        # self.x = random.randint(0, self.renderer.map_width)
        # self.y = random.randint(0, self.renderer.map_height)
        self.x = random.randint(0, 1200)               
        self.y = random.randint(0, 1200)


        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        

