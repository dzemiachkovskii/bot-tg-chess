class Game:
    def __init__(self):
        self.board = [
            [8, 9, 10, 11, 12, 10, 9, 8],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [2, 3, 4, 5, 6, 4, 3, 2]
        ]
        self.user_turn = True

    def move_from(self, x, y):
        if not self.user_turn:
            return
        figure = self.board[x][y]
        # set figure to ready state
        if figure in range(1, 7):
            self.board[x][y] = [self.board[x][y]]
        # clean all red dots & figure ready state
        for i in range(0, 8):
            for j in range(0, 8):
                if type(self.board[i][j]) == list:
                    if self.board[i][j][0] == 13:
                        self.board[i][j] = self.board[i][j][1]
                    else:
                        self.board[i][j] = self.board[i][j][0]
        # /clean all red dots
        # plot possible steps on board & save current condition of tiles
        if figure == 1:
            if x - 2 < 0:
                return -1
            self.board[x - 2][y] = [13, self.board[x - 2][y]]
            if x == 6:
                self.board[x - 1][y] = [13, self.board[x - 1][y]]
        elif figure == 2:
            # up
            for i in range(x, -1, -1):
                if i == x:
                    continue
                if self.board[i][y] in range(1, 7):
                    break
                if self.board[i][y] in range(7, 13):
                    self.board[i][y] = [13, self.board[i][y]]
                    break
                self.board[i][y] = [13, self.board[i][y]]
            # right
            for j in range(y, 8):
                if j == y:
                    continue
                if self.board[x][j] in range(1, 7):
                    break
                if self.board[x][j] in range(7, 13):
                    self.board[x][j] = [13, self.board[x][j]]
                    break
                self.board[x][j] = [13, self.board[x][j]]
            # down
            for i in range(x, 8):
                if i == x:
                    continue
                if self.board[i][y] in range(1, 7):
                    break
                if self.board[i][y] in range(7, 13):
                    self.board[i][y] = [13, self.board[i][y]]
                    break
                self.board[i][y] = [13, self.board[i][y]]
            # left
            for j in range(y, -1, -1):
                if j == y:
                    continue
                if self.board[x][j] in range(1, 7):
                    break
                if self.board[x][j] in range(7, 13):
                    self.board[x][j] = [13, self.board[x][j]]
                    break
                self.board[x][j] = [13, self.board[x][j]]
        elif figure == 3:
            pass
        elif figure == 4:
            pass
        elif figure == 5:
            pass
        elif figure == 6:
            pass

    def move_to(self, x, y):
        if type(self.board[x][y]) == list:
            self.user_turn = False
