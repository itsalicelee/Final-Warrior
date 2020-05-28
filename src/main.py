import pygame
import sys
import random
import math
from pygame.locals import *

import const
from renderer import Renderer
from sound import Sound
from bullet import Bullet
from brick import Brick
from menu import Menu
from game import hand

# #######################
class Game:
	"""docstring for game"""
	def __init__(self):
		pygame.init()
		self.mainClock = pygame.time.Clock()
		self.renderer = Renderer()
		self.menu = Menu()
		self.menu.main_menu()
		self.mainClock.tick(60)

	# def update(self):
	# 	self.mainClock.tick(60)
	# 	pygame.display.update()


# ######################
if __name__ == "__main__":
	Game()

