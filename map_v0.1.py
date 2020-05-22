# 引入 pygame 模組
import pygame 

# 初始化 pygame
pygame.init()
clock = pygame.time.Clock()


# 視窗寬度、高度
screen_width = 1000
screen_height = 750

# 設定常用顏色色碼
black = (0, 0, 0)
white = (255, 255, 255)


# 顯示視窗
screen = pygame.display.set_mode((screen_width, screen_height))
# 顯示標題
screen_caption = pygame.display.set_caption("game")


# 匯入主角圖片
actorIMG = pygame.image.load("/Users/zhangxiangxian/Desktop/racecar.png")

# 匯入地圖image，並取得長寬資訊
bg = pygame.image.load("/Users/zhangxiangxian/Desktop/1.1-4d046d33a07490f813867425851deff9.jpg")
map_width = bg.get_width()
map_height = bg.get_height()


# 定義主角移動方式的函數
def move(x,y):
    screen.blit(actorIMG, (x,y))

# 設定主角起始位置
role_x, role_y = screen_width * 0.45, screen_height * 0.8
# 初始化主角移動量
x_change, y_change = 0, 0



# 開始主程式，建立一個無窮迴圈
quit = False
while not quit:

    for event in pygame.event.get():
        # 退出程式
        if event.type == pygame.QUIT:
            quit = True

        # 使用者用鍵盤操控人物移動
        if event.type == pygame.KEYDOWN:
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

    # 將x, y 移動量加到主角本身的座標上
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

    # 以 map_x 和 map_y 顯示地圖
    screen.blit(bg, (map_x, map_y))
    # 將人物顯示出來，因為座標的關係，將人物的座標加上地圖的座標，可以在大多情況下，人物在畫面的中心
    move(map_x + role_x, map_y + role_y)

    # 將剛才的變動在畫面上進行更新
    pygame.display.update()
    clock.tick(60)

pygame.quit()

