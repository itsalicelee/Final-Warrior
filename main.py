import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))  # 顯示視窗

# Title and icon
pygame.display.set_caption("casters")
icon = pygame.image.load("avatar.png")
pygame.display.set_icon(icon)

# Player
playerImage = pygame.image.load("avatar.png")
playerX = 370
playerY = 480


def player():
    screen.blit(playerImage, (playerX, playerY))


# Game Loop
running = True
while running:  # 死迴圈確保視窗一直顯示
    screen.fill((0, 0, 0))  # RGB background

    for event in pygame.event.get():  # 遍歷所有事件
        if event.type == pygame.QUIT:  # 如果單擊關閉視窗，則退出
            running = False

    player()

    pygame.display.update()



