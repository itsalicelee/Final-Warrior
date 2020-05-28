import pygame
import const
from game import User_control
class Renderer:
    """docstring for Render"""

    def __init__(self):
        pygame.init()
        self.user_control = User_control()

        # 圖片建立字典
        # 匯入程式icon

        self.icon = pygame.image.load("images/avatar.png")  

        # 匯入主角圖片
        self.actorIMG = pygame.image.load("images/racecar.png") 

        # 地圖背景
        self.bg = pygame.image.load("images/background.jpg")

        # 匯入 click 圖片
        self.manual_cursor = pygame.image.load('images/click.png')
        # self.manual_cursor = pygame.image.load('images/click.png').convert_alpha()
        self.manual_cursor = pygame.transform.scale(self.manual_cursor, (40, 50))




        # 建立視窗，RESIZABLE將視窗設為可調整
        self.screen = pygame.display.set_mode((const.screen_width, const.screen_height))

        # 建立矩形_1，長200寬50，距離左邊邊界為400，距離上面邊界500
        self.button_1 = pygame.Rect(400, 500, 200, 50)

        # 建立矩形_2，長200寬50，距離左邊邊界為400，距離上面邊界600
        self.button_2 = pygame.Rect(400, 600, 200, 50)  

        # 建立字型和字體大小 # 字體到時候建立字典
        self.font = pygame.font.SysFont(None, 50)


        # 設定視窗名稱
        self.set_caption()

        # 設定視窗的icon
        self.set_icon()

    def set_caption(self):
        pygame.display.set_caption('menu test')


    def set_icon(self):
        pygame.display.set_icon(self.icon)


    #傳入文字，字體，顏色，表面，x軸y軸座標，繪製text到指定坐標的畫布上，且text的中心為(x,y)'''
    def draw_text(self, text, font, color, surface, x, y):
        self.textobj = font.render(text, 1, color)  # render傳入四個字、抗鋸齒、顏色、背景色（沒指定為透明）
        self.textrect = self.textobj.get_rect()
        self.textrect.center = (x, y)
        surface.blit(self.textobj, self.textrect)

    def update(self):
        self.user_control.event_handler()
        pygame.display.update()  # 更新畫布



