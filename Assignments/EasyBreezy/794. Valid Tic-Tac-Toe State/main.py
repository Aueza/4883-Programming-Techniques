def checkWin(board, xCount, oCount):
    # Helper function to check if a specific player has won
    def hasWon(player):  
        # Check rows
        for row in board:
            if row[0] == player and row[0] == row[1] == row[2]:
                return True
        # Check columns
        for c in range(0,3):
            if board[0][c] == player and board[0][c] == board[1][c] == board[2][c]:
                return True
        # Check diagonals
        if board[0][0] == player and board[0][0] == board[1][1] == board[2][2]:
            return True
        if board[0][2] == player and board[0][2] == board[1][1] == board[2][0]:
            return True
        # That player has not won
        return False

    # Check if X or O has won
    xWins = hasWon('X')
    oWins = hasWon('O')

    # If both players have win, game is invalid.
    if xWins == True and oWins == True:
        return False
    # If X wins they should have one more than O.
    if xWins == True and xCount != oCount + 1:
        return False
    # If O wins they should have the same number as X.
    if oWins == True and xCount != oCount:
        return False
    # There is a true winner.
    return True
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        #initialize x and o count.
        xCount = 0
        oCount = 0
        totalCount = 0
        
        # loops to count x and o's
        for row in board:
            for ch in row:
                totalCount += 1
                if ch == 'X':
                    xCount += 1
                elif ch == 'O':
                    oCount += 1

        # number of o's should never be more than number of x's
        if oCount > xCount:
            return False
        # if the difference is more than 1 then someone was skipped or went out of turn.
        elif abs(xCount - oCount) > 1:
            return False
        # check for winner.
        else:
            return checkWin(board, xCount, oCount)
        
