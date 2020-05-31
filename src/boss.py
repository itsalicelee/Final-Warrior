import pygame
class Boss(pygame.sprite.Sprite):
	def __init__(self, x, y, hp = 100):
		pygame.sprite.Sprite.__init__(self)
		self.hp = hp
		self.alive = True
		self.image = pygame.image.load("images/bad.png")
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
