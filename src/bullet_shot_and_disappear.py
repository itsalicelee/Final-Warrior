import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame,random,math,time, const

class bullet(pygame.sprite.Sprite):#輸入代表這個類別是特殊的角色類別

    def __init__(self,inputspeed,inputx,inputy,radius,color, direction):
        pygame.sprite.Sprite.__init__(self)#一定要有這行，但不要問我為啥 我也不知道

        self.speed = inputspeed
        self.x = inputx
        self.y = inputy
        #!!!image,rect不是自己定的變量 特殊的角色類別一定要有 image是角色類別的畫布 可以在上面畫東西 rect式畫布的區塊!!!
        self.image = pygame.image.load("images/theme_ghost/bullet1.png")
        self.image = pygame.transform.scale(self.image, (int(2000*0.01), int(2000*0.01)))
        self.rect = self.image.get_rect()#取得畫布的區塊
        self.rect.x = self.x
        self.rect.y = self.y

        self.rect.center = (inputx, inputy)#設置畫布區塊的中心點
        self.direction = direction
        
    def update(self):
        radian = math.radians(self.direction)#角度轉弧度 才能用sin cos函數 
        self.dx = self.speed * math.cos(radian) # 讓速度跟著角度走 但其實如果沒有要碰撞就不需要
        self.dy = -self.speed * math.sin(radian)
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y
      
class brick(pygame.sprite.Sprite): # 建立邊界 然後切記切記把它做成sprite
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,10])
        self.image.fill(color)
        self.rect = self.image.get_rect() #方形畫布get
        self.rect.x = x
        self.rect.y = y
