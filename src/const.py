import pygame

# Renderer()

###########################################################
# 螢幕長尺寸
screen_width = 1000
screen_height = 750

# # 取得長寬資訊
# map_width = Renderer.bg.get_width()
# map_height = Renderer.bg.get_height()  

# 設定Menu的選單位置，且button上的字可以隨著button位置置中
# 矩形長200寬50，距離左邊邊界為400，距離上面邊界400
menuButton = {"game":(400, 400, 200, 50), "option":(400, 500, 200, 50), "quit":(400, 600, 200, 50)} 

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
	   "esc": pygame.K_ESCAPE,
	   "space": pygame.K_SPACE,
	   "pause": pygame.K_p}

