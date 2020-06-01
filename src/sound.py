import pygame

class Sound:
	
	pygame.mixer.init()
	switchSound = pygame.mixer.Sound("music/switch.ogg")
	selectSound = pygame.mixer.Sound("music/select.wav")
	bonusSound = pygame.mixer.Sound("music/got_bonus.wav")
	#hpSound = pygame.mixer.Sound("music/hpSound.wav") 還沒找到適合的音效
	

	def __init__(self):
		# 啟動背景音樂
		#pygame.mixer.init()

		# 讀取背景音樂
		pygame.mixer.music.load("music/bgm.ogg")
		pygame.mixer.music.set_volume(float(0.7))  # 來設定播放的音量，音量value的範圍為0.0到1.0
		pygame.mixer.music.play(-1)
		

	def set_bgm(self, value):
		pygame.mixer.music.set_volume(value)  # 來設定播放的音量，音量value的範圍為0.0到1.0


	def get_volume(self):
		return pygame.mixer.music.get_volume()






