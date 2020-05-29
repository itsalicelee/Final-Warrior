import pygame, renderer
class Character(role_x, role_y):
    def __init__():
        self.image = pygame.image.loads('avatar')
        self.set_properties()

    def set_properties(self):
		self.rect = self.image.get_rect()
		self.origin_x = self.rect.centerx
		self.origin_y = self.rect.centery

    def charater_move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change
        
    def get_loc(self):
        return self.rect.x, self.rect.y