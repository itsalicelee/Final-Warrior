import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame, const
class Boss(pygame.sprite.Sprite):
	def __init__(self, x = const.screen_width // 2, y = const.screen_height // 2, hp = 100):
		pygame.sprite.Sprite.__init__(self)
		self.hp = hp
		self.alive = True
		self.image = pygame.image.load("images/theme_ghost/boss1.png")
		pygame.transform.scale(self.image,(80,60))
		self.x = x
		self.y = y
		self.set_properties(x, y)

	def set_properties(self, x, y):
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y

	def get_loc(self):
		return self.rect.x, self.rect.y
	 
	def be_attacked(self):
		self.hp -= 1
		if self.hp <= 0:
			self.alive = False
	
	def if_still_alive(self):
		return self.alive
