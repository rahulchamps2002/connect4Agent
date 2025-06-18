# board.py
class Board:
    """
    I hold the Connect-4 grid, let players drop pieces, and detect wins / draws.
    """

    def __init__(self, rows: int = 6, columns: int = 7):
        self.rows = rows
        self.columns = columns
        self.grid = [[0 for _ in range(columns)] for _ in range(rows)]

#CORE GAMES
    def make_move(self, col: int, player: int) -> bool:
        """
        Drop a piece in column `col` for `player`.
        Returns True on success, False if the column is full or invalid.
        """
        if col < 0 or col >= self.columns:
            return False

        for row in range(self.rows - 1, -1, -1):
            if self.grid[row][col] == 0:
                self.grid[row][col] = player
                return True
        return False 

    def get_legal_moves(self) -> list:
        """Columns whose top cell is still empty."""
        return [c for c in range(self.columns) if self.grid[0][c] == 0]

#WINNING detection
    def _check_line(self, row: int, col: int, d_row: int, d_col: int,
                    player: int) -> bool:
        """True if four in a row from (row, col) in (d_row, d_col)."""
        for step in range(1, 4):
            r = row + d_row * step
            c = col + d_col * step
            if r < 0 or r >= self.rows or c < 0 or c >= self.columns:
                return False
            if self.grid[r][c] != player:
                return False
        return True

    def check_winner(self) -> int:
        """
        1 → Player 1 wins, 2 → Player 2 wins, 0 → no winner yet.
        """
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # ↔ ↓ ↘ ↙
        for row in range(self.rows):
            for col in range(self.columns):
                player = self.grid[row][col]
                if player == 0:
                    continue
                for d_row, d_col in directions:
                    if self._check_line(row, col, d_row, d_col, player):
                        return player
        return 0

    # MCTS asked for this convenience wrapper
    def get_winner(self) -> int:
        """Alias so Frame/MCTS can call `frame.get_winner()` directly."""
        return self.check_winner()

    # ─────────────────────────────
    # Draw and copy helpers
    # ─────────────────────────────
    def is_draw(self) -> bool:
        """True when the board is full and nobody has won."""
        return self.check_winner() == 0 and not self.get_legal_moves()

    def copy(self):
        """Deep copy (needed for simulation roll-outs)."""
        clone = Board(self.rows, self.columns)
        clone.grid = [row[:] for row in self.grid]
        return clone

    # ─────────────────────────────
    # Debug print
    # ─────────────────────────────
    def print_board(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))
        print()

    # So `print(board)` shows the grid nicely
    def __str__(self):
        return "\n".join(" ".join(str(cell) for cell in row)
                         for row in self.grid)
    
