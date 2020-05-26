#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame, random, math, time

class bullet(pygame.sprite.Sprite):#輸入代表這個類別是特殊的角色類別
    speed = 0
    x = 0
    y = 0
    dx = 0
    dy = 0
    def __init__(self, inputspeed, inputx, inputy, radius, color, direction):
        pygame.sprite.Sprite.__init__(self)  # 一定要有這行，但不要問我為啥 我也不知道
        self.speed = inputspeed
        self.x = inputx
        self.y = inputy
        # !!!image,rect不是自己定的變量特殊的角色類別一定要有 image是角色類別的畫布 可以在上面畫東西 rect式畫布的區塊!!!
        self.image = pygame.Surface([radius*2, radius*2])  # 繪製畫布
        self.image.fill((255, 255, 255))  # 畫布塗上背景色
        pygame.draw.circle(self.image, color, (radius,radius), radius, 0)#在畫布上畫圓
        self.rect = self.image.get_rect()  # 取得畫布的區塊
        self.rect.center = (inputx,inputy)  # 設置畫布區塊的中心點
        self.direction = direction#初始化角度 讓他是一個隨機生成 這樣就會亂跑惹
        
    def update(self):
        radian = math.radians(self.direction)  # 角度轉弧度 才能用sin cos函數 
        self.dx = self.speed * math.cos(radian)  # 讓速度跟著角度走 但其實如果沒有要碰撞就不需要
        self.dy = -self.speed * math.sin(radian)
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y

class brick(pygame.sprite.Sprite): # 建立邊界 然後切記切記把它做成sprite
     def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(color)
        self.rect = self.image.get_rect() #方形畫布get
        self.rect.x = x
        self.rect.y = y
class moveclip(pygame.sprite.Sprite): # 這邊是簡單的滑鼠點擊開始這樣
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > window.get_width() - self.rect.width:
            self.rect.x = window.get_width() - self.rect.width
pygame.init()
font = pygame.font.SysFont("SimHei", 20)   
bullet_add_speed = 10000  # 子彈生成速度 印象中是毫秒

window = pygame.display.set_mode((600, 400))  # 畫布大小
pygame.display.set_caption("Robert")
background = pygame.Surface(window.get_size())  # 畫布
background = background.convert()  # 可有可無
background.fill((255, 255, 255))  # 畫布上色
window.blit(background,(0,0))  # 把畫布貼在繪圖視窗window上
allsprite = pygame.sprite.Group()  # 角色群組變數
bricksprite = pygame.sprite.Group()# 一定要阿!!!不然沒辦法碰撞測試
controllersprite = pygame.sprite.Group() #同上
bulletsprite = pygame.sprite.Group()
# 把所有的元素都加進allsprite 方便等等一次叫出
controller = moveclip((255, 0, 0), 0, 350) # 鼠標操作
allsprite.add(controller) 
controllersprite.add(controller)
clock = pygame.time.Clock()
tick = 0

for j in range(0, 60): #建立邊界 然後把它放進brick和all的group，放進brick才好做碰撞測試
    i = 0
    thebrick = brick((0, 0, 0), j * 10 + 1, i * 10 + 1)
    bricksprite.add(thebrick)
    allsprite.add(thebrick)
for j in range(0, 60):
    i = 39
    thebrick = brick((0, 0, 0),j * 10 + 1, i * 10 + 1)
    bricksprite.add(thebrick)
    allsprite.add(thebrick)
for i in range(0, 40):
    j = 0
    thebrick = brick((0,0,0), j * 10 + 1, i * 10 + 1)
    bricksprite.add(thebrick)
    allsprite.add(thebrick)
for i in range(0,40):
    j = 59
    thebrick = brick((0, 0, 0), j * 10 + 1, i * 10 + 1)
    bricksprite.add(thebrick)
    allsprite.add(thebrick)
#for
direction = 0
playing = False  # playing true代表球正在動
run = True  # run false代表程式結束
while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 使用者者按x結束視窗
            running = False  # 跳出pygame
    button = pygame.mouse.get_pressed()
    # 按下滑鼠左鍵開始遊戲（求開始動）
    if button[0]:
        playing = True
    if playing:
        window.blit(background,(0, 0))  # 清除繪圖視窗window
        if tick % bullet_add_speed == 0: # 時間進行多少毫秒的時候出一次子彈
            direction += 22.5
            new_bul = (bullet(6,300,200,8,(0,0,255), direction)) # 子彈格式 ，這邊如果多弄幾個東東 就可以每隔多少秒弄出不同大小速度形狀的子彈
            if direction >= 360:
                direction = 0
            bulletsprite.add(new_bul)  # 更新敵機組
        bulletsprite.update()  # 刷新新的bulletgroup
        bulletsprite.draw(window)  # 畫到螢幕上
        # 這邊很關鍵，pygame內建很方便的碰撞測試分別有spritecollide(物件，物件group，group要不要消除)、groupcollide(物件1group，物件2group、物件1要不要消除，物件二要步要消除)
        # 以及 spritecollidiency(物件group,物件,物件要不要消除) 所以到時侯撞主角應該是用spritecollide來讓子彈group撞主角時消失
        hitbrick = pygame.sprite.groupcollide(bricksprite, bulletsprite, False, True)  # 改動TRUE，FALSE就可以消除不消除
        # 繪製所有的角色 球 磚塊 打版
        bulletsprite.update()
    allsprite.draw(window)
    pygame.display.update()
pygame.quit()


# In[ ]:




