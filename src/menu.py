import const
from renderer import Renderer
from game import hand
import pygame, sys

class Menu(Renderer):
    """docstring for Menu"""

    def __init__(self):
        pygame.init()
        self.click = False
        self.renderer = Renderer()

    def main_menu(self):
        while True:
            self.renderer.screen.fill(const.color["black"])  # 背景底色為黑色
            self.renderer.draw_text('main menu', self.renderer.font, const.color["white"], self.renderer.screen, 500, 200) # 畫上text，位置設定在(500,200)

            # 取得滑鼠的座標，回傳一個tuple(x,y)
            mx, my = pygame.mouse.get_pos() 

            if  self.renderer.button_1.collidepoint((mx, my)):  # 若游標在button_1內
                if self.click:  # 若有點擊，進入遊戲
            #       game()
                    pass
            if  self.renderer.button_2.collidepoint((mx, my)):  # 若游標在button_2內
                if self.click:  # 若有點擊，進入遊戲
                  self.options()  # 進入option

            if 400 < mx < 600 and 500 < my < 550:  # 如果游標移到第一個選單方框內
                pygame.draw.rect(self.renderer.screen, const.color["red"],  self.renderer.button_1)  # 畫出紅色矩形
            else:
                pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.button_1)  # 畫上藍色矩形，傳入畫布、顏色、矩形

            if 400 < mx < 600 and 600 < my < 650:  # 如果游標移到第二個選單方框內
                pygame.draw.rect(self.renderer.screen, const.color["red"], self.renderer.button_2)  # 畫出紅色矩形
            else:
                pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.button_2)  # 畫上藍色矩形，傳入畫布、顏色、矩形

            self.renderer.draw_text('start', self.renderer.font, const.color["white"], self.renderer.screen, 500, 525)  # 在矩形上加上start的text
            self.renderer.draw_text('option', self.renderer.font, const.color["white"], self.renderer.screen, 500, 625) # 在矩形上加上option的text

            self.click = False


            for event in pygame.event.get():
                hand.event_handler(self, event)
                # if event.type == pygame.QUIT:
                #   pygame.quit()
                #   sys.exit()
                # if event.type == pygame.KEYDOWN:  # 若按下esc鍵，退出遊戲
                #   if event.key == pygame.K_ESCAPE:
                #       pygame.quit()
                #       sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:  # 若按下滑鼠鍵
                  if event.button == 1:
                      self.click = True  # 將click更新為1

            '''更改游標圖示'''
            pygame.mouse.set_visible(False)  # 隱藏原本的游標
            self.renderer.screen.blit(self.renderer.manual_cursor, (pygame.mouse.get_pos()))  # 改變游標

            pygame.display.update()  # 更新畫布

    # def mouse_position(self):
    #     mx, my = pygame.mouse.get_pos()  # 取得滑鼠的座標，回傳一個tuple(x,y)

    #     if 400 < mx < 600 and 500 < my < 550:  # 如果游標移到第一個選單方框內
    #         pygame.draw.rect(Renderer.screen, const.color["red"],  Renderer.button_1)  # 畫出紅色矩形
    #     else:
    #         pygame.draw.rect(Renderer.screen, const.color["blue"], Renderer.button_1)  # 畫上藍色矩形，傳入畫布、顏色、矩形

    #     if 400 < mx < 600 and 600 < my < 650:  # 如果游標移到第二個選單方框內
    #         pygame.draw.rect(Renderer.screen, const.color["red"], Renderer.button_2)  # 畫出紅色矩形
    #     else:
    #         pygame.draw.rect(Renderer.screen, const.color["blue"], Renderer.button_2)  # 畫上藍色矩形，傳入畫布、顏色、矩形

    def options(self):
        
        running = True #遊戲選項
        while running:
            self.renderer.screen.fill(const.color["black"])  # 設定option背景顏色
            self.renderer.draw_text('options', self.renderer.font, const.color["white"], self.renderer.screen, 500, 50)


            for event in pygame.event.get():
                hand.event_handler(self, event)

                # if event.type == QUIT:  # 關閉視窗
                #     pygame.quit()
                #     sys.exit()
                # if event.type == KEYDOWN:  # 若按下ESC鍵，退出option
                #     if event.key == K_ESCAPE:
            #         running = False

            pygame.display.update()


            
            