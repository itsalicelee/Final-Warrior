import pygame
import const
class Renderer:
    """docstring for Render"""

    def __init__(self):
        pygame.init()

        self.photo_dct = {
                            "icon": pygame.image.load("images/avatar.png"),
                            "actorIMG": pygame.image.load("images/racecar.png"),
                            "bg": pygame.image.load("images/background.jpg"),
                            "game_over": pygame.image.load("images/game_over.jpeg"),
                            "replay": pygame.image.load("images/play_again.png"),
                            "replay_red": pygame.image.load("images/play_again_red.png"),
                            "back_to_menu": pygame.image.load("images/back_to_menu.png"),
                            "back_to_menu_red": pygame.image.load("images/back_to_menu_red.png"),
                            "bonus" : pygame.image.load("images/bonus.png")
                            

        }

        self.map_width = self.photo_dct["bg"].get_width()
        self.map_height = self.photo_dct["bg"].get_height()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)  # 顯示視窗
        const.screen_width = self.screen.get_width()
        const.screen_height = self.screen.get_height()
##########################################################################################
# 各種按鈕們
        # 建立矩形_1，長200寬50，距離左邊邊界為400，距離上面邊界400
        self.button_1 = pygame.Rect(const.menuButton["game"])

        # 建立矩形_2，長200寬50，距離左邊邊界為400，距離上面邊界500
        self.button_2 = pygame.Rect(const.menuButton["option"])

        # 建立矩形_3，長200寬50，距離左邊邊界為400，距離上面邊界600
        self.button_3 = pygame.Rect(const.menuButton["quit"])


        self.pause_button = {
                                "quit": pygame.Rect(const.pauseButton["quit"]),
                                "option": pygame.Rect(const.pauseButton["option"]),
                                "resume": pygame.Rect(const.pauseButton["resume"])
        }
##########################################################################################

        # 建立字型和字體大小
        self.font = pygame.font.SysFont(None, 50)


        # 設定視窗名稱
        self.set_caption()

        # 設定視窗的icon
        self.set_icon()


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


    # 先畫出hp的位置，之後要改成 hp 血條的圖片
    def draw_hp(self):
        pygame.draw.rect(self.screen, const.color["blue"], (20, 20, 240, 120)) # [x坐標, y坐標, 寬度, 高度]
        self.draw_text("hp ...", self.font, const.color["black"], self.screen, 100, 100)


    # 先畫出暫停的位置，之後要改成暫停鍵的圖片
    def draw_pasue_button(self):
        pygame.draw.rect(self.screen, const.color["red"], (const.screen_width -100, 50, 50, 50)) # [x坐標, y坐標, 寬度, 高度]
        self.draw_text("pause", self.font, const.color["black"], self.screen, const.screen_width -100, 60)


    '''
    pause 選單
    '''
    # 選到 option
    def draw_option_chosen(self):
        pygame.draw.rect(self.screen, const.color["blue"], self.pause_button["resume"])  # 一開始預設畫出start紅色矩形
        pygame.draw.rect(self.screen, const.color["red"], self.pause_button["option"])  # 畫上藍色矩形，傳入畫布、顏色、矩形
        pygame.draw.rect(self.screen, const.color["blue"], self.pause_button["quit"])  # 畫上藍色矩形，傳入畫布、顏色、矩形

    # 選到 quit
    def draw_quit_chosen(self):
        pygame.draw.rect(self.screen, const.color["blue"], self.pause_button["resume"])  # 一開始預設畫出start紅色矩形
        pygame.draw.rect(self.screen, const.color["blue"], self.pause_button["option"])  # 畫上藍色矩形，傳入畫布、顏色、矩形
        pygame.draw.rect(self.screen, const.color["red"], self.pause_button["quit"])  # 畫上藍色矩形，傳入畫布、顏色、矩形

    # 選到 resume
    def draw_resume_chosen(self):
        pygame.draw.rect(self.screen, const.color["red"], self.pause_button["resume"])  # 一開始預設畫出start紅色矩形
        pygame.draw.rect(self.screen, const.color["blue"], self.pause_button["option"])  # 畫上藍色矩形，傳
        pygame.draw.rect(self.screen, const.color["blue"], self.pause_button["quit"])  # 畫上藍色矩形，傳入畫布、顏色、矩形


    '''
    game over 選單
    '''
    # 畫出game over 的選單，預設為回到主選單
    def draw_game_over(self):
        game_over = pygame.transform.scale(self.photo_dct["game_over"], (400, 200))
        replay_red = pygame.transform.scale(self.photo_dct["replay_red"], (80, 80))
        back_to_menu = pygame.transform.scale(self.photo_dct["back_to_menu"], (80,80))

        self.screen.blit(game_over, (const.screen_width/2 -150, const.screen_height/2 - 200))
        self.screen.blit(replay_red, (const.screen_width/2 -100, const.screen_height/2))
        self.screen.blit(back_to_menu, (const.screen_width/2 + 100, const.screen_height/2))

    # game over 選單中，replay 被選中
    def draw_replay_chosen(self):
        chosen = pygame.transform.scale(self.photo_dct["replay_red"], (80, 80))
        other = pygame.transform.scale(self.photo_dct["back_to_menu"], (80, 80))

        self.screen.blit(chosen, (const.screen_width/2 -100, const.screen_height/2))
        self.screen.blit(other, (const.screen_width/2 + 100, const.screen_height/2))

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


    




