'''匯入模組'''
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame, sys, random
import const
import area_setting as boundary

from bullet_shot_and_disappear import bullet, brick
from renderer import Renderer
from character import Character
from block import Block
from bonus import Bonus
from sound import Sound
from boss import Boss
'''匯入模組結束'''


# Game Class
class Game:


    def __init__(self):

        # 初始化 pygame
        pygame.init()

        # 初始化時間，遊戲幀數為每秒60幀
        self.mainClock = pygame.time.Clock()
        self.mainClock.tick(60)
        self.tick = 0

        # 初始化「繪圖」、「聲音」、「主角」
        self.renderer = Renderer()
        self.character = Character()
        self.sound = Sound()
        self.bgm = Sound()

        '''遊戲參數初始化設定'''
        self.pause = False  # 可控制遊戲暫停
        self.quit = False  # 可退出當前遊戲
        self.pause_button = 0  # 遊戲暫停選單按鍵 
        self.game_over_button = 0  # 遊戲死亡選單按鍵 
        '''遊戲參數初始化設定結束'''

        '''遊戲精靈群組初始化'''
        self.allsprite = pygame.sprite.Group()  # 精靈群組的總群組
        self.bulletsprite = pygame.sprite.Group() # 子彈群組
        self.bricksprite = pygame.sprite.Group()  # 子彈邊界群組
        self.bosssprite = pygame.sprite.Group() # 魔王群組

        self.score_sprite = pygame.sprite.Group()
        self.shoes_sprite = pygame.sprite.Group()
        self.heart_sprite = pygame.sprite.Group()
        self.bonus_lst = [self.score_sprite, self.shoes_sprite, self.heart_sprite]  # 突發class清單
        self.direction = 0
        self.num = 0
        self.speed_adjust = 0
        self.map_changex = 0
        self.map_changey = 0
        self.speed_up = False
        self.speed_up_time = 0
        # 魔王加群組
        self.boss = Boss()
        # boss = Boss(const.screen_width // 2 + self.map_changex, const.screen_height // 2 + self.map_changey)
        self.bosssprite.add(self.boss)
        '''遊戲精靈群組初始化結束'''


        self.volume_dct = {
                            "v_0": pygame.image.load("images/volume/volume.png"),
                            "v_1": pygame.image.load("images/volume/volume5.png"),
                            "v_2": pygame.image.load("images/volume/volume4.png"),
                            "v_3": pygame.image.load("images/volume/volume3.png"),
                            "v_4": pygame.image.load("images/volume/volume2.png"),
                            "v_5": pygame.image.load("images/volume/volume1.png"),
                            "v_6": pygame.image.load("images/volume/volume0.png")
        }

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    '''bonus 函數區'''
    # 出現 bonus 事件
    def bonus_event(self):
        self.bonus = Bonus()

        # 添加分數bonus
        if self.bonus.type == "score":
            self.score_sprite.add(self.bonus)

        # 添加加速bonus
        elif self.bonus.type == "shoes":
            self.shoes_sprite.add(self.bonus)

        # 添加回血bonus
        elif self.bonus.type == "heart":
            ########改!!
            if self.character.hp <= 2.5:
                self.heart_sprite.add(self.bonus)


    # 觸發 bonus 效果
    def bonus_triggered(self):

        # 觸發分數bonus
        if pygame.sprite.spritecollide(self.character, self.score_sprite, True):
            self.character.score += 1
            self.bonus = Bonus()
            self.bonus.score()
            self.score_sprite.add(self.bonus)
            self.sound.bonusSound.play()

        # 觸發加速bonus
        elif pygame.sprite.spritecollide(self.character, self.shoes_sprite, True):
            #print("加速")
            ########改!!
            const.speed += 5
            self.speed_up_time = 0
            self.speed_up = True
            self.sound.speedSound.play()

        # 觸發回血bonus
        elif pygame.sprite.spritecollide(self.character, self.heart_sprite, True):
            self.character.hp += 0.5
            self.sound.hpSound.play()

    # 顯示 bonus 到螢幕上
    def draw_bonus(self):
        for group in self.bonus_lst:
            for sprite in group.sprites():
                sprite.expire_time += 1
                if pygame.sprite.spritecollide(sprite, boundary.group, False):
                    sprite.kill()

                
                if 0 <= sprite.expire_time <= 200:  # 檢查每個 bonus 存在的時間，超過上限就消除
                    self.renderer.screen.blit(sprite.image, (sprite.x + const.map_x,sprite.y + const.map_y))

                elif 200 < sprite.expire_time < 500:  # 在某個時間後開始閃爍
                    if sprite.expire_time % 30 == 0:
                        pass
                    else:
                        self.renderer.screen.blit(sprite.image, (sprite.x + const.map_x,sprite.y + const.map_y))

                else:
                    sprite.kill()
    '''bonus 函數區結束'''


        # 子彈模式
    def bullet_mode1(self, speed, width, height):
        if self.tick % 10 == 0: # 時間進行多少毫秒的時候出一次子彈
            self.num += 1
            if self.num <= 50:
                self.direction = random.randint(-180, 180)
                new_bul =(bullet(speed, ((width // 2) + 70), ((height // 2) + 100), 8, (0, 0, 255), self.direction)) # 子彈格式
                self.bulletsprite.add(new_bul)
            elif 50 <= self.num <= 60:
                self.direction = 0
                for i in range(8):
                    new_bul =(bullet(speed, ((width // 2) + 70), ((height // 2) + 100), 8, (0, 0, 255), self.direction)) # 子彈格式
                    self.bulletsprite.add(new_bul)
                    self.direction += 45
            elif 60 <= self.num <= 120:
                new_bul =(bullet(speed, ((width // 2) + 70), ((height // 2) + 100), 8, (0, 0, 255), self.direction)) # 子彈格式
                self.direction += 22.5
                self.bulletsprite.add(new_bul)
                if self.direction >= 360:
                    self.direction = 0
            elif 120 <= self.num <= 180:
                self.direction += 22.5
                new_bul =(bullet(speed, ((width // 2) + 70), ((height // 2) + 100), 8, (0, 0, 255), self.direction)) # 子彈格式
                self.bulletsprite.add(new_bul)
                new_bul =(bullet(speed, ((width // 2) + 70), ((height // 2) + 100), 8, (0, 0, 255), -self.direction)) # 子彈格式
                self.bulletsprite.add(new_bul)
                if self.direction >= 180:
                    self.direction = 0
            if self.num >= 180:
                self.num = 0 
        
        
    # 退出遊戲
    def quit_game(self):
        pygame.quit()
        sys.exit()


    # 主遊戲的 main loop
    def game_start(self):
        played = False
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
                self.renderer.screen.blit(self.renderer.theme_ghost["bg_1"], (const.map_x, const.map_y))
                if const.x_change == 0 and const.y_change == 0:
                    self.renderer.screen.blit(const.character_tracked["last_pose"], (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                # else:
                elif const.x_change != 0:
                    self.renderer.draw_character_x(self.tick)
                elif const.y_change != 0:
                    self.renderer.draw_character_y(self.tick)

                self.renderer.screen.blit(self.renderer.photo_dct ["bg_upper"], (const.map_x, const.map_y))
                self.renderer.screen.blit(self.renderer.photo_dct ["vine"], (const.map_x, const.map_y))

                # 印血量、暫停按鈕
                self.renderer.draw_hp(self.character.hp)
                self.renderer.draw_pasue_button()

                # 魔王出現
                for sprite in self.bosssprite.sprites():
                    self.renderer.screen.blit(sprite.image, (const.screen_width // 2 + const.map_x, const.screen_height // 2 + const.map_y))

                '''
                子彈區
                '''
                if self.tick % 1000 == 0 and self.tick > 1500:
                    self.speed_adjust += 2
               # 子彈出現
                if self.tick <= 3000:
                    self.bullet_mode1(const.bullet_add_speed + self.speed_adjust, const.screen_width, const.screen_height)
                    self.bulletsprite.update() # 刷新新的bulletgroup
                elif 3000 <= self.tick <= 3100:
                    if self.tick % const.bullet_add_speed == 0:
                        self.direction = 0
                        for i in range(16):
                            new_bul =(bullet(const.bullet_add_speed + self.speed_adjust, ((const.screen_width // 2) + 70), ((const.screen_height // 2) + 100), 8, (0, 0, 255), self.direction)) # 子彈格式
                            self.bulletsprite.add(new_bul)
                            self.direction += 22.5
                    self.bulletsprite.update() # 刷新新的bulletgroup
                elif self.tick >= 3100:
                    self.bullet_mode1(const.bullet_add_speed + self.speed_adjust, const.screen_width, const.screen_height)
                    self.bulletsprite.update()
                if self.tick >= 100000:
                    self.tick = 0
                    

                hitbrick = pygame.sprite.groupcollide(boundary.group, self.bulletsprite, False, True) # 改動TRUE，FALSE就可
                
                for sprite in self.bulletsprite.sprites():
                    self.renderer.screen.blit(sprite.image, (sprite.x+const.map_x, sprite.y+const.map_y))

                self.bullet_hit_actor()

                # 螢幕更新
                self.tick += 1


                '''bonus 事件區'''
                # 出現隨機事件
                if self.tick % 200 == 0: 
                    self.bonus_event()
                # 隨機事件被觸發
                self.bonus_triggered()
                # 印出未消除的bonus
                self.draw_bonus()

                #速度回覆
                if self.speed_up:
                    self.speed_up_time += 1
                    if self.speed_up_time >= 200:
                        const.speed = 5
                        self.speed_up = False
                        self.speed_up_time = 0
                    
                '''bonus 事件區結束'''

                self.renderer.draw_score_while_game(str(self.character.score))

                # 檢查死亡
                self.check_whether_die()

                # 螢幕更新
                pygame.display.update()

            # 當使用者按下暫停：
            else:

                # 將 background 顯示在screen上
                self.renderer.screen.blit(self.renderer.theme_ghost["bg_1"], (const.map_x, const.map_y))

                # 將主角顯示在screen上
                ########改!!
                self.renderer.screen.blit(const.character_tracked["last_pose"],
                                         (int(const.map_x + const.now_x), int(const.map_y + const.now_y)))
                
                # 畫血條
                self.renderer.draw_hp(self.character.hp)

                #畫子彈
                for sprite in self.bulletsprite.sprites():
                    self.renderer.screen.blit(sprite.image, (sprite.x+const.map_x, sprite.y+const.map_y))

                # 使用者按下 p 鍵或是死亡都會觸發暫停，由主角的血量屬性來判斷有沒有死亡，在此先以按下g鍵表示死亡事件
                if self.character.alive:
                    self.game_pause()
                else:
                    self.renderer.draw_game_over()
                    self.renderer.draw_score_game_over(str(self.character.score))
                    
                    self.game_over()
                    if played == False:
                        self.sound.gameoverSound.play()
                        played = True


                 # 螢幕更新
                pygame.display.update()


    def bullet_hit_actor(self):
        if pygame.sprite.spritecollide(self.character, self.bulletsprite, True):
            self.character.hp -= 0.5
            self.sound.shotSound.play()


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
            ########改!! 
                const.x_change = -const.speed

            elif event.key == const.key["right"]:
                const.x_change = const.speed

            elif event.key == const.key["up"]:
                const.y_change = -const.speed

            elif event.key == const.key["down"]:
                const.y_change = const.speed

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
                    
                elif event.key == const.key["down"]:  # 若按下向下鍵
                    self.pause_button += 1
                    self.sound.switchSound.play()

                elif event.key == const.key["up"]:   # 若按下向上鍵
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
            self.renderer.draw_volume_chosen()

        elif self.pause_button % 3 == 2:  # 選到menu
            self.renderer.draw_menu_chosen()


    def volume(self):
        back_to_pause = False
        while back_to_pause == False:
            #self.renderer.draw_volume_chosen()
            self.renderer.draw_volume()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  # 若按下ESC鍵，退出volume
                    
                    """音量有七段"""
                    if event.key == const.key["left"]:  # 若按下left，音量減小
                        if self.bgm.get_volume() < 0.1:
                            self.bgm.set_bgm(0.0)

                        else:
                            self.bgm.set_bgm(float(self.bgm.get_volume())-0.1)

                    if event.key == const.key["right"]:  # 若按下right，音量增大
                        if float(self.bgm.get_volume()) + 0.1 <= 0.6:  # 不要讓音量太大 
                            self.bgm.set_bgm(float(self.bgm.get_volume())+ 0.1)
                        #self.game_pause()
                    if event.key == const.key["space"]:   # 若按下esc 跳出調整音量
                        self.sound.selectSound.play()
                        back_to_pause = True


            self.renderer.draw_volume()
            pygame.display.update()
        self.game_pause()

    # 檢查死亡
    def check_whether_die(self):
        if self.character.hp == 0:
            self.pause = True
            self.character.alive = False
            const.x_change = 0
            const.y_change = 0
            move_tempt = pygame.transform.scale(self.renderer.character_move["r1"], (int(28*1.5), int(53*1.5)))
            const.character_tracked["last_pose"] = move_tempt


    # 定義game over 後，畫面要跳出的選單內容
    def game_over(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == const.key["space"]:
                    self.sound.selectSound.play()
                    self.renderer.draw_game_over()
                    self.quit = True
                    const.speed = 5
