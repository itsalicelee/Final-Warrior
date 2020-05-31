'''
這是負責存全部 constant 的檔案，請不要在裡面引用任何其他的class，避免circular import。
'''


# 使用 pygame 模組
import pygame

###########################################################
'''
螢幕顯示的參數
'''

# 全螢幕的長寬大小
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen_width = screen.get_width()
screen_height = screen.get_height()

# 設定常用顏色色碼
color = {
			"black": (0, 0, 0),
			"white": (255, 255, 255),
			"red": (255, 0, 0),
			"blue": (0, 0, 255)
}

###########################################################


###########################################################

# 設定Menu的選單位置，且button上的字可以隨著button位置置中
# menu button using screen info
menuButton = {
				"game": ( screen_width/2-200, screen_height*2/5, 400, 200), 
				"option": ( screen_width/2-200, screen_height*3/5, 400, 200), 
				"quit": ( screen_width/2-200, screen_height*4/5, 400, 200),
} 


# 設定遊戲暫停時的選單按鈕
pauseButton = {
				
				"resume": (400, 350, 60, 60),
				"option": (500, 350, 60, 60),
				"quit": (600, 350, 60, 60)
}
###########################################################

# 設定地圖的起始位置
map_x = 0
map_y = 0

#
now_x = 0
now_y = 0



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
############################################################

bonus_type = ["type1", "type2", "type3"]
###########################################################
key = {
		"left": pygame.K_LEFT,
		"right": pygame.K_RIGHT,
		"up": pygame.K_UP,
		"down": pygame.K_DOWN,
		"esc": pygame.K_ESCAPE,
		"space": pygame.K_SPACE,
		"pause": pygame.K_p,
		"game_over": pygame.K_g
}

