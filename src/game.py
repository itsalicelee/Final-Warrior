import pygame, sys
import const
from renderer import Renderer
# from menu import Menu


class hand:
    """docstring for game"""
    # def __init__(self):
    #     pygame.init()

    #     self.mainClock = pygame.time.Clock()
    #     self.renderer = Renderer()
    #     self.menu = Menu()
    #     self.menu.main_menu(self.renderer)
    #     self.mainClock.tick(60)

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


        