import pygame, const
from block import Block

'''
設定不能行走的地方
'''

# 上方邊界
block_1 = Block(0, 0 ,1900, 5)

# 下方邊界
block_2 = Block(0, 1220, 1900, 5)

# 右方邊界
block_3 = Block(1900, 0, 5, 1200)

# 左方邊界
# block_4 = Block(1900, 0, 5, 1200)


# 建立群組，並把所有的邊界加入群組
group = pygame.sprite.Group()
group.add(block_1, block_2, block_3)