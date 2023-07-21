import Board

class Piece:
    x = 0
    y = 0
    isAlive = True
    board = None

    def __init__(self, board):
        self.board = board

    def out(self, newx, newy):
        return newx >= 8 or newy >= 8 or newx < 0 or newy < 0

    def move(self, newx, newy):
        if self.out(newx, newy):
            print("Out of bounds!")
            return 0
        self.x = newx
        self.y = newy
        return 1

    def eat(self, character):
        character.isAlive = False
        self.board[character.x][character.y] = ''
        self.move(character.x, character.y)
        return 1

    def check(self, king):
        king.change_check_status(True)
        return 1


class Pawn(Piece):
    isFirstMove = True
    isQueen = False

    def eat(self, character):
        difference_x = character.x - self.x
        difference_y = character.y - self.y
        if difference_x == 1 and difference_y == 1:
            character.isAlive = False
            self.move(character.x, character.y)
            return 1
        return 0

    def is_valid_move(self, newx, newy):
        difference_x = newx - self.x
        difference_y = newy - self.y

        if (difference_x == 1 and difference_y == 0) or (self.isFirstMove and difference_x == 2 and difference_y == 0):
            return True
        return False

    def move(self, newx, newy):
        if self.out(newx, newy):
            print("Out of bounds!")
            return 0

        if self.is_valid_move(newx, newy):
            self.isFirstMove = False
            self.x = newx
            self.y = newy
            if self.y == 7:
                self.queening()
            return 1
        else:
            return 0

    def queening(self):
        self.isQueen = True

class Queen(Piece):
    def move(self, newx, newy):
        if self.out(newx, newy):
            print("Out of bounds!")
            return 0
        elif not self.is_valid_move(newx, newy):
            return 0
        self.x = newx
        self.y = newy
        return 1

    def is_valid_move(self, newx, newy):
        difference_x = newx - self.x
        difference_y = newy - self.y

        if difference_x == 0 and difference_y != 0: # this means the queen intends to  move vertically
            for y in range(min(self.y,newy), max(self.y, newy)):
                if self.board[self.x][y] != "":
                    return False

        if difference_y == 0 and difference_x != 0:
            for r in range(min(self.x, newx), max(self.x, newx)):
                if self.board[self.y][r] != "":
                    return False

        if difference_y != 0 and difference_x != 0 and difference_y == difference_x:
            if difference_x < 0: # negative direction
                for diff in range(difference_x, 1, -1):
                    if self.board[self.x + diff][self.y + diff] != "":
                        return False
            else:
                for diff in range(1, difference_x):
                    if self.board[self.x + diff][self.y + diff] != "":
                        return False



class King(Piece):
    isChecked = False

    def change_check_status(self, status):
        self.isChecked = status

class Rook(Piece):
    def move(self, newx, newy):
        if self.out(newx, newy):
            print("Out of bounds!")
            return 0
        elif not self.is_valid_move(newx, newy):
            return 0
        self.x = newx
        self.y = newy
        return 1

    def is_valid_move(self, newx, newy):
        difference_x = newx - self.x
        difference_y = newy - self.y

        if difference_x == 0 and difference_y != 0: # this means the queen intends to  move vertically
            for m in range(min(self.y,newy), max(self.y, newy)):
                if self.board[self.x][m] != "":
                    return False

        if difference_y == 0 and difference_x != 0:
            for z in range(min(self.x, newx), max(self.x, newx)):
                if self.board[self.y][z] != "":
                    return False

class Knight(Piece):

    def move(self, newx, newy):
        if self.out(newx, newy):
            print("Out of bounds!")
            return 0
        elif not self.is_valid_move(newx, newy):
            return 0
        self.x = newx
        self.y = newy
        return 1

    def is_valid_move(self, newx, newy):
        possible_moves = [[-1,2],[1,2],[2,1],[-2,-1],[-1,-2],[1,-2]]

        for i,j in possible_moves:
            if self.x + i == newx and self.y + j == newy:
                return True
        return False
