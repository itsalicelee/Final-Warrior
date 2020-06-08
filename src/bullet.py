import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame, math
import const
class Bullet(pygame.sprite.Sprite): #輸入代表這個類別是特殊的角色類別 

    def __init__(self, input_speed, input_x, input_y, radius, color):
        # 初始化 sprite   
        pygame.sprite.Sprite.__init__(self)

        self.speed = input_speed
        self.x = input_x
        self.y = input_y
        
        #image,rect不是自己定的變量 特殊的角色類別一定要有 image是角色類別的畫布 可以在上面畫東西 rect式畫布的區塊!!!
        self.image = pygame.Surface([radius*2,radius*2]) # 繪製畫布

        self.image.fill(const.color["white"]) # 畫布塗上背景色
        pygame.draw.circle(self.image, color, (radius,radius), radius, 0)  # 在畫布上畫圓
        self.rect = self.image.get_rect()  # 取得畫布的區塊
        self.rect.center = (input_x,input_y)  # 設置畫布區塊的中心點
        self.direction = random.randint(-180,180) # 初始化角度 讓他是一個隨機生成 這樣就會亂跑惹

    # 更新球的移動方式
    def update(self):
        radian = math.radians(self.direction) #數字轉角度才能用sin cos函數 
        self.dx = self.speed * math.cos(radian) # 讓速度跟著角度走 但其實如果沒有要碰撞就不需要
        self.dy = -self.speed * math.sin(radian)
        
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y