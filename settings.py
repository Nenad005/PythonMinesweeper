import wx
import pygame
import os

app = wx.App(False)
width, height = wx.GetDisplaySize()
del(app)

difficulty = 3

difficulties = {
    #dif - width, height, mines
    1 : [9, 9, 10],
    2 : [16, 16, 40],
    3 : [30, 16, 99]
}

TILE_SIZE = (width // difficulties[3][0]) // 1.5
WIDTH = TILE_SIZE * difficulties[difficulty][0]
HEIGHT = TILE_SIZE * difficulties[difficulty][1]
MINES = difficulties[difficulty][2]

BOARD = []
for i in range(difficulties[difficulty][1]):
    row = []
    for j in range(difficulties[difficulty][0]):
        row.append(0)
    BOARD.append(row)

#COLORS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#IMAGES

msUK = pygame.image.load(os.path.join("Assets", "msUK.png"))
msFLAG = pygame.image.load(os.path.join("Assets", "msFLAG.png"))

msMT = pygame.image.load(os.path.join("Assets", "msMT.png"))

ms1 = pygame.image.load(os.path.join("Assets", "ms1.png"))
ms2 = pygame.image.load(os.path.join("Assets", "ms2.png"))
ms3 = pygame.image.load(os.path.join("Assets", "ms3.png"))
ms4 = pygame.image.load(os.path.join("Assets", "ms4.png"))
ms5 = pygame.image.load(os.path.join("Assets", "ms5.png"))
ms6 = pygame.image.load(os.path.join("Assets", "ms6.png"))
ms7 = pygame.image.load(os.path.join("Assets", "ms7.png"))
ms8 = pygame.image.load(os.path.join("Assets", "ms8.png"))

msFAIL = pygame.image.load(os.path.join("Assets", "msFAIL.png"))
msDEATH = pygame.image.load(os.path.join("Assets", "msDEATH.png"))