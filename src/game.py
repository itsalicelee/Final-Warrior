import pygame, sys
import const
from renderer import Renderer
from character import Character
# from menu import Menu


class Game:
    """docstring for game"""
    def __init__(self):
        pygame.init()

        self.mainClock = pygame.time.Clock()
        self.renderer = Renderer()
        self.character = Character()
        self.mainClock.tick(60)

    def game_start(self):
        self.renderer.screen.fill(const.color["black"])  # 遊戲的底圖顏色預設為黑色
        while True:
            self.renderer.draw_text('game', self.renderer.font, const.color["black"], self.renderer.screen, 500, 50)

            for event in pygame.event.get():
                self.event_handler(event)

            self.character.character_move(const.x_change, const.y_change)
            self.now_x, self.now_y = self.character.get_loc()
            self.renderer.rolling_map(self.now_x, self.now_y)

            self.renderer.screen.blit(self.renderer.photo_dct["bg"], (const.map_x, const.map_y))

            self.renderer.screen.blit(self.renderer.photo_dct["actorIMG"], (int(const.map_x + self.now_x), int(const.map_y + self.now_y)))
            print(self.now_x, self.now_y)


            pygame.display.update()


    def event_handler(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 鍵盤：按下按鍵
        if event.type == pygame.KEYDOWN:  
            # 若按下esc鍵，退出遊戲
            if event.key == const.key["esc"]:
                pygame.quit()
                sys.exit()

            # 若按下上下左右，改變人物方向
            elif event.key == const.key["left"]: 
                const.x_change = -5

            elif event.key == const.key["right"]:
                const.x_change = 5

            elif event.key == const.key["up"]:
                const.y_change = -5

            elif event.key == const.key["down"]:
                const.y_change = 5

        # 鍵盤：放掉按鍵
        if event.type == pygame.KEYUP:
            if event.key == const.key["left"] or event.key == const.key["right"]:
                const.x_change = 0

            if event.key == const.key["up"] or event.key == const.key["down"]:
                 const.y_change = 0 

        # 滑鼠：按下按鍵
        if event.type ==  pygame.MOUSEBUTTONDOWN:  
            if event.button == 1:
                click = True
    









