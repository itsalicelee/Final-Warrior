'''v0.2：增加滑鼠碰到選單會變色、背景音樂
fullscreen時所有選單功能無法使用
'''

import pygame, sys


mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('menu test')  # 設定視窗名稱
icon = pygame.image.load("avatar.png")  # 傳入照片
pygame.display.set_icon(icon)  # 設定視窗的icon
screen = pygame.display.set_mode((1000, 750), pygame.RESIZABLE)  # 建立視窗，RESIZABLE將視窗設為可調整

font = pygame.font.SysFont(None, 50)  # 建立字型和字體大小


'''設定背景音樂'''
bgm = '怪醫黑傑克 ED1 (HD)(MAD).mp3'  # 讀取背景音樂
pygame.mixer.init()  # 啟動背景音樂
pygame.mixer.music.load(bgm)
pygame.mixer.music.set_volume(0.1)  # 來設定播放的音量，音量value的範圍為0.0到1.0
pygame.mixer.music.play(-1)  # 若為-1則會


def draw_text(text, font, color, surface, x, y):
    '''傳入文字，字體，顏色，表面，x軸y軸座標，繪製text到指定坐標的畫布上，且text的中心為(x,y)'''
    textobj = font.render(text, 1, color)  # render傳入四個字、抗鋸齒、顏色、背景色（沒指定為透明）
    textrect = textobj.get_rect()
    textrect.center= (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    while True:
        screen.fill((0, 0, 0))  # 背景底色為黑色
        draw_text('main menu', font, (255, 255, 255), screen, 500, 200)  # 畫上text，位置設定在(500,200)



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
            pygame.draw.rect(screen, (255, 0, 0), button_1)  # 畫出紅色矩形
        else:
            pygame.draw.rect(screen, (0, 0, 255), button_1)  # 畫上藍色矩形，傳入畫布、顏色、矩形
        if 400 < mx < 600 and 600 < my < 650:  # 如果游標移到第二個選單方框內
            pygame.draw.rect(screen, (255, 0, 0), button_2)  # 畫出紅色矩形
        else:
            pygame.draw.rect(screen, (0, 0, 255), button_2)  # 畫上藍色矩形，傳入畫布、顏色、矩形
        draw_text('start', font, (255, 255, 255), screen, 500, 525)  # 在矩形上加上start的text
        draw_text('option', font, (255, 255, 255), screen, 500, 625)  # 在矩形上加上start的text


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
        manual_cursor = pygame.image.load('click.png').convert_alpha()  # 游標的照片
        manual_cursor = pygame.transform.scale(manual_cursor, (40, 50))  # 將游標照片改為寬40長50
        screen.blit(manual_cursor, (pygame.mouse.get_pos()))  # 改變游標

        pygame.display.update()  # 更新畫布
        mainClock.tick(60)


def game():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('game', font, (255, 255, 255), screen, 500, 50)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def options():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('options', font, (255, 255, 255), screen, 500, 50)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()
