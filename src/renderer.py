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
        }

        self.map_width = self.photo_dct["bg"].get_width()
        self.map_height = self.photo_dct["bg"].get_height()

        self.screen = pygame.display.set_mode((1000, 750))  # 顯示視窗
        

        # 建立矩形_1，長200寬50，距離左邊邊界為400，距離上面邊界400
        self.button_1 = pygame.Rect(const.menuButton["game"])

        # 建立矩形_2，長200寬50，距離左邊邊界為400，距離上面邊界500
        self.button_2 = pygame.Rect(const.menuButton["option"])

        # 建立矩形_3，長200寬50，距離左邊邊界為400，距離上面邊界600
        self.button_3 = pygame.Rect(const.menuButton["quit"])

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
        # x 方向
        if role_x < const.screen_width / 2:
            const.map_x = 0

        elif role_x > self.map_width - const.screen_width / 2:
            const.map_x = -(self.map_width - const.screen_width)

        else:
            const.map_x =  -(role_x - const.screen_width / 2)

          # y 方向
        if role_y < const.screen_height / 2:
            const.map_y = 0

        elif role_y > self.map_height - const.screen_height / 2:
            const.map_y = -(self.map_height - const.screen_height)

        else:
            const.map_y = -(role_y - const.screen_height / 2)
    
    def draw_hp(self):
        # self.hit_box = (17, 11, 29, 52)
        # 血條：绿色背景矩形
        pygame.draw.rect(self.screen, const.color["blue"], (20, 20, 240, 120)) # [x坐標, y坐標, 寬度, 高度]
        # # 血條：红色背景矩形，即：消耗的血）
        # pygame.draw.rect(self.screen, const.color["red"], (20, 20, 240, 120)) # [x坐標, y坐標, 寬度, 高度]

        self.draw_text("hp ...", self.font, const.color["black"], self.screen, 130, 70)

    def draw_game_pause(self):
        self.draw_text("pause", self.font, const.color["black"], self.screen, const.screen_width/2, const.screen_height/2)





