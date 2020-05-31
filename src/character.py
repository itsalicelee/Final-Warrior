import pygame, renderer
import area_setting as boundary
import const

class Character(pygame.sprite.Sprite):
    def __init__(self, hp = 30, alive = True):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/racecar.png")
        self.set_properties()

        self.rect = self.image.get_rect()

        # 設定人物的起始血量
        self.hp = hp
        # 預設人物為活著
        self.alive = alive


    def set_properties(self):
        self.rect = self.image.get_rect()
        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery


    # 判斷人物移動，如果碰到不能走的地方，速度變成零
    def character_move(self, x_change, y_change):

        self.rect.x += x_change
        # 判斷 x 方向有沒有碰到
        if pygame.sprite.spritecollide(self, boundary.group, False):
            self.rect.x -= x_change

        self.rect.y += y_change
        # # 判斷 y 方向有沒有碰到
        if pygame.sprite.spritecollide(self, boundary.group, False):
            self.rect.y -= y_change

    # 取得角色的位置
    def get_loc(self):
        return self.rect.x, self.rect.y

    

    