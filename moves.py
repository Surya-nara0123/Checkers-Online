def findMoves(self: object):
    self.moves = []
    for i in range(8):
        for j in range(8):
            if self.PeicesPositions[i][j][0] == self.turn[0] == 'b':
                if self.PeicesPositions[i][j][1] == 'p':
                    #check if it is an edge peice
                    if j != 0 and j != 7:
                        pass
                    else:
                        pass
                else:
                    pass