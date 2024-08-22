import random, copy
from settings import *

class Board:

    def __init__(self) -> None:
        self.boardUK = copy.deepcopy(BOARD)
        self.board = self.get_board()
        self.removed = set()
        self.count()

    def draw_boardUK(self, win):
        for i in range(len(self.boardUK)):
            for j in range(len(self.boardUK[i])):
                if self.boardUK[i][j] == 0: win.blit(msUK, (j*TILE_SIZE, i*TILE_SIZE))
                if self.boardUK[i][j] == 1: win.blit(msFLAG, (j*TILE_SIZE, i*TILE_SIZE))
                if self.boardUK[i][j] == 2: win.blit(msDEATH, (j*TILE_SIZE, i*TILE_SIZE))

    def draw_board(self, win):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0: win.blit(msMT, (j*TILE_SIZE, i*TILE_SIZE))
                if self.board[i][j] == 1: win.blit(ms1, (j*TILE_SIZE, i*TILE_SIZE))
                if self.board[i][j] == 2: win.blit(ms2, (j*TILE_SIZE, i*TILE_SIZE))
                if self.board[i][j] == 3: win.blit(ms3, (j*TILE_SIZE, i*TILE_SIZE))
                if self.board[i][j] == 4: win.blit(ms4, (j*TILE_SIZE, i*TILE_SIZE))
                if self.board[i][j] == 5: win.blit(ms5, (j*TILE_SIZE, i*TILE_SIZE))
                if self.board[i][j] == 6: win.blit(ms6, (j*TILE_SIZE, i*TILE_SIZE))
                if self.board[i][j] == 7: win.blit(ms7, (j*TILE_SIZE, i*TILE_SIZE))
                if self.board[i][j] == 8: win.blit(ms8, (j*TILE_SIZE, i*TILE_SIZE))
                if self.board[i][j] == 9: win.blit(msFAIL, (j*TILE_SIZE, i*TILE_SIZE))

    def click(self, clickT, pos):
        row = int(pos[1]//TILE_SIZE)
        col = int(pos[0]/TILE_SIZE)

        if clickT != 1 and clickT != 3:
            return
        elif self.boardUK[row][col] == 2:
            return

        elif clickT == 1:
            if self.board[row][col] == 9 and self.boardUK[row][col] != 1:
                self.boardUK[row][col] = 2
                # self.end_game()
                return
            if self.boardUK[row][col] == 0:
                if self.board[row][col] == 0:
                    self.remove_surr(row, col)
                self.boardUK[row][col] = 3
        elif clickT == 3:
            if self.boardUK[row][col] == 1:
               self.boardUK[row][col] = 0
            elif self.boardUK[row][col] == 0:
               self.boardUK[row][col] = 1
        
    def remove_surr(self, row, col):
        if col < difficulties[difficulty][0] - 1:
            if self.board[row][col+1] == 0 and (row, col+1) not in self.removed:
                self.removed.add((row, col+1))
                self.boardUK[row][col+1] = 3
                self.remove_numbers(row, col+1)
                self.remove_surr(row, col+1)

        if col > 0:
            if self.board[row][col-1] == 0 and (row, col-1) not in self.removed:
                self.removed.add((row, col-1))
                self.boardUK[row][col-1] = 3
                self.remove_numbers(row, col-1)
                self.remove_surr(row, col-1)

        if row < difficulties[difficulty][1] - 1:
            if self.board[row+1][col] == 0 and (row+1, col) not in self.removed:
                self.removed.add((row+1, col))
                self.boardUK[row+1][col] = 3
                self.remove_numbers(row+1, col)
                self.remove_surr(row+1, col)

        if row > 0:
            if self.board[row-1][col] == 0 and (row-1, col) not in self.removed:
                self.removed.add((row-1, col))
                self.boardUK[row-1][col] = 3
                self.remove_numbers(row-1, col)
                self.remove_surr(row-1, col)

        if col < difficulties[difficulty][0] - 1 and row < difficulties[difficulty][1] - 1:
            if self.board[row+1][col+1] == 0 and (row+1, col+1) not in self.removed:
                self.removed.add((row+1, col+1))
                self.boardUK[row+1][col+1] = 3
                self.remove_numbers(row+1, col+1)
                self.remove_surr(row+1, col+1)

        if col > 0 and row > 0:
            if self.board[row-1][col-1] == 0 and (row-1, col-1) not in self.removed:
                self.removed.add((row-1, col-1))
                self.boardUK[row-1][col-1] = 3
                self.remove_numbers(row-1, col-1)
                self.remove_surr(row-1, col-1)

        if row < difficulties[difficulty][1] - 1 and col > 0:
            if self.board[row+1][col-1] == 0 and (row+1, col-1) not in self.removed:
                self.removed.add((row+1, col-1))
                self.boardUK[row+1][col-1] = 3
                self.remove_numbers(row+1, col-1)
                self.remove_surr(row+1, col-1)

        if row > 0 and col < difficulties[difficulty][0] - 1:
            if self.board[row-1][col+1] == 0 and (row-1, col+1) not in self.removed:
                self.removed.add((row-1, col+1))
                self.boardUK[row-1][col+1] = 3
                self.remove_numbers(row-1, col+1)
                self.remove_surr(row-1, col+1)
        
    def remove_numbers(self, row, col):
        if row > 0:
            if self.board[row-1][col] not in [0,9]:
                self.boardUK[row-1][col] = 3
        if col > 0:
            if self.board[row][col-1] not in [0,9]:
                self.boardUK[row][col-1] = 3
        if row < difficulties[difficulty][1] - 1:
            if self.board[row+1][col] not in [0,9]:
                self.boardUK[row+1][col] = 3
        if col < difficulties[difficulty][0] - 1:
            if self.board[row][col+1] not in [0,9]:
                self.boardUK[row][col+1] = 3
        if row > 0 and col > 0:
           if self.board[row-1][col-1] not in [0,9]:
                self.boardUK[row-1][col-1] = 3
        if row > 0 and col < difficulties[difficulty][0] - 1:
           if self.board[row-1][col+1] not in [0,9]:
                self.boardUK[row-1][col+1] = 3
        if row < difficulties[difficulty][1] - 1 and col > 0:
           if self.board[row+1][col-1] not in [0,9]:
                self.boardUK[row+1][col-1] = 3
        if row < difficulties[difficulty][1] - 1 and col < difficulties[difficulty][0] - 1:
           if self.board[row+1][col+1] not in [0,9]:
                self.boardUK[row+1][col+1] = 3

    def get_board(self):
        board_under = copy.deepcopy(BOARD)
        self.plant_mines(board_under)
        self.get_numbers(board_under)
        return board_under

    def count(self):
        numbers = {
            'tiles' : 0,
            'mines' : 0,
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0,
            5 : 0,
            6 : 0,
            7 : 0,
            8 : 0,
        }
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                numbers['tiles'] += 1
                if self.board[i][j] == 1 : numbers[1] += 1
                elif self.board[i][j] == 2 : numbers[2] += 1
                elif self.board[i][j] == 3 : numbers[3] += 1
                elif self.board[i][j] == 4 : numbers[4] += 1
                elif self.board[i][j] == 5 : numbers[5] += 1
                elif self.board[i][j] == 6 : numbers[6] += 1
                elif self.board[i][j] == 7 : numbers[7] += 1
                elif self.board[i][j] == 8 : numbers[8] += 1
                elif self.board[i][j] == 9 : numbers['mines'] += 1

        print(f"mines - {numbers['mines']}, tiles - {numbers['tiles']}")
        print(f"1 - {numbers[1]}")
        print(f"2 - {numbers[2]}")
        print(f"3 - {numbers[3]}")
        print(f"4 - {numbers[4]}")
        print(f"5 - {numbers[5]}")
        print(f"6 - {numbers[6]}")
        print(f"7 - {numbers[7]}")
        print(f"8 - {numbers[8]}")

    def plant_mines(self, board):
        coords = []
        for i in range(difficulties[difficulty][2]):
            x = random.randint(0, difficulties[difficulty][0] - 1)
            y = random.randint(0, difficulties[difficulty][1] - 1)
            while (x,y) in coords:
                x = random.randint(0, difficulties[difficulty][0] - 1)
                y = random.randint(0, difficulties[difficulty][1] - 1)
            coords.append((x,y))
        for coord in coords:
            board[coord[1]][coord[0]] = 9

    def get_numbers(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                number = 0
                if board[i][j] == 9:
                    continue
                if j < len(board[i]) - 1:
                    if board[i][j+1] == 9 : number += 1
                if j > 0:
                    if board[i][j-1] == 9 : number += 1
                if i < len(board) - 1 and j < len(board[i]) - 1:
                    if board[i+1][j+1] == 9 : number += 1
                if i < len(board) - 1 and j > 0: 
                    if board[i+1][j-1] == 9 : number += 1
                if i > 0 and j < len(board[i]) - 1: 
                    if board[i-1][j+1] == 9 : number += 1
                if i > 0 and j > 0:
                    if board[i-1][j-1] == 9 : number += 1
                if i < len(board) - 1:
                    if board[i+1][j] == 9 : number += 1
                if i > 0:
                    if board[i-1][j] == 9 : number += 1
                board[i][j] = number