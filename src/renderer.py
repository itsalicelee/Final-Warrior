import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import const
from sound import Sound

class Renderer:
    def __init__(self):
        pygame.init()

        self.photo_dct = {
                            "icon": pygame.image.load("images/avatar.png").convert_alpha(),
                            "bg": pygame.image.load("images/background/background.png").convert_alpha(),
                            "bg_upper": pygame.image.load("images/background/background_upper.png").convert_alpha(),
                            "game_over": pygame.image.load("images/gameover.png").convert_alpha(),
                            "main_menu": pygame.image.load("images/main_menu.png").convert_alpha(),
                            "pause_button": pygame.image.load("images/pause_button.png").convert_alpha(),
                            "vine" : pygame.image.load("images/vine.png").convert_alpha(),
                             ############ buttons ####################
                            "yes_start" : pygame.image.load("images/button/yes_start.png").convert_alpha(),
                            "yes_about" : pygame.image.load("images/button/yes_about.png").convert_alpha(),
                            "yes_quit" : pygame.image.load("images/button/yes_quit.png").convert_alpha(),
                            "no_start" : pygame.image.load("images/button/no_start.png").convert_alpha(),
                            "no_about" : pygame.image.load("images/button/no_about.png").convert_alpha(),
                            "no_quit" : pygame.image.load("images/button/no_quit.png").convert_alpha(),

                             ############ pause #######################
                            "pause_bg" : pygame.image.load("images/pause_menu.png").convert_alpha(),
                            "yes_resume" : pygame.image.load("images/button/yes_resume.png").convert_alpha(),
                            "no_resume" : pygame.image.load("images/button/no_resume.png").convert_alpha(),
                            "yes_volume" : pygame.image.load("images/button/yes_volume.png").convert_alpha(),
                            "no_volume" : pygame.image.load("images/button/no_volume.png").convert_alpha(),
                            "yes_menu" : pygame.image.load("images/button/yes_menu.png").convert_alpha(),
                            "no_menu" : pygame.image.load("images/button/no_menu.png").convert_alpha(),
            
                            "intro_pg1" : pygame.image.load("images/about_p1.png").convert_alpha(),
                            "intro_pg2" : pygame.image.load("images/about_p2.png").convert_alpha()

        }
       
        self.theme_ghost = {
                            "bg_1": pygame.image.load("images/theme_ghost/bg/bg.png").convert_alpha(),
                            "bg_1_num": pygame.image.load("images/theme_ghost/bg/bg_1_num.png").convert_alpha(),
                            "bg_sk": pygame.image.load("images/theme_ghost/bg/bg_sk.png").convert_alpha(),
                            "bg_tomb": pygame.image.load("images/theme_ghost/bg/bg_tomb.png").convert_alpha()
        }

        self.theme_cat = {
                            "bg_3": pygame.image.load("images/theme_cat/bg_3.png").convert_alpha(),
                            "bg3": pygame.image.load("images/theme_cat/bg3.png").convert_alpha(),
                            "bullet3": pygame.image.load("images/theme_cat/bullet3.png").convert_alpha(),
                            "bonus3": pygame.image.load("images/theme_cat/bonus3.png").convert_alpha(),
        }

        self.theme_desert = {
                            "bonus2": pygame.image.load("images/theme_desert/bonus2.png").convert_alpha(),
                            "boss2": pygame.image.load("images/theme_desert/boss2.png").convert_alpha(),
                            "bullet2": pygame.image.load("images/theme_desert/bullet2.png").convert_alpha(),
                            "bg_2": pygame.image.load("images/theme_desert/bg2/bg_2.png").convert_alpha(),
                            "bg2_ca": pygame.image.load("images/theme_desert/bg2/bg2_ca.png").convert_alpha(),
                            "bg2_sc": pygame.image.load("images/theme_desert/bg2/bg2_sc.png").convert_alpha(),
                            "bg2": pygame.image.load("images/theme_desert/bg2/bg2.png").convert_alpha(),

        }

        self.number_dct = {
                            "0": pygame.image.load("images/number/0.png").convert_alpha(),
                            "1": pygame.image.load("images/number/1.png").convert_alpha(),
                            "2": pygame.image.load("images/number/2.png").convert_alpha(),
                            "3": pygame.image.load("images/number/3.png").convert_alpha(),
                            "4": pygame.image.load("images/number/4.png").convert_alpha(),
                            "5": pygame.image.load("images/number/5.png").convert_alpha(),
                            "6": pygame.image.load("images/number/6.png").convert_alpha(),
                            "7": pygame.image.load("images/number/7.png").convert_alpha(),
                            "8": pygame.image.load("images/number/8.png").convert_alpha(),
                            "9": pygame.image.load("images/number/9.png").convert_alpha()
        }

        self.character_move = {
                                "r1": pygame.image.load("images/character/3-1.png").convert_alpha(),
                                "r2": pygame.image.load("images/character/3-2.png").convert_alpha(),
                                "r3": pygame.image.load("images/character/3-3.png").convert_alpha(),
                                "r4": pygame.image.load("images/character/3-4.png").convert_alpha(),

                                "l1": pygame.image.load("images/character/2-1.png").convert_alpha(),
                                "l2": pygame.image.load("images/character/2-2.png").convert_alpha(),
                                "l3": pygame.image.load("images/character/2-3.png").convert_alpha(),
                                "l4": pygame.image.load("images/character/2-4.png").convert_alpha(),

                                "u1": pygame.image.load("images/character/4-1.png").convert_alpha(),
                                "u2": pygame.image.load("images/character/4-2.png").convert_alpha(),
                                "u3": pygame.image.load("images/character/4-3.png").convert_alpha(),
                                "u4": pygame.image.load("images/character/4-4.png").convert_alpha(),

                                "d1": pygame.image.load("images/character/1-1.png").convert_alpha(),
                                "d2": pygame.image.load("images/character/1-2.png").convert_alpha(),
                                "d3": pygame.image.load("images/character/1-3.png").convert_alpha(),
                                "d4": pygame.image.load("images/character/1-4.png").convert_alpha()
        }

        self.volume_dct = {
                            "v_6": pygame.image.load("images/volume/volume.png").convert_alpha(),
                            "v_5": pygame.image.load("images/volume/volume5.png").convert_alpha(),
                            "v_4": pygame.image.load("images/volume/volume4.png").convert_alpha(),
                            "v_3": pygame.image.load("images/volume/volume3.png").convert_alpha(),
                            "v_2": pygame.image.load("images/volume/volume2.png").convert_alpha(),
                            "v_1": pygame.image.load("images/volume/volume1.png").convert_alpha(),
                            "v_0": pygame.image.load("images/volume/volume0.png").convert_alpha()
        }


        ###########英雄血量圖片#############
        self.hp_image =[pygame.image.load("images/HP/3hp.png"),pygame.image.load("images/HP/2.5hp.png"),pygame.image.load("images/HP/2hp.png"),pygame.image.load("images/HP/1.5hp.png"),pygame.image.load("images/HP/1hp.png"),pygame.image.load("images/HP/0.5hp.png"),pygame.image.load("images/HP/0hp.png")]
        self.map_width = self.photo_dct["bg"].get_width()
        self.map_height = self.photo_dct["bg"].get_height()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)  # 顯示視窗
        const.screen_width = self.screen.get_width()
        const.screen_height = self.screen.get_height()
