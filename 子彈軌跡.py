import pygame as pg
pg.init()

#設定視窗
width, height = 1000, 750                     
screen = pg.display.set_mode((width, height))   
pg.display.set_caption("game")         
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255,255,255))
ball_list = [] 
bossIMG = pg.image.load("/Users/huangziyong/Downloads/devil.png")
bossIMG = pg.transform.scale(bossIMG,(80,60))
clock = pg.time.Clock()   #建立時間元件
role_x, role_y = width * 0.45, height * 0.8
boss_rect = role_x, role_y
speed = 3
all_sprites = pg.sprite.Group()
class Ball():
    global role_x, role_y, screen, speed
    def __init__(self):
        self.ball1 = pg.Surface((20,20))
        self.ball1.fill((255,255,255))
        pg.draw.circle(self.ball1, (0,0,255), (10,10), 10, 0) 
        self.rect1 = self.ball1.get_rect()
        self.rect1.center = (role_x,role_y)
        self.x1, self.y1 = (role_x,role_y)
        
        self.ball2 = pg.Surface((20,20))
        self.ball2.fill((255,255,255))
        pg.draw.circle(self.ball2, (0,0,255), (10,10), 10, 0) 
        self.rect2 = self.ball1.get_rect()
        self.rect2.center = (role_x,role_y)
        self.x2, self.y2 = (role_x,role_y)
        
        self.ball3 = pg.Surface((20,20))
        self.ball3.fill((255,255,255))
        pg.draw.circle(self.ball3, (0,0,255), (10,10), 10, 0) 
        self.rect3 = self.ball3.get_rect()
        self.rect3.center = (role_x,role_y)
        self.x3, self.y3 = (role_x,role_y)
        
        self.ball4 = pg.Surface((20,20))
        self.ball4.fill((255,255,255))
        pg.draw.circle(self.ball4, (0,0,255), (10,10), 10, 0) 
        self.rect4 = self.ball4.get_rect()
        self.rect4.center = (role_x,role_y)
        self.x4, self.y4 = (role_x,role_y)
        self.speed = 3
    def move_ball1(self):
        self.x1 += speed
        self.y1 -= speed
        self.rect1.center = (self.x1, self.y1)
        if(self.rect1.left <= 0 or self.rect1.right >= screen.get_width()):
            self.rect1.center = (role_x,role_y)
            self.x1, self.y1 = (role_x,role_y)
    def move_ball2(self):
        self.x2 += speed
        self.y2 += speed
        self.rect2.center = (self.x2, self.y2)
        if(self.rect2.left <= 0 or self.rect2.right >= screen.get_width()):
            self.rect2.center = (role_x,role_y)
            self.x2, self.y2 = (role_x,role_y)
    def move_ball3(self):
        self.x3 -= speed
        self.y3 -= speed
        self.rect3.center = (self.x3, self.y3)
        if(self.rect3.left <= 0 or self.rect3.right >= screen.get_width()):
            self.rect3.center = (role_x,role_y)
            self.x3, self.y3 = (role_x,role_y)
    def move_ball4(self):
        self.x4 -= speed
        self.y4 += speed
        self.rect4.center = (self.x4, self.y4)
        if(self.rect4.left <= 0 or self.rect4.right >= screen.get_width()):
            self.rect4.center = (role_x,role_y)
            self.x4, self.y4 = (role_x,role_y)
s = Ball()
#關閉程式的程式碼
running = True
while running:
    clock.tick(30)        #每秒執行30次
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    s.move_ball1()
    s.move_ball2()
    s.move_ball3()
    s.move_ball4()
    screen.blit(bg, (0,0))
    screen.blit(bossIMG, (role_x, role_y))
    screen.blit(s.ball1, s.rect1.center)
    screen.blit(s.ball2, s.rect2.center)
    screen.blit(s.ball3,  s.rect3.center)
    screen.blit(s.ball4, s.rect4.center)
    pg.display.update()     #更新視窗
    
pg.quit()