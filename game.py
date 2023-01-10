import pygame as pyg
import sys
import PawnClass.functions

class gameWindow:
    def __init__(self):
        self.height = self.width = 500
        self.window = pyg.display.set_mode((self.width, self.height))
        self.boardImage = pyg.transform.flip(pyg.transform.scale(pyg.image.load("Assets/CheckersBoard.png"), (self.width, self.height)), False, True)
        self.run = True
        self.turn = 'bn'
        self.selected = (0, 0)
        self.definitions()
        self.main()

    def definitions(self):
        self.boardPositions = []
        for i in range(8):
            self.boardPositions.append([])
            for j in range(8):
                self.boardPositions[i].append(pyg.Rect(j*(60)+12, i*(60)+12, 60, 60))
        self.PeicesPositions = []
        self.PeicesClass = []
        for i in range(8):
            self.PeicesPositions.append([])
            for j in range(8):
                if j % 2:
                    if i == 0:
                        self.PeicesPositions[i].append('wp')
                    elif i == 6:
                        self.PeicesPositions[i].append('bp')
                    else:
                        self.PeicesPositions[i].append('')
                else:
                    if i == 1:
                        self.PeicesPositions[i].append('wp')
                    elif i == 7:
                        self.PeicesPositions[i].append('bp')
                    else:
                        self.PeicesPositions[i].append('')
        self.PeicesPositions[5][2] = 'wp'
        for i in range(8):
            for j in range(8):
                if self.PeicesPositions[i][j] != '':
                    self.PeicesClass.append([i, j, PawnClass.functions.Pawn(self.PeicesPositions[i][j][0], *self.boardPositions[i][j].center)])

    def findMoves(self):
        self.moves = []
        for i in range(8):
            for j in range(8):
                if self.PeicesPositions[i][j] != '' and self.PeicesPositions[i][j][0] == self.turn[0]:
                    if self.PeicesPositions[i][j][1] == 'p':
                        #Now to check diogionally upward 2 positions
                        #condition to check for not forced moves
                        if j != 0 and j != 7:
                            if self.PeicesPositions[i-1][j-1] == '':
                                self.moves.append({'initial position':(i, j), 'final position':(i-1, j-1), 'type of move':'n'})
                            if self.PeicesPositions[i-1][j+1] == '':
                                self.moves.append({'initial position':(i, j), 'final position':(i-1, j+1), 'type of move':'n'})
                        else:
                            if j == 7:
                                if self.PeicesPositions[i-1][j-1] == '':
                                    self.moves.append({'initial position':(i, j), 'final position':(i-1, j-1), 'type of move':'n'})
                            else:
                                if self.PeicesPositions[i-1][j+1] == '':
                                    self.moves.append({'initial position':(i, j), 'final position':(i-1, j+1), 'type of move':'n'})
                        #condition of forced move
                        if j != 0 and j != 7:
                            if self.PeicesPositions[i-1][j-1] != '' and self.PeicesPositions[i-1][j-1][0] != self.turn[0]:
                                if j != 1 and i != 1:
                                    if self.PeicesPositions[i-2][j-2] == '':
                                        self.moves.append({'initial position':(i, j), 'final position':(i-2, j-2), 'type of move':'f'})
                            if self.PeicesPositions[i-1][j+1] != '' and self.PeicesPositions[i-1][j+1][0] != self.turn[0]:
                                if j != 6 and i != 1:
                                    if self.PeicesPositions[i-2][j+2] == '':
                                        self.moves.append({'initial position':(i, j), 'final position':(i-2, j+2), 'type of move':'f'})
                        else:
                            if j == 7 and i != 1:
                                if self.PeicesPositions[i-1][j-1] != '' and self.PeicesPositions[i-1][j-1][0] != self.turn[0]:
                                    if self.PeicesPositions[i-2][j-2] == '':
                                        self.moves.append({'initial position':(i, j), 'final position':(i-2, j-2), 'type of move':'f'})
                            elif j == 0 and i != 1:
                                if self.PeicesPositions[i-2][j+2] == '':
                                        self.moves.append({'initial position':(i, j), 'final position':(i-2, j+2), 'type of move':'f'})

    def filterMoves(self):
        # checking if there is any forced move possible
        flag = False
        for i in self.moves:
            if i['type of move'] == 'f':
                flag = True
        # if there is even one forced move, we are going to remove all not forced move from the list
        if flag:
            i = 0
            while i <len(self.moves):
                if self.moves[i]['type of move'] == 'n':
                    self.moves.pop(i)
                else:
                    i += 1

    def main(self):
        while self.run:
            self.window.blit(self.boardImage, (0, 0))
            for i in range(len(self.PeicesClass)):
                self.window.blit(self.PeicesClass[i][-1].spriteImage, self.PeicesClass[i][-1].spriteRect)
                self.findMoves()
                self.filterMoves()
            for i in self.moves:
                #print(self.boardPositions[i['final position'][0]][i['final position'][1]])
                if i['initial position'][0] == self.selected[0] and i['initial position'][1] == self.selected[1]:
                    pyg.draw.circle(self.window, (255, 0, 0), self.boardPositions[i['final position'][0]][i['final position'][1]].center, 5)
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    self.run = False
                    pyg.quit()
                    sys.exit()
                elif event.type == pyg.MOUSEBUTTONDOWN:
                    for i in range(8):
                        for j in range(8):
                            if self.boardPositions[i][j].collidepoint(pyg.mouse.get_pos()):
                                self.selected = (i, j)

            pyg.display.update()

gameWindow()
