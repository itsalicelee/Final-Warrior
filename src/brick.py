import pygame
class Brick(pygame.sprite.Sprite): # 建立邊界 然後切記切記把它做成sprite
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,10])
        self.image.fill(color)
        self.rect = self.image.get_rect() #方形畫布get
        self.rect.x = x
        self.rect.y = y