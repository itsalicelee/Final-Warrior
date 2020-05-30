import pygame, sys
import const
from bullet_shot_and_disappear import bullet, brick
from renderer import Renderer
from character import Character


class Game:
    """docstring for game"""
    def __init__(self):
        pygame.init()

        self.mainClock = pygame.time.Clock()
        self.renderer = Renderer()
        self.character = Character()
        self.mainClock.tick(60)
        self.pause = False
        self.button = 0
        # self.renderer.screen.fill(const.color["black"])  # 遊戲的底圖顏色預設為黑色
        self.allsprite = pygame.sprite.Group()#角色群組變數
        self.bricksprite = pygame.sprite.Group()# 一定要阿!!!不然沒辦法碰撞測試
        self.bulletsprite = pygame.sprite.Group() # 子彈群組
        self.tick = 0
        # 製造周圍 Brick
        for i in range(0, const.screen_width // 10):
            up = 0
            thebrick = brick((0, 0, 0), i * 10 + 1, up * 10 + 1)
            self.bricksprite.add(thebrick)
            self.allsprite.add(thebrick) 

        for i in range(0, const.screen_width // 10):
            down = const.screen_height // 10 - 1
            thebrick = brick((0, 0, 0),i * 10 + 1, down * 10 + 1)
            self.bricksprite.add(thebrick)
            self.allsprite.add(thebrick)

        for j in range(0, const.screen_height // 10):
            left = 0
            thebrick = brick((0, 0, 0), left * 10 + 1, j * 10 + 1)
            self.bricksprite.add(thebrick)
            self.allsprite.add(thebrick)

        for j in range(0, const.screen_height // 10):
            right = const.screen_width // 10 - 1
            thebrick = brick((0, 0, 0), right * 10 + 1, j * 10 + 1)
            self.bricksprite.add(thebrick)
            self.allsprite.add(thebrick)

    # 退出遊戲
    def quit_game(self):
        pygame.quit()
        sys.exit()


    # 主遊戲的 main loop
    def game_start(self):
        
        # 建立無窮迴圈，開始進行遊戲
        while True:
            # 當使用者沒有按下暫停：
            if not self.pause:  

                # 讀取使用者指令
                for event in pygame.event.get():
                    self.event_handler(event)

                # 算出主角和地圖分別要怎麼顯示
                self.character.character_move(const.x_change, const.y_change)
                const.now_x, const.now_y = self.character.get_loc()
                self.renderer.rolling_map(const.now_x, const.now_y)

                

                # 將 background 顯示在screen上
                self.renderer.screen.blit(self.renderer.photo_dct["bg"], (const.map_x, const.map_y))

                # 將主角顯示在 screen 上
                self.renderer.screen.blit(self.renderer.photo_dct["actorIMG"], (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))

                # 印血量、暫停按鈕
                self.renderer.draw_hp()
                self.renderer.draw_pasue_button()
                # 子彈出現
                if self.tick % const.bullet_add_speed == 0: # 時間進行多少毫秒的時候出一次子彈
                    new_bul =(bullet(6,300,200,8,(0,0,255))) # 子彈格式
                    self.bulletsprite.add(new_bul)  # 更新敵機組
                self.bulletsprite.update() # 刷新新的bulletgroup
                self.bulletsprite.draw(self.renderer.screen)  # 畫到螢幕上
                hitbrick = pygame.sprite.groupcollide(self.bricksprite, self.bulletsprite, False, True) # 改動TRUE，FALSE就可
                # 螢幕更新
                self.tick += 1
                # 螢幕更新
                pygame.display.update()

            # 當使用者按下暫停：
            else:
                # 將 background 顯示在screen上
                self.renderer.screen.blit(self.renderer.photo_dct["bg"], (const.map_x, const.map_y))

                # 將主角顯示在screen上
                self.renderer.screen.blit(self.renderer.photo_dct["actorIMG"],
                                         (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))

                # 畫血條
                self.renderer.draw_hp()

                # 呼叫遊戲暫停的選單
                self.game_pause()

                 # 螢幕更新
                pygame.display.update()
            

    def event_handler(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 鍵盤：按下按鍵
        if event.type == pygame.KEYDOWN:  
            
            # 若按下esc鍵，退出遊戲
            if event.key == const.key["esc"]:
                self.quit_game()

            # 若按下上下左右，改變人物方向
            if event.key == const.key["left"]: 
                const.x_change = -5

            elif event.key == const.key["right"]:
                const.x_change = 5

            elif event.key == const.key["up"]:
                const.y_change = -5

            elif event.key == const.key["down"]:
                const.y_change = 5

            elif event.key == const.key["pause"]:
                self.game_pause()

                if self.pause:
                    self.pause = False
                else:
                    self.pause = True
                    

        # 鍵盤：放掉按鍵
        if event.type == pygame.KEYUP:
            if event.key == const.key["left"] or event.key == const.key["right"]:
                const.x_change = 0

            elif event.key == const.key["up"] or event.key == const.key["down"]:
                 const.y_change = 0 


    # 按下暫停後，遊戲暫停並跳出選單，預設為 “繼續遊戲”
    def game_pause(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # 若按下ESC鍵，退出option
                if event.key == const.key["esc"]:
                    self.pause = False

                elif event.key == const.key["right"]:  # 若按下向右鍵
                    self.button += 1

                elif event.key == const.key["left"]:   # 若按下向左鍵
                    self.button -= 1

                elif event.key == const.key["space"]:
                    if self.button % 3 == 0:  # 進入 resume
                        self.pause = False
                    if self.button % 3 == 1:  # 進入theme
                        pass
                    if self.button % 3 == 2:  # 回到main menu
                        pass

        if self.button % 3 == 1:  # 選到resume
            pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.pause_button["resume"])  # 一開始預設畫出start紅色矩形
            pygame.draw.rect(self.renderer.screen, const.color["red"], self.renderer.pause_button["option"])  # 畫上藍色矩形，傳入畫布、顏色、矩形
            pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.pause_button["quit"])  # 畫上藍色矩形，傳入畫布、顏色、矩形



        if self.button % 3 == 2:  # 選到quit
            pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.pause_button["resume"])  # 一開始預設畫出start紅色矩形
            pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.pause_button["option"])  # 畫上藍色矩形，傳入畫布、顏色、矩形
            pygame.draw.rect(self.renderer.screen, const.color["red"], self.renderer.pause_button["quit"])  # 畫上藍色矩形，傳入畫布、顏色、矩形

        if self.button % 3 == 0:  # 選到option
            pygame.draw.rect(self.renderer.screen, const.color["red"], self.renderer.pause_button["resume"])  # 一開始預設畫出start紅色矩形
            pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.pause_button["option"])  # 畫上藍色矩形，傳入畫布、顏色、矩形
            pygame.draw.rect(self.renderer.screen, const.color["blue"], self.renderer.pause_button["quit"])  # 畫上藍色矩形，傳入畫布、顏色、矩形

    # # def display_pause_button(self):
    #     # option_lst = ["resume", "option", "quit"]
    #     # for i in range(3):
    #     #     if self.button % 3 == i:
    #     pygame.rect(self.renderer.screen, const.color["blue"], self.renderer.pause_button["resume"])
    #     # else:
        #     pygame.rect(self.renderer.screen, const.color["blue"], self.renderer.pause_button[option_lst[i]])
                # pygame.rect(self.renderer.screen, const.color["red"], self.renderer.pause_button[option_lst[i]])




    # def check_rect_collide(rect_a, rect_b):
    #     if rect_a.bottom >= rect_b.top and rect_a.top <= rect_b.bottom and 
    #        rect_a.right >= rect_b.left and rect_a.left <= rect_b.right:
    #         return True
    #     else:
    #         return False


