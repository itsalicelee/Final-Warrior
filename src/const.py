import pygame
# from renderer import Renderer

###########################################################
# 螢幕長尺寸
screen_width = 1000
screen_height = 750

map_x = 0
map_y = 0


# 設定常用顏色色碼
color = {"black": (0, 0, 0),
		 "white": (255, 255, 255),
		 "red": (255, 0, 0),
		 "blue": (0, 0, 255)}

###########################################################
# 設定主角初始位置
role_x = screen_width * 0.45
role_y = screen_height * 0.8

# 設定主角走動量初始值
x_change = 0 
y_change = 0

###########################################################
# 子彈初始速度(印象中是毫秒)
bullet_add_speed = 5


key = {"left": pygame.K_LEFT,
	   "right": pygame.K_RIGHT,
	   "up": pygame.K_UP,
	   "down": pygame.K_DOWN,
	   "esc": pygame.K_ESCAPE}

