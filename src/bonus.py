import pygame, random
import const

class Bonus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        # 隨機挑選 bonus 種類，給予不同的權重
        self.index = random.randint(0, 100)
        if 0 <= self.index <= 60: 
            self.type = const.bonus_type[0]
        elif 60 < self.index <= 80:
            self.type = const.bonus_type[1]
        else:
            self.type = const.bonus_type[2]

        # bonus 的畫布大小
        self.surface = pygame.Surface([200, 200])
        
        # 根據不同的 bonus 載入對應的圖片
        if self.type == "score":
            self.image = pygame.image.load("images/bonus/bonus_score.png")

        elif self.type == "shoes":
            self.image = pygame.image.load("images/bonus/bonus_shoe.png")

        elif self.type == "heart":
            self.image = pygame.image.load("images/bonus/bonus_heart.png")

        else:
            pass

        # bonus 隨機出現的位置
        self.x = random.randint(0, 1200)               
        self.y = random.randint(0, 1200)


        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


        self.expire_time = 0
        

