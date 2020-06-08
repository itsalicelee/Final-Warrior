import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame, const
from block import Block

'''
設定不能行走的地方
'''

# 上方邊界
block_up = Block(0, 61 ,2000, 1)

# 下方邊界
block_down = Block(0, 1200, 2000, 1)

# 左方邊界
block_left = Block(65, 0, 1, 1300)

# 右方邊界
block_right = Block(1800, 0, 1, 1300)

block_left_and_down = Block(0, 1140, 793, 50)
block_right_and_down = Block(1100, 1150, 793, 50)


# 建立群組，並把所有的邊界加入群組
group = pygame.sprite.Group()
group.add(block_up, block_down, block_left, block_right, block_left_and_down, block_right_and_down)
