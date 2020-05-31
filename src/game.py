import pygame, sys
import const
from bullet_shot_and_disappear import bullet, brick
from renderer import Renderer
from character import Character
from block import Block
from bonus import Bonus
import random
from sound import Sound
from boss import Boss


import area_setting as boundary

class Game:
    """docstring for game"""
    def __init__(self):
        # 初始化 pygame
        pygame.init()

        # 初始化時間，並呼叫「繪圖」和「主角」兩個class
        self.mainClock = pygame.time.Clock()
        self.renderer = Renderer()
        self.character = Character()
        self.mainClock.tick(60)

        # 預設為「遊戲進行中」
        self.pause = False
        self.pause_button = 0
        self.game_over_button = 0

        # 
        self.quit = False

        self.allsprite = pygame.sprite.Group() #角色群組變數
        self.bricksprite = pygame.sprite.Group()# 一定要阿!!!不然沒辦法碰撞測試
        self.bulletsprite = pygame.sprite.Group() # 子彈群組
        self.bosssprite = pygame.sprite.Group() # 魔王群組
        # 魔王加群組
        boss = Boss(const.screen_width // 2, const.screen_height // 2)
        self.bosssprite.add(boss)

        self.tick = 0
        self.map_changex = 0
        self.map_changey = 0

        self.create_brick()

        # 突發事件
        self.bonus_1 = Bonus()
        self.bonus_2 = Bonus()
        self.bonussprite = pygame.sprite.Group()
        self.bonussprite.add(self.bonus_1, self.bonus_2)

        self.sound = Sound()
        


    def create_brick(self):
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
        while not self.quit :
            # 當使用者沒有按下暫停：
            if not self.pause:  

                # 讀取使用者指令
                for event in pygame.event.get():
                    self.event_handler(event)


                # 算出主角和地圖分別要怎麼顯示
                self.character.character_move(const.x_change, const.y_change)
                const.now_x, const.now_y = self.character.get_loc()
                map_change_x, map_change_y = self.renderer.rolling_map(const.now_x, const.now_y)
                self.map_changex += map_change_x
                self.map_changey += map_change_y

                '''
                開始顯示地圖、主角、血量、子彈
                '''
                # 將 background 顯示在screen上
                self.renderer.screen.blit(self.renderer.photo_dct["bg"], (const.map_x, const.map_y))

                # 將主角顯示在 screen 上
                self.renderer.screen.blit(self.renderer.photo_dct["actorIMG"], (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))

                # 印血量、暫停按鈕
                self.renderer.draw_hp()
                self.renderer.draw_pasue_button()

                # 魔王出現
                for sprite in self.bosssprite.sprites():
                    self.renderer.screen.blit(sprite.image, (const.screen_width // 2 + self.map_changex, const.screen_height // 2 + self.map_changey))

                # 子彈出現
                if self.tick % const.bullet_add_speed == 0: # 時間進行多少毫秒的時候出一次子彈
                    new_bul =(bullet(6, (const.screen_width // 2 + self.map_changex), (const.screen_height // 2 + self.map_changey), 8, (0, 0, 255))) # 子彈格式
                    self.bulletsprite.add(new_bul)  # 更新敵機組
                self.bulletsprite.update() # 刷新新的bulletgroup

                # self.bulletsprite.draw(self.renderer.screen)  # 畫到螢幕上
                hitbrick = pygame.sprite.groupcollide(self.bricksprite, self.bulletsprite, False, True) # 改動TRUE，FALSE就可
                
                for sprite in self.bulletsprite.sprites():
                    self.renderer.screen.blit(sprite.image, (sprite.x+const.map_x, sprite.y+const.map_y))

                self.bullet_hit_actor()

                # 檢查死亡
                if self.character.hp == 0:
                    self.pause = True
                    self.character.alive = False

                # 螢幕更新
                self.tick += 1

                # 畫出不能走的區域方便觀察，這段之後可以註解掉
                self.renderer.draw_block(boundary.block_1)
                self.renderer.draw_block(boundary.block_2)
                self.renderer.draw_block(boundary.block_3)
                
                
###########################
                # if self.tick % 5 == 0:  # 多久出現一次隨機事件
                #     self.bonus.x = random.randint(0, self.renderer.map_width)
                #     self.bonus.y = random.randint(0, self.renderer.map_height)
                #     self.type = const.bonus_type[random.randint(0,len(const.bonus_type)-1)]
                #self.bonus = Bonus()

                # 檢查碰撞，碰撞到就消除：
                pygame.sprite.spritecollide(self.character, self.bonussprite, True)

                # 用這個作法，把未消除的bonus印出來，除了人物本身的座標再加上地圖的座標，這樣bonus 就不會隨著地圖動了
                for sprite in self. bonussprite.sprites():
                    self.renderer.screen.blit(sprite.image, (sprite.x + const.map_x,sprite.y + const.map_y))

###########################
                
                
       

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

                # 使用者按下 p 鍵或是死亡都會觸發暫停，由主角的血量屬性來判斷有沒有死亡，在此先以按下g鍵表示死亡事件
                if self.character.alive:
                    self.game_pause()
                else:
                    self.renderer.draw_game_over()
                    self.game_over()

                 # 螢幕更新
                pygame.display.update()

    def bullet_hit_actor(self):
        if pygame.sprite.spritecollide(self.character, self.bulletsprite, True):
            self.character.hp -= 1

    def event_handler(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 鍵盤：按下按鍵
        if event.type == pygame.KEYDOWN:  
            
            # 若按下esc鍵，退出遊戲
            if event.key == const.key["esc"]:
                self.quit_game()

            # 按「上、下、左、右」：改變人物方向
            if event.key == const.key["left"]: 
                const.x_change = -5

            elif event.key == const.key["right"]:
                const.x_change = 5

            elif event.key == const.key["up"]:
                const.y_change = -5

            elif event.key == const.key["down"]:
                const.y_change = 5

            # 按 p ，遊戲暫停，
            elif event.key == const.key["pause"]:
                self.pause = True
                self.game_pause()

            elif event.key == const.key["game_over"]:
                self.pause = True
                self.character.alive = False

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
                    self.pause_button += 1
                    self.sound.switchSound.play()

                elif event.key == const.key["left"]:   # 若按下向左鍵
                    self.pause_button -= 1
                    self.sound.switchSound.play()

                # 畫面上的排列順序，由左至右分別是：「resume、volume、menu」
                elif event.key == const.key["space"]:
                    self.sound.selectSound.play()
                    if self.pause_button % 3 == 0:  # 進入 resume
                        self.pause = False
                    elif self.pause_button % 3 == 1:  # 進入volume
                        self.volume()
                    elif self.pause_button % 3 == 2:  # 回到menu
                        self.quit = True

        if self.pause_button % 3 == 0:  # 選到resume
            self.renderer.draw_resume_chosen()

        elif self.pause_button % 3 == 1:  # 選到volume
           self.renderer.draw_option_chosen()

        elif self.pause_button % 3 == 2:  # 選到menu
            self.renderer.draw_quit_chosen()

    def volume(self):
        
        while True:
            self.renderer.screen.fill(const.color["black"])  # 設定option背景顏色
            self.renderer.draw_text('volume', self.renderer.font, const.color["white"], self.renderer.screen,  const.screen_width/2, const.screen_height/4)
            

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

                    if event.key == const.key["esc"]:    # 若按下esc
                        
                        #以下兩個指令都需要重開機千萬別嘗試
                        self.pause = True
                        #self.game_pause()
                    if event.key == const.key["up"]: # 防止卡死備用的：按上可以quit整個遊戲
                        self.quit_game()

            self.renderer.draw_text('set volume', self.renderer.font, const.color["white"], self.renderer.screen,  const.screen_width/2, const.screen_height/5)
            
            pygame.display.update()

    # 定義game over 後，畫面要跳出的選單內容
    def game_over(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == const.key["right"]:  # 若按下向右鍵
                    self.game_over_button += 1
                    self.sound.switchSound.play()
                elif event.key == const.key["left"]:   # 若按下向左鍵
                    self.game_over_button -= 1
                    self.sound.switchSound.play()
                elif event.key == const.key["space"]:
                    self.sound.selectSound.play()
                    if self.game_over_button % 2 == 0:  # 進入 replay
                        pass
                    elif self.game_over_button % 2 == 1:  # 進入 back_to_menu
                        self.quit = True
        
        if self.game_over_button % 2 == 0:
            self.renderer.draw_replay_chosen()

        elif self.game_over_button %2 == 1:
            self.renderer.draw_back_to_menu_chosen()




