import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import const
from renderer import Renderer
import pygame, sys
from game import Game
from sound import Sound
import time 
class Menu():
    """docstring for Menu"""
    

    def __init__(self):
        pygame.init()
        self.click = False
        self.renderer = Renderer()
        # self.game = Game()
        self.sound = Sound()
        self.main_menu()
        

    def main_menu(self):
        button = 0
        start_y = 1000
        about_y = 1000
        quit_y = 1000
        imagex = const.menuButton["game"][0]
        start_btn_pos = const.screen_height*2/5
        about_btn_pos = const.screen_height*3/5
        quit_btn_pos = const.screen_height*4/5 
        # 產生按鈕
        no_startBtn = self.renderer.no_start
        no_aboutBtn = self.renderer.no_about
        no_quitBtn = self.renderer.no_quit
        yes_startBtn = self.renderer.yes_start
        yes_aboutBtn = self.renderer.yes_about
        yes_quitBtn = self.renderer.yes_quit

        click = False



        while True:

            pygame.mouse.set_visible(False)  # 隱藏原本的游標
            self.renderer.screen.fill(const.color["black"])  # 背景底色為黑色
            #self.renderer.screen.blit(self.renderer.photo_dct["main_menu"], (0, 0))
            temp_menu = pygame.transform.scale(self.renderer.photo_dct["main_menu"], (const.screen_width,const.screen_height))
            #self.renderer.draw_text('main menu', self.renderer.font, const.color["white"], self.renderer.screen, const.screen_width/2, const.screen_height/5) # 畫上text，位置設定在螢幕的中間
            self.renderer.screen.blit(temp_menu,(0,0))
            
            if not click:
                ''' 按鈕的動畫，但目前無法跟變色同時出現，所以先註解掉'''
                if start_y > start_btn_pos:
                    delta = (start_y - start_btn_pos)*0.05
                    start_y -= delta
                

                if about_y > about_btn_pos:
                    delta = (about_y - about_btn_pos)*0.05
                    about_y -= delta

                if quit_y > quit_btn_pos:
                    delta = (about_y - about_btn_pos)*0.05
                    quit_y -= delta

                # 顯示按鈕動畫
                self.renderer.screen.blit(yes_startBtn, (imagex, start_y))
                self.renderer.screen.blit(no_aboutBtn, (imagex, about_y))
                self.renderer.screen.blit(no_quitBtn, (imagex, quit_y))



            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:  # 若按下esc鍵，退出遊戲

                    if event.key == const.key["down"]:  # 若按下down
                        button += 1
                        click = True
                        self.sound.switchSound.play()
                    if event.key == const.key["up"]:
                        button -= 1
                        click = True
                        self.sound.switchSound.play()
                    if event.key == const.key["space"]:
                        self.sound.selectSound.play()
                        if button % 3 == 0:
                            self.game = Game()
                            self.game.game_start()
                            self.sound.selectSound.play()
                        if button % 3 == 1:
                            self.intro()  # 進入intro
                        if button % 3 == 2:
                            pygame.quit()
                            sys.exit()
            

            if click:
                if button % 3 == 0:  # 選到start
                    self.renderer.screen.blit(yes_startBtn, (imagex, start_btn_pos))
                    self.renderer.screen.blit(no_aboutBtn, (imagex,about_btn_pos))
                    self.renderer.screen.blit(no_quitBtn, (imagex, quit_btn_pos))
                if button % 3 == 1:  # 選到intro(about)
                    self.renderer.screen.blit(no_startBtn, (imagex, start_btn_pos))  
                    self.renderer.screen.blit(yes_aboutBtn, (imagex,about_btn_pos))
                    self.renderer.screen.blit(no_quitBtn, (imagex, quit_btn_pos))
                if button % 3 == 2:  # 選到quit
                    self.renderer.screen.blit(no_startBtn, (imagex, start_btn_pos))  
                    self.renderer.screen.blit(no_aboutBtn, (imagex, about_btn_pos))
                    self.renderer.screen.blit(yes_quitBtn, (imagex, quit_btn_pos))

            pygame.display.update()  # 更新畫布


    def options(self):
        '''
        都還沒改，無法進入options
        '''
        button = 0

        running = True #遊戲選項
        while running:
            self.renderer.screen.fill(const.color["black"])  # 設定option背景顏色
            self.renderer.draw_text('options', self.renderer.font, const.color["white"], self.renderer.screen,  const.screen_width/2, const.screen_height/4)

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
    
    def intro(self):

        while True:
            pg1 = pygame.transform.scale(self.renderer.photo_dct["intro_pg1"], (const.screen_width, const.screen_height))
            self.renderer.screen.blit(pg1, (0,0))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  # 若按下space鍵，退出
                    if event.key == const.key["esc"]:    # 若按下space，回到選單
                        self.sound.selectSound.play()                    
                        self.main_menu()
                    if event.key == const.key["right"]:
                        self.sound.switchSound.play()
                        self.intro_pg2()
            
            pygame.display.update()


    def intro_pg2(self):

        while True:
            pg2 = pygame.transform.scale(self.renderer.photo_dct["intro_pg2"], (const.screen_width, const.screen_height))
            self.renderer.screen.blit(pg2, (0,0))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  # 若按下space鍵，退出
                    if event.key == const.key["esc"]:    # 若按下space，回到選單
                        self.sound.selectSound.play()
                        self.main_menu()
                    if event.key == const.key["left"]:
                        self.sound.switchSound.play()
                        self.intro()
            
            pygame.display.update()

