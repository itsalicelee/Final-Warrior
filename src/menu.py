import const
from renderer import Renderer
import pygame, sys
from game import Game
from sound import Sound

class Menu():
    """docstring for Menu"""
    

    def __init__(self):
        pygame.init()
        self.click = False
        self.renderer = Renderer()
        self.game = Game()
        self.bgm = Sound()
        self.main_menu()
        

        #self.sound = Sound() 
        

    def main_menu(self):
        button = 0
        while True:
            pygame.mouse.set_visible(False)  # 隱藏原本的游標
            self.renderer.screen.fill(const.color["black"])  # 背景底色為黑色
            self.renderer.draw_text('main menu', self.renderer.font, const.color["white"], self.renderer.screen, 500, 200) # 畫上text，位置設定在(500,200)
            

            # 取得滑鼠的座標，回傳一個tuple(x,y)
            # mx, my = pygame.mouse.get_pos() 

            # if  self.renderer.button_1.collidepoint((mx, my)):  # 若游標在button_1內
            #     if self.click:  # 若有點擊，進入遊戲
            # #       game.game_start()
            #         pass
            # if  self.renderer.button_2.collidepoint((mx, my)):  # 若游標在button_2內
            #     if self.click:  # 若有點擊，進入遊戲
            #       self.options()  # 進入option
      
            # if 400 < mx < 600 and 500 < my < 550:  # 如果游標移到第一個選單方框內
            #     pygame.draw.rect(self.renderer.screen, const.color["red"],  self.renderer.button_1)  # 畫出紅色矩形
            # else:
            #     pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.button_1)  # 畫上藍色矩形，傳入畫布、顏色、矩形

            # if 400 < mx < 600 and 600 < my < 650:  # 如果游標移到第二個選單方框內
            #     pygame.draw.rect(self.renderer.screen, const.color["red"], self.renderer.button_2)  # 畫出紅色矩形
            # else:
            #     pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.button_2)  # 畫上藍色矩形，傳入畫布、顏色、矩形

            
            #self.renderer.draw_text('option', self.renderer.font, const.color["white"], self.renderer.screen, 500, 625) # 在矩形上加上option的text
            #self.renderer.draw_text('start', self.renderer.font, const.color["white"], self.renderer.screen, 500, 525)  # 在矩形上加上start的text
            
            #self.click = False
            pygame.draw.rect(self.renderer.screen, const.color["red"],  self.renderer.button_1)  # 一開始預設畫出start紅色矩形
            pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.button_2)  # 畫上藍色矩形，傳入畫布、顏色、矩形
            pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.button_3)  # 畫上藍色矩形，傳入畫布、顏色、矩形
            
            
            
            for event in pygame.event.get():

                #game.event_handler(self, event)
                # if event.type == pygame.QUIT:
                #     pygame.quit()
                #     sys.exit()
                if event.type == pygame.KEYDOWN:  # 若按下esc鍵，退出遊戲

                    if event.key == const.key["down"]:  # 若按下down
                        button += 1
                    if event.key == const.key["up"]:
                        button -= 1
                    if event.key == const.key["space"]:
                        if button % 3 == 0:
                            self.game.game_start()
                        if button % 3 == 1:
                            self.options()  # 進入option
                        if button % 3 ==  2:
                            pygame.quit()
                            sys.exit()
                    
            if button % 3 == 0:  # 選到start
                pygame.draw.rect(self.renderer.screen, const.color["red"],  self.renderer.button_1)  # 一開始預設畫出start紅色矩形
                pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.button_2)  # 畫上藍色矩形，傳入畫布、顏色、矩形
                pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.button_3)  # 畫上藍色矩形，傳入畫布、顏色、矩形

            if button % 3 == 1:  # 選到option 
                pygame.draw.rect(self.renderer.screen, const.color["blue"],  self.renderer.button_1)  # 一開始預設畫出start紅色矩形
                pygame.draw.rect(self.renderer.screen, const.color["red"], self.renderer.button_2)  # 畫上藍色矩形，傳入畫布、顏色、矩形
                pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.button_3)  # 畫上藍色矩形，傳入畫布、顏色、矩形
            if button % 3 == 2:  # 選到quit
                pygame.draw.rect(self.renderer.screen, const.color["blue"],  self.renderer.button_1)  # 一開始預設畫出start紅色矩形
                pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.button_2)  # 畫上藍色矩形，傳入畫布、顏色、矩形
                pygame.draw.rect(self.renderer.screen, const.color["red"], self.renderer.button_3)  # 畫上藍色矩形，傳入畫布、顏色、矩形
            




            
            # 畫矩形以及字
            #pygame.draw.rect(self.renderer.screen, const.color["red"],  self.renderer.button_1)  # 一開始預設畫出start紅色矩形
            self.renderer.draw_text('start', self.renderer.font, const.color["white"], self.renderer.screen, const.menuButton["game"][0]+0.5*(const.menuButton["game"][2]), const.menuButton["game"][1]+0.5*(const.menuButton["game"][3]))  # 在矩形上加上start的text

            #pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.button_2)  # 畫上藍色矩形，傳入畫布、顏色、矩形
            self.renderer.draw_text('option', self.renderer.font, const.color["white"], self.renderer.screen, const.menuButton["option"][0]+0.5*(const.menuButton["option"][2]), const.menuButton["option"][1]+0.5*(const.menuButton["option"][3])) # 在矩形上加上option的text

            #pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.button_3)  # 畫上藍色矩形，傳入畫布、顏色、矩形
            self.renderer.draw_text('quit', self.renderer.font, const.color["white"], self.renderer.screen, const.menuButton["quit"][0]+0.5*(const.menuButton["quit"][2]), const.menuButton["quit"][1]+0.5*(const.menuButton["quit"][3])) # 在矩形上加上option的text
            '''更改游標圖示'''
            # pygame.mouse.set_visible(False)  # 隱藏原本的游標
            # self.renderer.screen.blit(self.renderer.manual_cursor, (pygame.mouse.get_pos()))  # 改變游標

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
        button = 0

        running = True #遊戲選項
        while running:
            self.renderer.screen.fill(const.color["black"])  # 設定option背景顏色
            self.renderer.draw_text('options', self.renderer.font, const.color["white"], self.renderer.screen, 500, 50)

            pygame.draw.rect(self.renderer.screen, const.color["red"],  self.renderer.button_1)  # 一開始預設畫出start紅色矩形
            pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.button_2)  # 畫上藍色矩形，傳入畫布、顏色、矩形
            pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.button_3)  # 畫上藍色矩形，傳入畫布、顏色、矩形


            if button % 3 == 0:  # 選到start
                pygame.draw.rect(self.renderer.screen, const.color["red"],  self.renderer.button_1)  # 一開始預設畫出start紅色矩形
                pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.button_2)  # 畫上藍色矩形，傳入畫布、顏色、矩形
                pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.button_3)  # 畫上藍色矩形，傳入畫布、顏色、矩形

            if button % 3 == 1:  # 選到option 
                pygame.draw.rect(self.renderer.screen, const.color["blue"],  self.renderer.button_1)  # 一開始預設畫出start紅色矩形
                pygame.draw.rect(self.renderer.screen, const.color["red"], self.renderer.button_2)  # 畫上藍色矩形，傳入畫布、顏色、矩形
                pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.button_3)  # 畫上藍色矩形，傳入畫布、顏色、矩形
            if button % 3 == 2:  # 選到quit
                pygame.draw.rect(self.renderer.screen, const.color["blue"],  self.renderer.button_1)  # 一開始預設畫出start紅色矩形
                pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.button_2)  # 畫上藍色矩形，傳入畫布、顏色、矩形
                pygame.draw.rect(self.renderer.screen, const.color["red"], self.renderer.button_3)  # 畫上藍色矩形，傳入畫布、顏色、矩形
            

            self.renderer.draw_text('volume', self.renderer.font, const.color["white"], self.renderer.screen, const.menuButton["game"][0]+0.5*(const.menuButton["game"][2]), const.menuButton["game"][1]+0.5*(const.menuButton["game"][3]))  # 在矩形上加上start的text

            #pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.button_2)  # 畫上藍色矩形，傳入畫布、顏色、矩形
            self.renderer.draw_text('theme', self.renderer.font, const.color["white"], self.renderer.screen, const.menuButton["option"][0]+0.5*(const.menuButton["option"][2]), const.menuButton["option"][1]+0.5*(const.menuButton["option"][3])) # 在矩形上加上option的text

            #pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.button_3)  # 畫上藍色矩形，傳入畫布、顏色、矩形
            self.renderer.draw_text('main menu', self.renderer.font, const.color["white"], self.renderer.screen, const.menuButton["quit"][0]+0.5*(const.menuButton["quit"][2]), const.menuButton["quit"][1]+0.5*(const.menuButton["quit"][3])) # 在矩形上加上option的text          



            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  # 若按下ESC鍵，退出option
                    if event.key == pygame.K_ESCAPE:
                        self.main_menu()
                    if event.key == const.key["down"]:  # 若按下down
                        button += 1
                    if event.key == const.key["up"]:
                        button -= 1
                    if event.key == const.key["space"]:
                        if button % 3 == 0:  # 進入volume
                            self.volume()
                        if button % 3 == 1:  # 進入theme
                            pass  
                        if button % 3 ==  2:  # 回到main menu
                            self.main_menu()

            pygame.display.update()

    def volume(self):
        
        while True:
            self.renderer.screen.fill(const.color["black"])  # 設定option背景顏色
            self.renderer.draw_text('volume', self.renderer.font, const.color["white"], self.renderer.screen, 500, 50)
            

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  # 若按下ESC鍵，退出volume

                    
                    """音量有七段"""
                    if event.key == const.key["left"]:  # 若按下left，音量減小
                        if self.bgm.get_volume() < 0.1:
                            self.bgm.set_bgm(0.0)
                        else:
                            self.bgm.set_bgm(float(self.bgm.get_volume())-0.1)

                    if event.key == const.key["right"]:  # 若按下right，音量增大
                        if float(self.bgm.get_volume()) + 0.1 < 0.7:  # 不要讓音量太大 
                            self.bgm.set_bgm(float(self.bgm.get_volume())+ 0.1)

                    if event.key == const.key["esc"]:    # 若按下option，回到選單
                        self.options()
                    
            self.renderer.draw_text('set volume', self.renderer.font, const.color["white"], self.renderer.screen, 500, 200)
            
            pygame.display.update()
