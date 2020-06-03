import pygame
import const
from sound import Sound

class Renderer:
    """docstring for Render"""

    def __init__(self):
        pygame.init()

        self.photo_dct = {
                            "icon": pygame.image.load("images/avatar.png"),
                            "actorIMG": pygame.image.load("images/racecar.png"),
                            "bg": pygame.image.load("images/background/background.png"),
                            "game_over": pygame.image.load("images/gameover.png"),
                            "replay": pygame.image.load("images/play_again.png"),
                            "replay_red": pygame.image.load("images/play_again_red.png"),
                            "back_to_menu": pygame.image.load("images/back_to_menu.png"),
                            "back_to_menu_red": pygame.image.load("images/back_to_menu_red.png"),
                            "main_menu": pygame.image.load("images/main_menu.png"),
                            "pause_button": pygame.image.load("images/pause_button.png"),

                             ############ buttons ####################
                            "yes_start" : pygame.image.load("images/button/yes_start.png"),
                            "yes_about" : pygame.image.load("images/button/yes_about.png"),
                            "yes_quit" : pygame.image.load("images/button/yes_quit.png"),
                            "no_start" : pygame.image.load("images/button/no_start.png"),
                            "no_about" : pygame.image.load("images/button/no_about.png"),
                            "no_quit" : pygame.image.load("images/button/no_quit.png"),

                             ############ pause #######################
                            "pause_bg" : pygame.image.load("images/pause_menu.png"),
                            "yes_resume" : pygame.image.load("images/button/yes_resume.png"),
                            "no_resume" : pygame.image.load("images/button/no_resume.png"),
                            "yes_volume" : pygame.image.load("images/button/yes_volume.png"),
                            "no_volume" : pygame.image.load("images/button/no_volume.png"),
                            "yes_menu" : pygame.image.load("images/button/yes_menu.png"),
                            "no_menu" : pygame.image.load("images/button/no_menu.png")

        }
        
        self.theme_ghost = {
                            "bg_1": pygame.image.load("images/theme_ghost/bg/bg.png"),
                            "bg_1_num": pygame.image.load("images/theme_ghost/bg/bg_1_num.png"),
                            "bg_sk": pygame.image.load("images/theme_ghost/bg/bg_sk.png"),
                            "bg_tomb": pygame.image.load("images/theme_ghost/bg/bg_tomb.png")
        }

        self.number_dct = {
                            "0": pygame.image.load("images/number/0.png"),
                            "1": pygame.image.load("images/number/1.png"),
                            "2": pygame.image.load("images/number/2.png"),
                            "3": pygame.image.load("images/number/3.png"),
                            "4": pygame.image.load("images/number/4.png"),
                            "5": pygame.image.load("images/number/5.png"),
                            "6": pygame.image.load("images/number/6.png"),
                            "7": pygame.image.load("images/number/7.png"),
                            "8": pygame.image.load("images/number/8.png"),
                            "9": pygame.image.load("images/number/9.png")
        }

        self.character_move = {
                                "r1": pygame.image.load("images/character/3-1.png"),
                                "r2": pygame.image.load("images/character/3-2.png"),
                                "r3": pygame.image.load("images/character/3-3.png"),
                                "r4": pygame.image.load("images/character/3-4.png"),

                                "l1": pygame.image.load("images/character/2-1.png"),
                                "l2": pygame.image.load("images/character/2-2.png"),
                                "l3": pygame.image.load("images/character/2-3.png"),
                                "l4": pygame.image.load("images/character/2-4.png"),

                                "u1": pygame.image.load("images/character/4-1.png"),
                                "u2": pygame.image.load("images/character/4-2.png"),
                                "u3": pygame.image.load("images/character/4-3.png"),
                                "u4": pygame.image.load("images/character/4-4.png"),

                                "d1": pygame.image.load("images/character/1-1.png"),
                                "d2": pygame.image.load("images/character/1-2.png"),
                                "d3": pygame.image.load("images/character/1-3.png"),
                                "d4": pygame.image.load("images/character/1-4.png")
        }

        self.volume_dct = {
                            "v_6": pygame.image.load("images/volume/volume.png"),
                            "v_5": pygame.image.load("images/volume/volume5.png"),
                            "v_4": pygame.image.load("images/volume/volume4.png"),
                            "v_3": pygame.image.load("images/volume/volume3.png"),
                            "v_2": pygame.image.load("images/volume/volume2.png"),
                            "v_1": pygame.image.load("images/volume/volume1.png"),
                            "v_0": pygame.image.load("images/volume/volume0.png")
        }


        ###########英雄血量圖片#############
        self.hp_image =[pygame.image.load("images/HP/3hp.png"),pygame.image.load("images/HP/2hp.png"),pygame.image.load("images/HP/1hp.png"),pygame.image.load("images/HP/0hp.png")]
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
                move_tempt = pygame.transform.scale(self.character_move["r1"], (28*2, 53*2))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 1:
                move_tempt = pygame.transform.scale(self.character_move["r2"], (28*2, 53*2))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 2:
                move_tempt = pygame.transform.scale(self.character_move["r3"], (26*2, 53*2))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 3:
                move_tempt =pygame.transform.scale(self.character_move["r1"], (30*2, 53*2))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

        elif const.x_change < 0:
            if tick % 4 == 0:
                move_tempt = pygame.transform.scale(self.character_move["l1"], (28*2, 53*2))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 1:
                move_tempt = pygame.transform.scale(self.character_move["l2"], (28*2, 53*2))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 2:
                move_tempt = pygame.transform.scale(self.character_move["l3"], (26*2, 53*2))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 3:
                move_tempt =pygame.transform.scale(self.character_move["l1"], (30*2, 53*2))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt
            # const.character_tracked["direction"] = "x"
            # if tick % 4 == 0:
            #     move_tempt = pygame.transform.scale(self.character_move["l1"], (24*2, 53*2))
            #     self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
            #     const.character_tracked["last_pose"] = move_tempt

            # if tick % 4 == 1:
            #     move_tempt = pygame.transform.scale(self.character_move["l2"], (32*2, 53*2))
            #     self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
            #     const.character_tracked["last_pose"] = move_tempt

            # elif tick % 4 == 2:
            #     move_tempt = pygame.transform.scale(self.character_move["l3"], (25*2, 53*2))
            #     self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
            #     const.character_tracked["last_pose"] = move_tempt

            # elif tick % 4 == 3:
            #     move_tempt = pygame.transform.scale(self.character_move["l4"], (33*2, 53*2))
            #     self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
            #     const.character_tracked["last_pose"] = move_tempt

    def draw_character_y(self, tick):

        if const.y_change < 0:
            const.character_tracked["direction"] = "y"
            if tick % 4 == 0:
                move_tempt = pygame.transform.scale(self.character_move["u1"], (45*2, 52*2))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 1:
                move_tempt = pygame.transform.scale(self.character_move["u2"], (44*2, 53*2))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 2:
                move_tempt = pygame.transform.scale(self.character_move["u3"], (45*2, 53*2))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 3:
                move_tempt = pygame.transform.scale(self.character_move["u2"], (44*2, 52*2))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

        elif const.y_change > 0:
            const.character_tracked["direction"] = "y"
            if tick % 4 == 0:
                move_tempt = pygame.transform.scale(self.character_move["d1"], (53*2, 52*2))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 1:
                move_tempt = pygame.transform.scale(self.character_move["d2"], (54*2, 54*2))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 2:
                move_tempt = pygame.transform.scale(self.character_move["d3"], (53*2, 52*2))
                self.screen.blit(move_tempt, (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                const.character_tracked["last_pose"] = move_tempt

            elif tick % 4 == 3:
                move_tempt = pygame.transform.scale(self.character_move["d1"], (52*2, 53*2))
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
        if 20<hp<=30:
            self.screen.blit(pygame.transform.scale(self.hp_image[0], (int(579*0.5), int(199*0.5))), (30, 20))
        if 10<hp<=20:
            self.screen.blit(pygame.transform.scale(self.hp_image[1], (int(579*0.5), int(199*0.5))), (30, 20))
        if 0<hp<= 10:
            self.screen.blit(pygame.transform.scale(self.hp_image[2], (int(579*0.5), int(199*0.5))), (30, 20))
        elif hp==0:
            self.screen.blit(pygame.transform.scale(self.hp_image[3], (int(579*0.5), int(199*0.5))), (30, 20))

    # 畫出暫停
    def draw_pasue_button(self):
        self.screen.blit(pygame.transform.scale(self.photo_dct["pause_button"], (int(133*0.45), int(145*0.45))), (const.screen_width -70, 37))

    # 畫出分數
    def draw_score(self, score):
        score_lst = [number for number in score]
        score_lst.reverse()
        for i in range(len(score_lst)):
                number = pygame.transform.scale(self.number_dct[score_lst[i]], (int(80*0.45), int(100*0.45)))
                self.screen.blit(number, const.score_loc[i])
    
    # 選到 resume
    def draw_resume_chosen(self):
        pause_back_ground = pygame.transform.scale(self.photo_dct["pause_bg"],(1400, 900))
        yes_resume = pygame.transform.scale(self.photo_dct["yes_resume"], (300, 150))
        not_volume = pygame.transform.scale(self.photo_dct["no_volume"], (300, 150))
        not_menu = pygame.transform.scale(self.photo_dct["no_menu"], (300, 150))
        
        self.screen.blit(pause_back_ground, (const.screen_width/2 - 700, const.screen_height/2 - 500))
        self.screen.blit(yes_resume, (const.screen_width/2 - 150, const.screen_height/2 - 175))
        self.screen.blit(not_volume, (const.screen_width/2 - 150, const.screen_height/2 - 75))
        self.screen.blit(not_menu, (const.screen_width/2 - 150, const.screen_height/2 + 25))
    
    
    # 選到 volume
    def draw_volume_chosen(self):
        pause_back_ground = pygame.transform.scale(self.photo_dct["pause_bg"],(1400, 900)) 
        not_resume = pygame.transform.scale(self.photo_dct["no_resume"], (300, 150))
        choose_volume = pygame.transform.scale(self.photo_dct["yes_volume"], (300, 150))
        not_menu = pygame.transform.scale(self.photo_dct["no_menu"], (300, 150))
        
        self.screen.blit(pause_back_ground, (const.screen_width/2 - 700, const.screen_height/2 - 500))
        self.screen.blit(not_resume, (const.screen_width/2 - 150, const.screen_height/2 - 175))
        self.screen.blit(choose_volume,(const.screen_width/2 - 150, const.screen_height/2 - 75))
        self.screen.blit(not_menu, (const.screen_width/2 - 150, const.screen_height/2 + 25))

    # 選到 menu
    def draw_menu_chosen(self):
        pause_back_ground = pygame.transform.scale(self.photo_dct["pause_bg"],(1400, 900))
        not_resume = pygame.transform.scale(self.photo_dct["no_resume"], (300, 150))
        not_volume = pygame.transform.scale(self.photo_dct["no_volume"], (300, 150))
        choose_menu = pygame.transform.scale(self.photo_dct["yes_menu"], (300, 150))
        
        self.screen.blit(pause_back_ground, (const.screen_width/2 - 700, const.screen_height/2 - 500))
        self.screen.blit(not_resume, (const.screen_width/2 - 150, const.screen_height/2 - 175))
        self.screen.blit(not_volume,(const.screen_width/2 - 150, const.screen_height/2 - 75))
        self.screen.blit(choose_menu,(const.screen_width/2 - 150, const.screen_height/2 + 25))
    

    def draw_volume(self): 
        if self.bgm.get_volume() == 0.0:
            vl_0 = pygame.transform.scale(self.volume_dct["v_0"], (150, 80))
            self.screen.blit(vl_0, (const.screen_width/2 - 600, const.screen_height/2 - 40))
        elif 0 < self.bgm.get_volume() <= 0.1: 
            vl_1 = pygame.transform.scale(self.volume_dct["v_1"], (150, 80))
            self.screen.blit(vl_1, (const.screen_width/2 - 600, const.screen_height/2 - 40))
        elif 0.1 < self.bgm.get_volume() <= 0.2:
            vl_2 = pygame.transform.scale(self.volume_dct["v_2"], (150, 80))
            self.screen.blit(vl_2, (const.screen_width/2 - 600, const.screen_height/2 - 40))
        elif 0.2 < self.bgm.get_volume() <= 0.3:
            vl_3 = pygame.transform.scale(self.volume_dct["v_3"], (150, 80))
            self.screen.blit(vl_3, (const.screen_width/2 - 600, const.screen_height/2 - 40))
        elif 0.3 < self.bgm.get_volume() <= 0.4:
            vl_4 = pygame.transform.scale(self.volume_dct["v_4"], (150, 80))
            self.screen.blit(vl_4, (const.screen_width/2 - 600, const.screen_height/2 - 40))
        elif 0.5 < self.bgm.get_volume() <= 0.6:
            vl_5 = pygame.transform.scale(self.volume_dct["v_5"], (150, 80))
            self.screen.blit(vl_5, (const.screen_width/2 - 600, const.screen_height/2 - 40))
        elif 0.6 < self.bgm.get_volume():
            vl_6 = pygame.transform.scale(self.volume_dct["v_6"], (150, 80))
            self.screen.blit(vl_6, (const.screen_width/2 - 600, const.screen_height/2 - 40))


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

        