##########################################################################################
# 各種按鈕們
        # 建立矩形_1，長200寬50，距離左邊邊界為400，距離上面邊界400
        self.no_start = pygame.transform.scale(self.photo_dct["no_start"], (400, 200))
        self.yes_start = pygame.transform.scale(self.photo_dct["yes_start"], (400, 200))
        self.rect = self.no_start.get_rect()
        self.rect = self.yes_start.get_rect()


        # 建立矩形_2，長200寬50，距離左邊邊界為400，距離上面邊界500
        self.no_about = pygame.transform.scale(self.photo_dct["no_about"], (400, 200))
        self.yes_about = pygame.transform.scale(self.photo_dct["yes_about"], (400, 200))
        self.rect = self.no_about.get_rect()
        self.rect = self.yes_start.get_rect()

        # 建立矩形_3，長200寬50，距離左邊邊界為400，距離上面邊界600
        self.no_quit = pygame.transform.scale(self.photo_dct["no_quit"], (400, 200))
        self.yes_quit = pygame.transform.scale(self.photo_dct["yes_quit"], (400, 200))
        self.rect = self.no_quit.get_rect()
        self.rect = self.yes_quit.get_rect()

        self.pause_button = {
                                "resume": pygame.Rect(const.pauseButton["resume"]),
                                "volume": pygame.Rect(const.pauseButton["volume"]),
                                "menu": pygame.Rect(const.pauseButton["menu"])
        }
        self.yes_resume = pygame.transform.scale(self.photo_dct["yes_resume"],(400,200))
        self.no_resume = pygame.transform.scale(self.photo_dct["no_resume"],(400,200))
