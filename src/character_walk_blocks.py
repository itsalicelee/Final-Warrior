import pygame

bg = pygame.image.load('1.1-4d046d33a07490f813867425851deff9.jpg')
# 障礙物和主角都被歸類為Block class(sprite屬性)
class Block(pygame.sprite.Sprite):
    def __init__(self,color = (50,80,120), width = 300 ,height = 250):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width,height))
        self.image.fill((50,80,120))
        self.hspeed = 0
        self.vspeed = 0
        self.set_properties()

    #原本位置（x,y座標為矩形中心）
    def set_properties(self):
        self.rect = self.image.get_rect()
        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery

    #水平、垂直速度  
    def change_speed(self, hspeed, vspeed):
        self.hspeed += hspeed
        self.vspeed += vspeed

    #矩形位置設定
    def set_position(self, x, y):
        self.rect.x = x - self.origin_x
        self.rect.y = y - self.origin_y
        window.blit(self.image,(self.rect.x, self.rect.y) )

    # 角色位置設定
    def move(self, x, y):
        window.blit(self.image,(self.rect.x, self.rect.y))

    # 如果有圖片就使用圖片，否則使用color
    def set_image(self, filename = None):
        if (filename != None):
            self.image = pygame.image.load(filename)
            self.set_properties()

    # 移動並測試碰撞
    def update(self, collidable):
        #左右移動時
        self.rect.x += self.hspeed
        
        collision_list = pygame.sprite.spritecollide(self, collidable, False)

        for collided_object in collision_list:
            #向右碰撞到障礙物的話
            if (self.hspeed > 0):
                #矩形的右側恆為角色之左側
                self.rect.right = collided_object.rect.left
            #向左碰撞到障礙物的話
            elif(self.hspeed < 0):
                #矩形的左側恆為角色之右側
                self.rect.left = collided_object.rect.right
        #垂直移動時
        self.rect.y += self.vspeed

        collision_list = pygame.sprite.spritecollide(self, collidable, False)

        for collided_object in collision_list:
            #向上碰撞到障礙物的話
            if (self.vspeed > 0):
                #矩形的下側恆為角色之上側
                self.rect.bottom = collided_object.rect.top
            #向下碰撞到障礙物的話
            elif(self.vspeed < 0):
                #矩形的上側恆為角色之下側
                self.rect.top = collided_object.rect.bottom
vel = 10

if (__name__ == '__main__'):
    pygame.init()
    window_size = window_width, windiw_height = 1000, 750
    window = pygame.display.set_mode(window_size)
    
    clock = pygame.time.Clock()
    frame_per_second = 60

    character = Block()
    character.set_image('racecar.png')
    character.set_position(window_width/2, windiw_height/2)
    # 左上長方形
    block_1 = Block()
    block_1.set_position(150,125)
    # 右上
    block_2 = Block()
    block_2.set_position(850,125)
    # 左下
    block_3 = Block()
    block_3.set_position(150,625)
    # 右下
    block_4 = Block()
    block_4.set_position(850,625)
    # 左外
    block_5 = Block()
    block_5.set_position(-150,375)
    # 上外
    block_6 = Block()
    block_6.set_position(500,-125)
    # 右外
    block_7 = Block()
    block_7.set_position(1150,375)
    # 下外
    block_8 = Block()
    block_8.set_position(500,875)

    # 所有block(障礙+邊界)
    collidable_objects = pygame.sprite.Group()
    collidable_objects.add(block_1,block_2,block_3,block_4,block_5,block_6,block_7,block_8)

    running = True

    while(running):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or \
            (event.type == pygame.KEYDOWN and \
                (event.key == pygame.K_ESCAPE or event.key == pygame.K_q)):
                running = False

            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_LEFT):
                    character.change_speed(-vel, 0)
                if (event.key == pygame.K_RIGHT):
                    character.change_speed(vel, 0)
                if (event.key == pygame.K_UP):
                    character.change_speed(0, -vel)
                if (event.key == pygame.K_DOWN):
                    character.change_speed(0, vel)
            if (event.type == pygame.KEYUP):
                if (event.key == pygame.K_LEFT):
                    character.change_speed(vel, 0)
                if (event.key == pygame.K_RIGHT):
                    character.change_speed(-vel, 0)
                if (event.key == pygame.K_UP):
                    character.change_speed(0, vel)
                if (event.key == pygame.K_DOWN):
                    character.change_speed(0, -vel) 

        clock.tick(50)
        # 更新畫布
        window.blit(bg,(0,0))

        #顯示矩形
        # 左上
        block_1 = Block((0,0,0))
        block_1.set_position(150,125)
        # 右上
        block_2 = Block((0,0,0))
        block_2.set_position(850,125)
        # 左下
        block_3 = Block((0,0,0))
        block_3.set_position(150,625)
        # 右下
        block_4 = Block((0,0,0))
        block_4.set_position(850,625)
        # 左外
        block_5 = Block((0,0,0))
        block_5.set_position(-150,375)
        # 上外
        block_6 = Block((0,0,0))
        block_6.set_position(500,-125)
        # 右外
        block_7 = Block((0,0,0))
        block_7.set_position(1150,375)
        # 下外
        block_8 = Block((0,0,0))
        block_8.set_position(500,875)
        
        character.update(collidable_objects)
        character.move(character.rect.x, character.rect.y)
        
        pygame.display.update()
    pygame.quit()
