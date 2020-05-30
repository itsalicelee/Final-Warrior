import pygame, const

from block import Block
# 上方邊界
block_1 = Block(0, 0 ,1900, 5)

# 下方邊界
block_2 = Block(0, 1220, 1900, 5)

# 右方邊界
block_3 = Block(1900, 0, 5, 1200)

# 左方邊界
block_3 = Block(1900, 0, 5, 1200)


group = pygame.sprite.Group()

group.add(block_1, block_2, block_3)