import pygame as pyg
import sys
import PawnClass.functions
import KingClass.functions

class gameWindow:
    def __init__(self):
        self.height = self.width = 500
        pyg.font.init()
        self.window = pyg.display.set_mode((self.width+220, self.height))
        self.sidebar = pyg.transform.scale(pyg.image.load('/Users/surya/Documents/Checkers-Online/Assets/sideScreen.png'), (200, self.height))
        self.boardImage = pyg.transform.flip(pyg.transform.scale(pyg.image.load("/Users/surya/Documents/Checkers-Online/Assets/CheckersBoard.png"), (self.width, self.height)), False, True)
        self.run = True
        self.turn = 'bn'
        self.selected = (-1, 0)
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
        #self.PeicesPositions[5][6] = 'wp'
        #self.PeicesPositions = [
        #    ['', '', '', '', '', '', '', ''],
        #    ['', '', 'wp', '', '', '', 'bp', ''],
        #    ['', '', '', '', '', '', '', ''],
        #    ['', '', 'wp', '', '', '', '', ''],
        #    ['', 'bp', '', '', '', '', '', 'bp'],
        #    ['bp', '', '', '', 'bp', '', '', ''],
        #    ['', '', '', '', '', '', '', ''],
        #    ['bp', '', '', '', '', '', '', '']
        #]
        for i in range(8):
            for j in range(8):
                if self.PeicesPositions[i][j] != '':
                    self.PeicesClass.append([i, j, PawnClass.functions.Pawn(self.PeicesPositions[i][j][0], *self.boardPositions[i][j].center)])

    def findMoves(self):
        self.moves = []
        for i in range(8):
            for j in range(8):
                if self.PeicesPositions[i][j] != '' and self.PeicesPositions[i][j][0] == self.turn[0] == 'b':
                    if self.PeicesPositions[i][j][1] == 'p':
                        # Pawn settings
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
                            if self.PeicesPositions[i-1][j-1] != '' and self.PeicesPositions[i-1][j-1][0] != 'b':
                                if j != 1 and i != 1:
                                    if self.PeicesPositions[i-2][j-2] == '':
                                        self.moves.append({'initial position':(i, j), 'final position':(i-2, j-2), 'type of move':'f'})
                            if self.PeicesPositions[i-1][j+1] != '' and self.PeicesPositions[i-1][j+1][0] != 'b':
                                if j != 6 and i != 1:
                                    if self.PeicesPositions[i-2][j+2] == '':
                                        self.moves.append({'initial position':(i, j), 'final position':(i-2, j+2), 'type of move':'f'})
                        else:
                            if j == 7 and i != 1:
                                if self.PeicesPositions[i-1][j-1] != '' and self.PeicesPositions[i-1][j-1] != '' and self.PeicesPositions[i-1][j-1][0] != 'b':
                                    if self.PeicesPositions[i-2][j-2] == '':
                                        self.moves.append({'initial position':(i, j), 'final position':(i-2, j-2), 'type of move':'f'})
                            elif j == 0 and i != 1:
                                if self.PeicesPositions[i-2][j+2] == '' and self.PeicesPositions[i-1][j+1] != '' and self.PeicesPositions[i-1][j+1][0] != 'b':
                                        self.moves.append({'initial position':(i, j), 'final position':(i-2, j+2), 'type of move':'f'})
                    else:
                        #king setting
                        #Now to check diogionally upward and downward 2 positions
                        #condition to check for not forced moves
                        if j != 0 and j != 7:
                            if i != 0:
                                if self.PeicesPositions[i-1][j-1] == '':
                                    self.moves.append({'initial position':(i, j), 'final position':(i-1, j-1), 'type of move':'n'})
                                if self.PeicesPositions[i-1][j+1] == '':
                                    self.moves.append({'initial position':(i, j), 'final position':(i-1, j+1), 'type of move':'n'})
                            if i != 7:
                                if self.PeicesPositions[i+1][j-1] == '':
                                    self.moves.append({'initial position':(i, j), 'final position':(i+1, j-1), 'type of move':'n'})
                                if self.PeicesPositions[i+1][j+1] == '':
                                    self.moves.append({'initial position':(i, j), 'final position':(i+1, j+1), 'type of move':'n'})
                        else:
                            if j == 7:
                                if i != 0:
                                    if self.PeicesPositions[i-1][j-1] == '':
                                        self.moves.append({'initial position':(i, j), 'final position':(i-1, j-1), 'type of move':'n'})
                                if i != 7:
                                    if self.PeicesPositions[i+1][j-1] == '':
                                        self.moves.append({'initial position':(i, j), 'final position':(i+1, j-1), 'type of move':'n'})
                            else:
                                if i != 0:
                                    if self.PeicesPositions[i-1][j+1] == '':
                                        self.moves.append({'initial position':(i, j), 'final position':(i-1, j+1), 'type of move':'n'})
                                if i != 7:
                                    if self.PeicesPositions[i+1][j+1] == '':
                                        self.moves.append({'initial position':(i, j), 'final position':(i+1, j+1), 'type of move':'n'})
                        #condition of forced move
                        if j != 0 and j != 7:
                            if i != 0:
                                if self.PeicesPositions[i-1][j-1] != '' and self.PeicesPositions[i-1][j-1][0] != 'b':
                                    if j != 1 and i != 1:
                                        if self.PeicesPositions[i-2][j-2] == '':
                                            self.moves.append({'initial position':(i, j), 'final position':(i-2, j-2), 'type of move':'f'})
                                if self.PeicesPositions[i-1][j+1] != '' and self.PeicesPositions[i-1][j+1][0] != 'b':
                                    if j != 6 and i != 1:
                                        if self.PeicesPositions[i-2][j+2] == '':
                                            self.moves.append({'initial position':(i, j), 'final position':(i-2, j+2), 'type of move':'f'})
                            if i != 7:
                                if self.PeicesPositions[i+1][j-1] != '' and self.PeicesPositions[i+1][j-1][0] != 'b':
                                    if j != 1 and i != 6:
                                        if self.PeicesPositions[i+2][j-2] == '':
                                            self.moves.append({'initial position':(i, j), 'final position':(i+2, j-2), 'type of move':'f'})
                                if self.PeicesPositions[i+1][j+1] != '' and self.PeicesPositions[i+1][j+1][0] != 'b':
                                    if j != 6 and i != 6:
                                        if self.PeicesPositions[i+2][j+2] == '':
                                            self.moves.append({'initial position':(i, j), 'final position':(i+2, j+2), 'type of move':'f'})
                        else:
                            if j == 7 and i != 1:
                                if self.PeicesPositions[i-1][j-1] != '' and self.PeicesPositions[i-1][j-1] != '' and self.PeicesPositions[i-1][j-1][0] != 'b':
                                    if self.PeicesPositions[i-2][j-2] == '':
                                        self.moves.append({'initial position':(i, j), 'final position':(i-2, j-2), 'type of move':'f'})
                            elif j == 0 and i != 1:
                                if self.PeicesPositions[i-2][j+2] == '' and self.PeicesPositions[i-1][j+1] != '' and self.PeicesPositions[i-1][j+1][0] != 'b':
                                        self.moves.append({'initial position':(i, j), 'final position':(i-2, j+2), 'type of move':'f'})
                            if j == 7 and i != 6:
                                if self.PeicesPositions[i+1][j-1] != '' and self.PeicesPositions[i+1][j-1][0] != 'b':
                                    if self.PeicesPositions[i+2][j-2] == '':
                                        self.moves.append({'initial position':(i, j), 'final position':(i+2, j-2), 'type of move':'f'})
                            elif j == 0 and i != 6:
                                if self.PeicesPositions[i+2][j+2] == ''  and self.PeicesPositions[i+1][j+1] != '' and self.PeicesPositions[i+1][j+1][0] != 'b':
                                        self.moves.append({'initial position':(i, j), 'final position':(i+2, j+2), 'type of move':'f'})
                elif self.PeicesPositions[i][j] != '' and self.PeicesPositions[i][j][0] == self.turn[0] == 'w':
                    if self.PeicesPositions[i][j][1] == 'p':
                        # Pawn settings
                        #Now to check diogionally upward 2 positions
                        #condition to check for not forced moves
                        if j != 0 and j != 7:
                            if self.PeicesPositions[i+1][j-1] == '':
                                self.moves.append({'initial position':(i, j), 'final position':(i+1, j-1), 'type of move':'n'})
                            if self.PeicesPositions[i+1][j+1] == '':
                                self.moves.append({'initial position':(i, j), 'final position':(i+1, j+1), 'type of move':'n'})
                        else:
                            if j == 7:
                                if self.PeicesPositions[i+1][j-1] == '':
                                    self.moves.append({'initial position':(i, j), 'final position':(i+1, j-1), 'type of move':'n'})
                            else:
                                if self.PeicesPositions[i+1][j+1] == '':
                                    self.moves.append({'initial position':(i, j), 'final position':(i+1, j+1), 'type of move':'n'})
                        #condition of forced move
                        if j != 0 and j != 7:
                            if self.PeicesPositions[i+1][j-1] != '' and self.PeicesPositions[i+1][j-1][0] != 'w':
                                if j != 1 and i != 6:
                                    if self.PeicesPositions[i+2][j-2] == '':
                                        self.moves.append({'initial position':(i, j), 'final position':(i+2, j-2), 'type of move':'f'})
                            if self.PeicesPositions[i+1][j+1] != '' and self.PeicesPositions[i+1][j+1][0] != 'w':
                                if j != 6 and i != 6:
                                    if self.PeicesPositions[i+2][j+2] == '':
                                        self.moves.append({'initial position':(i, j), 'final position':(i+2, j+2), 'type of move':'f'})
                        else:
                            if j == 7 and i != 6:
                                if self.PeicesPositions[i+1][j-1] != '' and self.PeicesPositions[i+1][j-1] != '' and self.PeicesPositions[i+1][j-1][0] != 'w':
                                    if self.PeicesPositions[i+2][j-2] == '':
                                        self.moves.append({'initial position':(i, j), 'final position':(i+2, j-2), 'type of move':'f'})
                            elif j == 0 and i != 6:
                                if self.PeicesPositions[i+2][j+2] == '' and self.PeicesPositions[i+1][j+1] != '' and self.PeicesPositions[i+1][j+1][0] != 'w':
                                        self.moves.append({'initial position':(i, j), 'final position':(i+2, j+2), 'type of move':'f'})
                    else:
                        #king setting
                        #Now to check diogionally upward and downward 2 positions
                        #condition to check for not forced moves
                        if j != 0 and j != 7:
                            if i != 0:
                                if self.PeicesPositions[i-1][j-1] == '':
                                    self.moves.append({'initial position':(i, j), 'final position':(i-1, j-1), 'type of move':'n'})
                                if self.PeicesPositions[i-1][j+1] == '':
                                    self.moves.append({'initial position':(i, j), 'final position':(i-1, j+1), 'type of move':'n'})
                            if i != 7:
                                if self.PeicesPositions[i+1][j-1] == '':
                                    self.moves.append({'initial position':(i, j), 'final position':(i+1, j-1), 'type of move':'n'})
                                if self.PeicesPositions[i+1][j+1] == '':
                                    self.moves.append({'initial position':(i, j), 'final position':(i+1, j+1), 'type of move':'n'})
                        else:
                            if j == 7:
                                if i != 0:
                                    if self.PeicesPositions[i-1][j-1] == '' and i != 0:
                                        self.moves.append({'initial position':(i, j), 'final position':(i-1, j-1), 'type of move':'n'})
                                if i != 7:
                                    if self.PeicesPositions[i+1][j-1] == '' and i != 7:
                                        self.moves.append({'initial position':(i, j), 'final position':(i+1, j-1), 'type of move':'n'})
                            else:
                                if i != 0:
                                    if self.PeicesPositions[i-1][j+1] == '' and i != 0:
                                        self.moves.append({'initial position':(i, j), 'final position':(i-1, j+1), 'type of move':'n'})
                                if i != 7:
                                    if self.PeicesPositions[i+1][j+1] == '' and i != 7:
                                        self.moves.append({'initial position':(i, j), 'final position':(i+1, j+1), 'type of move':'n'})
                        #condition of forced move
                        if j != 0 and j != 7:
                            if i != 0:
                                if self.PeicesPositions[i-1][j-1] != '' and self.PeicesPositions[i-1][j-1][0] != 'w':
                                    if j != 1 and i != 1:
                                        if self.PeicesPositions[i-2][j-2] == '':
                                            self.moves.append({'initial position':(i, j), 'final position':(i-2, j-2), 'type of move':'f'})
                                if self.PeicesPositions[i-1][j+1] != '' and self.PeicesPositions[i-1][j+1][0] != 'w':
                                    if j != 6 and i != 1:
                                        if self.PeicesPositions[i-2][j+2] == '':
                                            self.moves.append({'initial position':(i, j), 'final position':(i-2, j+2), 'type of move':'f'})
                            elif i != 7:
                                if self.PeicesPositions[i+1][j-1] != '' and self.PeicesPositions[i+1][j-1][0] != 'w':
                                    if j != 1 and i != 6:
                                        if self.PeicesPositions[i+2][j-2] == '':
                                            self.moves.append({'initial position':(i, j), 'final position':(i+2, j-2), 'type of move':'f'})
                                if self.PeicesPositions[i+1][j+1] != '' and self.PeicesPositions[i+1][j+1][0] != 'w':
                                    if j != 6 and i != 6:
                                        if self.PeicesPositions[i+2][j+2] == '':
                                            self.moves.append({'initial position':(i, j), 'final position':(i+2, j+2), 'type of move':'f'})
                        else:
                            if j == 7 and i != 1 and i != 0 and i != 0:
                                if self.PeicesPositions[i-1][j-1] != '' and self.PeicesPositions[i-1][j-1] != '' and self.PeicesPositions[i-1][j-1][0] != 'w':
                                    if self.PeicesPositions[i-2][j-2] == '':
                                        self.moves.append({'initial position':(i, j), 'final position':(i-2, j-2), 'type of move':'f'})
                            elif j == 0 and i != 1 and i != 7 and i != 7:
                                if self.PeicesPositions[i-2][j+2] == '' and self.PeicesPositions[i-1][j+1] != '' and self.PeicesPositions[i-1][j+1][0] != 'w':
                                        self.moves.append({'initial position':(i, j), 'final position':(i-2, j+2), 'type of move':'f'})
                            if j == 7 and i != 6 and i != 0 and i != 0:
                                if self.PeicesPositions[i+1][j-1] != '' and self.PeicesPositions[i+1][j-1][0] != 'w':
                                    if self.PeicesPositions[i+2][j-2] == '':
                                        self.moves.append({'initial position':(i, j), 'final position':(i+2, j-2), 'type of move':'f'})
                            elif j == 0 and i != 6 and i != 7 and i != 7:
                                if self.PeicesPositions[i+2][j+2] == ''  and self.PeicesPositions[i+1][j+1] != '' and self.PeicesPositions[i+1][j+1][0] != 'w':
                                        self.moves.append({'initial position':(i, j), 'final position':(i+2, j+2), 'type of move':'f'})
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
                    
    def move(self, moveDict):
        # to move a piece if it is not a forced move and not succeding a forced move
        if moveDict['type of move'] == 'n' and self.turn[1] == 'n':
            self.PeicesPositions[moveDict['final position'][0]][moveDict['final position'][1]] = self.PeicesPositions[moveDict['initial position'][0]][moveDict['initial position'][1]]
            self.PeicesPositions[moveDict['initial position'][0]][moveDict['initial position'][1]] = ''
            for i in self.PeicesClass:
                if i[0] == moveDict['initial position'][0] and i[1] == moveDict['initial position'][1]:
                    i[0], i[1] = moveDict['final position'][0], moveDict['final position'][1]
                    i[-1].spriteRect.center = self.boardPositions[moveDict['final position'][0]][moveDict['final position'][1]].center
                    if moveDict['final position'][0] == 0 and self.turn[0] == 'b':
                        i[-1] = KingClass.functions.King('b', *i[-1].spriteRect.center)
                        self.PeicesPositions[moveDict['final position'][0]][moveDict['final position'][1]] = 'bk'
                        self.turn = 'bn'
                    if moveDict['final position'][0] == 7 and self.turn[0] == 'w':
                        i[-1] = KingClass.functions.King('w', *i[-1].spriteRect.center)
                        self.PeicesPositions[moveDict['final position'][0]][moveDict['final position'][1]] = 'wk'
                        self.turn = 'wn'
            if self.turn == 'wn':
                self.turn = 'bn'
            else:
                self.turn = 'wn'
        # to move forced peices
        elif moveDict['type of move'] == 'f' and self.turn[1] == 'n':
            self.PeicesPositions[moveDict['final position'][0]][moveDict['final position'][1]] = self.PeicesPositions[moveDict['initial position'][0]][moveDict['initial position'][1]]
            self.PeicesPositions[moveDict['initial position'][0]][moveDict['initial position'][1]] = ''
            self.PeicesPositions[(moveDict['initial position'][0]+moveDict['final position'][0])//2][(moveDict['initial position'][1]+moveDict['final position'][1])//2] = ''
            j = 0
            while j < len(self.PeicesClass):
                i = self.PeicesClass[j]
                if i[0] == moveDict['initial position'][0] and i[1] == moveDict['initial position'][1]:
                    i[0], i[1] = moveDict['final position'][0], moveDict['final position'][1]
                    i[-1].spriteRect.center = self.boardPositions[moveDict['final position'][0]][moveDict['final position'][1]].center
                    self.findMoves()
                    flag = False
                    for k in self.moves:
                        if k['type of move'] == 'f' and moveDict['final position'] == k['initial position']:
                            flag = True
                    if flag:
                        if self.turn == 'wn':
                            self.turn = f'wf {i[0]} {i[1]}'
                        else:
                            self.turn = f'bf {i[0]} {i[1]}'
                    else:
                        if self.turn == 'wn':
                            self.turn = 'bn'
                        else:
                            self.turn = 'wn'
                    if moveDict['final position'][0] == 0 and (self.turn == 'wn' or self.turn[0] == 'b'):
                        i[-1] = KingClass.functions.King('b', *i[-1].spriteRect.center)
                        self.PeicesPositions[moveDict['final position'][0]][moveDict['final position'][1]] = 'bk'
                        self.turn = 'wn'
                    if moveDict['final position'][0] == 7 and (self.turn == 'bn' or self.turn[0] == 'w'):
                        i[-1] = KingClass.functions.King('w', *i[-1].spriteRect.center)
                        self.PeicesPositions[moveDict['final position'][0]][moveDict['final position'][1]] = 'wk'
                        self.turn = 'bn'
                elif i[0] == (moveDict['initial position'][0]+moveDict['final position'][0])//2 and i[1] == (moveDict['initial position'][1]+moveDict['final position'][1])//2:
                    self.PeicesClass.pop(j)
                    j -= 1
                j += 1
        elif moveDict['type of move'] == 'f' and self.turn[1] == 'f':
            if (int(self.turn[3]), int(self.turn[5])) == moveDict['initial position']:
                self.PeicesPositions[moveDict['final position'][0]][moveDict['final position'][1]] = self.PeicesPositions[moveDict['initial position'][0]][moveDict['initial position'][1]]
                self.PeicesPositions[moveDict['initial position'][0]][moveDict['initial position'][1]] = ''
                self.PeicesPositions[(moveDict['initial position'][0]+moveDict['final position'][0])//2][(moveDict['initial position'][1]+moveDict['final position'][1])//2] = ''
                j = 0
                while j < len(self.PeicesClass):
                    i = self.PeicesClass[j]
                    if i[0] == moveDict['initial position'][0] and i[1] == moveDict['initial position'][1]:
                        i[0], i[1] = moveDict['final position'][0], moveDict['final position'][1]
                        i[-1].spriteRect.center = self.boardPositions[moveDict['final position'][0]][moveDict['final position'][1]].center
                        flag1 = False
                        if moveDict['final position'][0] == 0 and (self.turn == 'wn' or self.turn[0] == 'b'):
                            i[-1] = KingClass.functions.King('b', *i[-1].spriteRect.center)
                            self.PeicesPositions[moveDict['final position'][0]][moveDict['final position'][1]] = 'bk'
                            self.turn = 'wn'
                            flag1 = True
                        elif moveDict['final position'][0] == 7 and (self.turn == 'bn' or self.turn[0] == 'w'):
                            i[-1] = KingClass.functions.King('w', *i[-1].spriteRect.center)
                            self.PeicesPositions[moveDict['final position'][0]][moveDict['final position'][1]] = 'wk'
                            self.turn = 'bn'
                            flag1 = True
                        self.findMoves()
                        flag = False
                        for k in self.moves:
                            if k['type of move'] == 'f' and moveDict['final position'] == k['initial position']:
                                flag = True
                        if not flag1:
                            if flag:
                                if self.turn[0] == 'w':
                                    self.turn = f'wf {i[0]} {i[1]}'
                                else:
                                    self.turn = f'bf {i[0]} {i[1]}'
                                    print('hello')
                            else:
                                if self.turn == 'wn':
                                    self.turn = 'bn'
                                else:
                                    self.turn = 'wn'
                        
                    elif i[0] == (moveDict['initial position'][0]+moveDict['final position'][0])//2 and i[1] == (moveDict['initial position'][1]+moveDict['final position'][1])//2:
                        self.PeicesClass.pop(j)
                        j -= 1
                    j += 1


    def main(self):
        while self.run:
            self.window.blit(self.boardImage, (0, 0))
            self.window.blit(self.sidebar, (self.width+10, 0))
            for i in range(8):
                for j in range(8):
                        text = pyg.font.SysFont('Arial Black',15)
                        tempSurface = pyg.Surface((self.boardPositions[i][j].width, self.boardPositions[i][j].height))
                        img = text.render(f'{65-((i*8)+j+1)}', True, (255, 255, 255))
                        tempSurface.set_alpha(70)
                        tempSurface.blit(img, (0, 0))
                        self.window.blit(tempSurface, self.boardPositions[i][j].topleft)
            for i in range(len(self.PeicesClass[::-1])):
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
                    flag = False
                    for i in range(8):
                        for j in range(8):
                            if self.boardPositions[i][j].collidepoint(pyg.mouse.get_pos()):
                                for m in self.moves:
                                    if (i, j) == m['initial position']:
                                        self.selected = (i, j)
                                        flag = True
                                    if (i, j) == m['final position'] and m['initial position'] == self.selected:
                                        if self.selected != (-1, 0):
                                            self.move(m)
                                            
                    if flag == False:
                        self.selected = (-1, 0)
            c = 0
            for i in self.PeicesPositions:
                c += i.count('wp')
                c += i.count('wk')
            c1 = 0
            for i in self.PeicesPositions:
                c1 += i.count('bp')
                c1 += i.count('bk')
            if c1 == 0:
                print('White Wins')
                self.run = False
                pyg.quit()
                sys.exit()
            if c == 0:
                print('Black Wins')
                self.run = False
                pyg.quit()
                sys.exit()
            pyg.display.update()

gameWindow()
