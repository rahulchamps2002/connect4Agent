def detect_threat(board, player):
    """
    [Modified] Updated to use player numbers (1 or 2) instead of strings like 'Player 1'.
    also checks if the opponent has a winning position from the given board state.
    """
    opponent = 2 if player == 1 else 1
    # [New code] check all cells to find opponent tokens and look for 4-in-a-row patterns
    for row in range(6):
        for col in range(7):
            if board[row][col] == opponent:
                if (
                    check_line(board, row, col, 1, 0, opponent) or  # vertical
                    check_line(board, row, col, 0, 1, opponent) or  # horizontal
                    check_line(board, row, col, 1, 1, opponent) or  # diagonal \
                    check_line(board, row, col, 1, -1, opponent)    # diagonal /
                ):
                    return True
    return False

def check_line(board, row, col, d_row, d_col, player):
    """
    [New code] Checks whether there are 4 consecutive pieces for the given player starting at (row, col)
    in the direction specified by (d_row, d_col).
    """
    count = 0
    for i in range(4):
        r = row + i * d_row
        c = col + i * d_col
        if 0 <= r < 6 and 0 <= c < 7 and board[r][c] == player:
            count += 1
        else:
            break
    return count == 4