##########################################################################################

        # 建立字型和字體大小
        self.font = pygame.font.SysFont(None, 50)


        # 設定視窗名稱
        self.set_caption()

        # 設定視窗的icon
        self.set_icon()


        self.bgm = Sound()

    def set_caption(self):
        pygame.display.set_caption('menu test')


    def set_icon(self):
        pygame.display.set_icon(self.photo_dct["icon"])


    #傳入文字，字體，顏色，表面，x軸y軸座標，繪製text到指定坐標的畫布上，且text的中心為(x,y)'''
    def draw_text(self, text, font, color, surface, x, y):
        self.textobj = font.render(text, 1, color)  # render傳入四個字、抗鋸齒、顏色、背景色（沒指定為透明）
        self.textrect = self.textobj.get_rect()
        self.textrect.center = (x, y)
        surface.blit(self.textobj, self.textrect)
    def draw_character_x(self, tick):


        if const.x_change > 0:
            const.character_tracked["direction"] = "x"
            if tick % 4 == 0:
                move_tempt = pygame.transform.scale(self.character_move["r1"], (int(28*1.5), int(53*1.5)))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 1:
                move_tempt = pygame.transform.scale(self.character_move["r2"], (int(28*1.5), int(53*1.5)))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 2:
                move_tempt = pygame.transform.scale(self.character_move["r3"], (int(26*1.5), int(53*1.5)))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 3:
                move_tempt =pygame.transform.scale(self.character_move["r1"], (int(30*1.5), int(53*1.5)))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

        elif const.x_change < 0:
            if tick % 4 == 0:
                move_tempt = pygame.transform.scale(self.character_move["l1"], (int(28*1.5), int(53*1.5)))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 1:
                move_tempt = pygame.transform.scale(self.character_move["l2"], (int(28*1.5), int(53*1.5)))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 2:
                move_tempt = pygame.transform.scale(self.character_move["l3"], (int(26*1.5), int(53*1.5)))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 3:
                move_tempt =pygame.transform.scale(self.character_move["l1"], (int(30*1.5), int(53*1.5)))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

    def draw_character_y(self, tick):

        if const.y_change < 0:
            const.character_tracked["direction"] = "y"
            if tick % 4 == 0:
                move_tempt = pygame.transform.scale(self.character_move["u1"], (int(45*1.5), int(52*1.5)))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 1:
                move_tempt = pygame.transform.scale(self.character_move["u2"], (int(44*1.5), int(53*1.5)))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 2:
                move_tempt = pygame.transform.scale(self.character_move["u3"], (int(45*1.5), int(53*1.5)))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 3:
                move_tempt = pygame.transform.scale(self.character_move["u2"], (int(44*1.5), int(52*1.5)))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

        elif const.y_change > 0:
            const.character_tracked["direction"] = "y"
            if tick % 4 == 0:
                move_tempt = pygame.transform.scale(self.character_move["d1"], (int(53*1.5), int(52*1.5)))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 1:
                move_tempt = pygame.transform.scale(self.character_move["d2"], (int(54*1.5), int(54*1.5)))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 2:
                move_tempt = pygame.transform.scale(self.character_move["d3"], (int(53*1.5), int(52*1.5)))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 3:
                move_tempt = pygame.transform.scale(self.character_move["d1"], (int(52*1.5), int(53*1.5)))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt
    # 滾動地圖
    def rolling_map(self, role_x, role_y):
        self.role_x = role_x
        self.role_y = role_y
        self.x_change = 0
        self.y_change = 0

        # x 方向
        if role_x < const.screen_width / 2:
            const.map_x = 0

        elif role_x > self.map_width - const.screen_width / 2:
            self.map_x = -(self.map_width - const.screen_width)
            self.x_change = self.map_x - const.map_x
            const.map_x = self.map_x

        else:
            self.map_x =  -(role_x - const.screen_width / 2)
            self.x_change = self.map_x - const.map_x
            const.map_x = self.map_x

          # y 方向
        if role_y < const.screen_height / 2:
            const.map_y = 0

        elif role_y > self.map_height - const.screen_height / 2:
            self.map_y = -(self.map_height - const.screen_height)
            self.y_change = self.map_y - const.map_y
            const.map_y = self.map_y

        else:
            self.map_y = -(role_y - const.screen_height / 2)
            self.y_change = self.map_y - const.map_y
            const.map_y = self.map_y

        return self.x_change, self.y_change


    # 畫出hp
    def draw_hp(self, hp):
        if hp==3:
            self.screen.blit(pygame.transform.scale(self.hp_image[0], (int(579*0.5), int(199*0.5))), (30, 20))
        elif hp==2.5:
            self.screen.blit(pygame.transform.scale(self.hp_image[1], (int(579*0.5), int(199*0.5))), (30, 20))
        elif hp==2:
            self.screen.blit(pygame.transform.scale(self.hp_image[2], (int(579*0.5), int(199*0.5))), (30, 20))
        elif hp == 1.5:
            self.screen.blit(pygame.transform.scale(self.hp_image[3], (int(579*0.5), int(199*0.5))), (30, 20))
        elif hp==1:
            self.screen.blit(pygame.transform.scale(self.hp_image[4], (int(579*0.5), int(199*0.5))), (30, 20))
        elif hp==0.5:
            self.screen.blit(pygame.transform.scale(self.hp_image[5], (int(579*0.5), int(199*0.5))), (30, 20))
        elif hp==0:
            self.screen.blit(pygame.transform.scale(self.hp_image[6], (int(579*0.5), int(199*0.5))), (30, 20))

    # 畫出暫停
    def draw_pasue_button(self):
        self.screen.blit(pygame.transform.scale(self.photo_dct["pause_button"], (int(133*0.45), int(145*0.45))), (const.screen_width -70, 37))

    # 遊戲中畫出分數
    def draw_score_while_game(self, score):
        score_lst = [number for number in score]
        score_lst.reverse()
        for i in range(len(score_lst)):
                number = pygame.transform.scale(self.number_dct[score_lst[i]], (int(80*0.45), int(100*0.45)))
                self.screen.blit(number, const.score_loc[i])
    
    # 遊戲結束畫出分數
    def draw_score_game_over(self, score):
        score_lst = [number for number in score]
        #score_lst.reverse()
        for i in range(len(score_lst)):
                number = pygame.transform.scale(self.number_dct[score_lst[i]], (int(80*0.5), int(100*0.5)))
                self.screen.blit(number, const.score_loc_game_over[i])
    
    # 選到 resume
    def draw_resume_chosen(self):
        pause_back_ground = pygame.transform.scale(self.photo_dct["pause_bg"],(1400, 900))
        yes_resume = pygame.transform.scale(self.photo_dct["yes_resume"], (300, 150))
        not_volume = pygame.transform.scale(self.photo_dct["no_volume"], (300, 100))
        not_menu = pygame.transform.scale(self.photo_dct["no_menu"], (300, 150))
        
        self.screen.blit(pause_back_ground, (const.screen_width/2 - 670, const.screen_height/2 - 500))
        self.screen.blit(yes_resume, (const.screen_width/2 - 150, const.screen_height/2 - 175))
        self.screen.blit(not_volume, (const.screen_width/2 - 150, const.screen_height/2 - 45))
        self.screen.blit(not_menu, (const.screen_width/2 - 150, const.screen_height/2 + 25))
    
    
    # 選到 volume
    def draw_volume_chosen(self):
        pause_back_ground = pygame.transform.scale(self.photo_dct["pause_bg"],(1400, 900)) 
        not_resume = pygame.transform.scale(self.photo_dct["no_resume"], (300, 150))
        choose_volume = pygame.transform.scale(self.photo_dct["yes_volume"], (300, 150))
        not_menu = pygame.transform.scale(self.photo_dct["no_menu"], (300, 150))
        
        self.screen.blit(pause_back_ground, (const.screen_width/2 - 670, const.screen_height/2 - 500))
        self.screen.blit(not_resume, (const.screen_width/2 - 150, const.screen_height/2 - 175))
        self.screen.blit(choose_volume,(const.screen_width/2 - 150, const.screen_height/2 - 75))
        self.screen.blit(not_menu, (const.screen_width/2 - 150, const.screen_height/2 + 25))

    # 選到 menu
    def draw_menu_chosen(self):
        pause_back_ground = pygame.transform.scale(self.photo_dct["pause_bg"],(1400, 900))
        not_resume = pygame.transform.scale(self.photo_dct["no_resume"], (300, 150))
        not_volume = pygame.transform.scale(self.photo_dct["no_volume"], (300, 100))
        choose_menu = pygame.transform.scale(self.photo_dct["yes_menu"], (300, 150))
        
        self.screen.blit(pause_back_ground, (const.screen_width/2 - 670, const.screen_height/2 - 500))
        self.screen.blit(not_resume, (const.screen_width/2 - 150, const.screen_height/2 - 175))
        self.screen.blit(not_volume,(const.screen_width/2 - 150, const.screen_height/2 - 45))
        self.screen.blit(choose_menu,(const.screen_width/2 - 150, const.screen_height/2 + 25))
    

    def draw_volume(self): 
        pause_back_ground = pygame.transform.scale(self.photo_dct["pause_bg"],(1400, 900)) 
        not_resume = pygame.transform.scale(self.photo_dct["no_resume"], (300, 150))
        not_menu = pygame.transform.scale(self.photo_dct["no_menu"], (300, 150))

        self.screen.blit(pause_back_ground, (const.screen_width/2 - 670, const.screen_height/2 - 500))
        self.screen.blit(not_resume, (const.screen_width/2 - 150, const.screen_height/2 - 175))
        self.screen.blit(not_menu, (const.screen_width/2 - 150, const.screen_height/2 + 25))

        if self.bgm.get_volume() == 0.0:
            vl_0 = pygame.transform.scale(self.volume_dct["v_0"], (150, 80))
            self.screen.blit(vl_0, (const.screen_width/2 - 75, const.screen_height/2 - 40))
        elif 0 < self.bgm.get_volume() <= 0.1: 
            vl_1 = pygame.transform.scale(self.volume_dct["v_1"], (150, 80))
            self.screen.blit(vl_1, (const.screen_width/2 - 75, const.screen_height/2 - 40))
        elif 0.1 < self.bgm.get_volume() <= 0.2:
            vl_2 = pygame.transform.scale(self.volume_dct["v_2"], (150, 80))
            self.screen.blit(vl_2, (const.screen_width/2 - 75, const.screen_height/2 - 40))
        elif 0.2 < self.bgm.get_volume() <= 0.3:
            vl_3 = pygame.transform.scale(self.volume_dct["v_3"], (150, 80))
            self.screen.blit(vl_3, (const.screen_width/2 - 75, const.screen_height/2 - 40))
        elif 0.3 < self.bgm.get_volume() <= 0.4:
            vl_4 = pygame.transform.scale(self.volume_dct["v_4"], (150, 80))
            self.screen.blit(vl_4, (const.screen_width/2 - 75, const.screen_height/2 - 40))
        elif 0.4 < self.bgm.get_volume() <= 0.5:
            vl_5 = pygame.transform.scale(self.volume_dct["v_5"], (150, 80))
            self.screen.blit(vl_5, (const.screen_width/2 - 75, const.screen_height/2 - 40))
        elif 0.5 < self.bgm.get_volume():
            vl_6 = pygame.transform.scale(self.volume_dct["v_6"], (150, 80))
            self.screen.blit(vl_6, (const.screen_width/2 - 75, const.screen_height/2 - 40))


    # game over 選單中，回到主選單被選中
    def draw_back_to_menu_chosen(self):
        chosen = pygame.transform.scale(self.photo_dct["back_to_menu_red"], (80, 80))
        other = pygame.transform.scale(self.photo_dct["replay"], (80, 80))

        self.screen.blit(other, (const.screen_width/2 -100, const.screen_height/2))
        self.screen.blit(chosen, (const.screen_width/2 + 100, const.screen_height/2))

    def draw_block(self, block):
        pygame.draw.rect(self.photo_dct["bg"], const.color["blue"], block.rect)
        
        
 ###########################################       
    def draw_bonus(self,bonus):  # 繪出bonus的圖案
        self.screen.blit(bonus.image, (bonus.x + const.map_x, bonus.y + const.map_y))
    
    def draw_game_over(self):
        gameover = pygame.transform.scale(self.photo_dct["game_over"], (const.screen_width, const.screen_height))
        self.screen.blit(gameover, (0,0))

        
