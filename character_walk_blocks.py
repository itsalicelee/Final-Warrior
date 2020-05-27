import pygame

class Block(pygame.sprite.Sprite):
	def __init__(self,color, width = 300 ,height = 250):
		# 障礙物
		super(Block, self).__init__()
		self.image = pygame.Surface((width,height))
		self.image.fill((50,80,120))
		self.hspeed = 0
		self.vspeed = 0
		self.set_properties()

	def set_properties(self):
		self.rect = self.image.get_rect()
		self.origin_x = self.rect.centerx
		self.origin_y = self.rect.centery

	def change_speed(self, hspeed, vspeed):
		self.hspeed += hspeed
		self.vspeed += vspeed

	def set_posotion(self, x, y):
		self.rect.x = x - self.origin_x
		self.rect.y = y - self.origin_y

	def set_image(self, filename = None):
		if (filename != None):
			self.image = pygame.image.load(filename)
			self.set_properties()

	def update(self, collidable):
		self.rect.x += self.hspeed
		
		collision_list = pygame.sprite.spritecollide(self, collidable, False)

		for collided_object in collision_list:
			if (self.hspeed > 0):
				self.rect.right = collided_object.rect.left
			# 向右
			elif(self.hspeed < 0):
				self.rect.left = collided_object.rect.right
  			# 向左
		self.rect.y += self.vspeed

		collision_list = pygame.sprite.spritecollide(self, collidable, False)

		for collided_object in collision_list:
			if (self.vspeed > 0):
				self.rect.bottom = collided_object.rect.top
			# 向下
			elif(self.vspeed < 0):
				self.rect.top = collided_object.rect.bottom
			# 向上
vel = 10

if (__name__ == '__main__'):
	pygame.init()
	window_size = window_width, windiw_height = 1000, 750
	window = pygame.display.set_mode(window_size)
	
	clock = pygame.time.Clock()
	frame_per_second = 60

	block_group = pygame.sprite.Group()

	character = Block((0,0,0))
	character.set_image('koya.png')
	character.set_posotion(window_width/2, windiw_height/2)
	# 左上長方形
	block_1 = Block((0,0,0))
	block_1.set_posotion(150,125)
	# 右上
	block_2 = Block((0,0,0))
	block_2.set_posotion(850,125)
	# 左下
	block_3 = Block((0,0,0))
	block_3.set_posotion(150,625)
	# 右下
	block_4 = Block((0,0,0))
	block_4.set_posotion(850,625)
	# 左外
	block_5 = Block((0,0,0))
	block_5.set_posotion(-150,375)
	# 上外
	block_6 = Block((0,0,0))
	block_6.set_posotion(500,-125)
	# 右外
	block_7 = Block((0,0,0))
	block_7.set_posotion(1150,375)
	# 下外
	block_8 = Block((0,0,0))
	block_8.set_posotion(500,875)

	block_group.add(block_1, block_2, block_3,block_4, character)

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

		window.fill((61,93,154))

		character.update(collidable_objects)

		block_group.draw(window)
		pygame.display.update()
	pygame.quit()
