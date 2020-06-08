import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import sys
from pygame.locals import *
import game
import menu
from game import Game
from menu import Menu

# ######################
if __name__ == "__main__":
	Menu()