import pygame
import sys
from settings import *
from board import Board
pygame.init()


W_WIDTH, W_HEIGHT = WIDTH, HEIGHT
win = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
pygame.display.set_caption('MINESWEEPER')

board = Board()

class Game_State:
    def __init__(self):
        self.state = 'main'

    def main(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                clickT = event.button
                pos = pygame.mouse.get_pos()
                board.click(clickT, pos) 

        win.fill((0, 0, 0))
        board.draw_board(win)
        board.draw_boardUK(win)
        pygame.display.flip()

    def other(self):
        pass

    def state_setter(self):
        if self.state == 'main': self.main()
        if self.state == 'score': self.other()

clock = pygame.time.Clock()
gameloop = Game_State()

def main():
    while True:
        gameloop.state_setter()
        clock.tick(60)

if __name__ == '__main__':
    main()