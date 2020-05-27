'''
BUG:
1. full sreen
'''



########################################################
# module
import pygame, sys
from pygame.locals import *

# 初始化 pygame
pygame.init()
mainClock = pygame.time.Clock()

#################################
# 視窗
# 寬度、高度
screen_width, screen_height = 1000, 750
pygame.display.set_caption('menu test')  # 設定視窗名稱

icon = pygame.image.load("images/avatar.png")  # 傳入照片
pygame.display.set_icon(icon)  # 設定視窗的icon
screen = pygame.display.set_mode((screen_width, screen_height))  # 建立視窗，RESIZABLE將視窗設為可調整
font = pygame.font.SysFont(None, 50)  # 建立字型和字體大小
actorIMG = pygame.image.load("images/racecar.png") # 匯入主角圖片

bg = pygame.image.load("images/1.1-4d046d33a07490f813867425851deff9.jpg") # 匯入地圖image
map_width, map_height = bg.get_width(), bg.get_height()  # 取得長寬資訊

###############################################################
'''設定背景音樂'''
pygame.mixer.init()  # 啟動背景音樂
bgm = "music/bgm.ogg"  # 讀取背景音樂

pygame.mixer.music.load(bgm)
pygame.mixer.music.set_volume(0.1)  # 來設定播放的音量，音量value的範圍為0.0到1.0
pygame.mixer.music.play(-1)  # 若為-1則會無限輪迴播放

###############################################################
# intial parameter 
# 設定主角起始位置
role_x, role_y = screen_width * 0.45, screen_height * 0.8
x_change, y_change = 0, 0

# turn click to true to start the game
click = False

# 設定常用顏色色碼
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

##############################################
# 定義主角移動方式的函數
def move(x_change, y_change ,role_x, role_y, pause):
    # 將x, y 移動量加到主角本身的座標上
    if pause == True:
        role_x += 0
        role_y += 0
    else:
        role_x += x_change
        role_y += y_change


    # x 軸上的滾動地圖（判別方式如line上的網址）
    if role_x < screen_width / 2:
        map_x = 0
    elif role_x > map_width - screen_width / 2:
        map_x = -(map_width - screen_width)
    else:
        map_x = -(role_x - screen_width / 2)

     # y 軸上的滾動地圖（判別方式如line上的網址）
    if role_y < screen_height / 2:
        map_y = 0
    elif role_y > map_height - screen_height / 2:
        map_y = -(map_height - screen_height)
    else:
        map_y = -(role_y - screen_height / 2)
    
    return role_x, role_y, map_x, map_y

###############################################################################
# print text on the screen
def draw_text(text, font, color, surface, x, y):
    '''傳入文字，字體，顏色，表面，x軸y軸座標，繪製text到指定坐標的畫布上，且text的中心為(x,y)'''
    textobj = font.render(text, 1, color)  # render傳入四個字、抗鋸齒、顏色、背景色（沒指定為透明）
    textrect = textobj.get_rect()
    textrect.center= (x, y)
    surface.blit(textobj, textrect)

###############################################################################

