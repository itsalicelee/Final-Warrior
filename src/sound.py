import pygame

class Sound:
	def __init__(self):
		# 啟動背景音樂
		pygame.mixer.init()

		# 讀取背景音樂
		self.bgm = pygame.mixer.music.load("music/bgm.ogg")
		self.play_bgm()

	def play_bgm(self):
		pygame.mixer.music.set_volume(0.1)  # 來設定播放的音量，音量value的範圍為0.0到1.0
		pygame.mixer.music.play(-1)  # 若為-1則會無限輪迴播放