def main_menu():
    while True:
        screen.fill(black)  # 背景底色為黑色
        draw_text('main menu', font, white, screen, 500, 200)  # 畫上text，位置設定在(500,200)

        '''建立menu的按鈕和submenu'''
        mx, my = pygame.mouse.get_pos()  # 取得滑鼠的座標，回傳一個tuple(x,y)

        button_1 = pygame.Rect(400, 500, 200, 50)  # 建立矩形，長200寬50，距離左邊邊界為400，距離上面邊界500
        button_2 = pygame.Rect(400, 600, 200, 50)  # 建立矩形，長200寬50，距離左邊邊界為400，距離上面邊界600

        if button_1.collidepoint((mx, my)):  # 若游標在button_1內
            if click:  # 若有點擊，進入遊戲
                game()
        if button_2.collidepoint((mx, my)):  # 若游標在button_2內
            if click:  # 若有點擊，進入遊戲
                options()  # 進入option

        if 400 < mx < 600 and 500 < my < 550:  # 如果游標移到第一個選單方框內
            pygame.draw.rect(screen, red, button_1)  # 畫出紅色矩形
        else:
            pygame.draw.rect(screen, (0, 0, 255), button_1)  # 畫上藍色矩形，傳入畫布、顏色、矩形
        if 400 < mx < 600 and 600 < my < 650:  # 如果游標移到第二個選單方框內
            pygame.draw.rect(screen, red, button_2)  # 畫出紅色矩形
        else:
            pygame.draw.rect(screen, (0, 0, 255), button_2)  # 畫上藍色矩形，傳入畫布、顏色、矩形
        draw_text('start', font, white, screen, 500, 525)  # 在矩形上加上start的text
        draw_text('option', font, white, screen, 500, 625)  # 在矩形上加上start的text


        click = False  # 滑鼠預設為沒有按下

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # 若按下esc鍵，退出遊戲
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:  # 若按下滑鼠鍵
                if event.button == 1:
                    click = True  # 將click更新為1

        '''更改游標圖示'''
        pygame.mouse.set_visible(False)  # 隱藏原本的游標
        manual_cursor = pygame.image.load('images/click.png').convert_alpha()  # 游標的照片
        manual_cursor = pygame.transform.scale(manual_cursor, (40, 50))  # 將游標照片改為寬40長50
        screen.blit(manual_cursor, (pygame.mouse.get_pos()))  # 改變游標

        pygame.display.update()  # 更新畫布
        mainClock.tick(60)


def game():
    global role_x, role_y, x_change, y_change
    '''主遊戲畫面'''
    running = True  # 一開始設定遊戲正在進行
    pause = False
    while running:  # 遊戲進行的迴圈
        screen.fill(black)  # 遊戲的底圖顏色預設為黑色
        draw_text('game', font, white, screen, 500, 50)  # 寫上game字樣


        for event in pygame.event.get():

            if event.type == QUIT:  # 關閉視窗
                pygame.quit()  # 退出pygame
                sys.exit()  # 結束程式
            if event.type == KEYDOWN:  # 若按下按鍵
                if event.key == K_ESCAPE:  # 若按ESC鍵
                    running = False  # 跳出遊戲進行的迴圈
                if event.key == K_p:  # 若按下P
                    if pause == True:  # 若原本遊戲是暫停的狀態
                        pause = False  # 將暫停取消
                        pygame.mixer.music.unpause()  # 從暫停的地方開始恢復播放音樂
                    elif pause == False:  # 若原本遊戲是進行的狀態
                        pause = True  # 暫停遊戲

                #  press up, down, left, right key
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0 

        # 因為座標的關係，將人物的座標加上地圖的座標，可以在大多情況下，人物在畫面的中心
        role_x, role_y, map_x, map_y =  move(x_change, y_change, role_x, role_y, pause)

        # 以 map_x 和 map_y 顯示地圖
        screen.blit(bg, (map_x, map_y))

        # 將人物顯示出來
        screen.blit(actorIMG, (int(map_x + role_x), int(map_y + role_y)))


        if pause == False:  # 若遊戲沒有暫停
            # 遊戲主程式在這!!!!
            pass
        elif pause ==  True:  # 若遊戲暫停
            draw_text('pause!!', font, white, screen, 500, 625)  # pause text
            pygame.mixer.music.pause()  # 音樂暫停



        pygame.display.update()
        mainClock.tick(60)


def options():
    '''遊戲選項'''
    running = True
    while running:
        screen.fill(black)  # 設定option背景顏色
        draw_text('options', font, white, screen, 500, 50)

        for event in pygame.event.get():
            if event.type == QUIT:  # 關閉視窗
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # 若按下ESC鍵，退出option
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()
