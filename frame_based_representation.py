from board import Board  # import the core game logic class from from board.py

class Frame:
    
    '''The frame class wraps around a board object and tracks additional context, 
    including which player's turn it is. Its's desgined to support our MCTS simulations
    and agent level reasoning. 
    '''
    def __init__(self, board=None, current_player=1):
        '''initialize Frame object. 
        
        Parameters: 
        board- an existing Board object to copy. currently set to none. 
        current_player- the player whose turn it is. (player 1 or 2)
        '''
        self.board = board.copy() if board else Board()#create a copy of the given Board or make a new Board()
        self.current_player = current_player    #tracks wich current player will move next

    def get_legal_moves(self):
        '''
        Returns a list of legal columns where a move can be made
        Delegates to the Board class
        '''
        return self.board.get_legal_moves()

    def apply_move(self, column):
        ''' Apply a move to the board, then switch players.
        Parameters: 
        column- the column index (0-6) where the current player wants to drop a piece
        
    
        Return:
        success- returns true if the move was applied, false if the column is full. 
        '''
        success = self.board.make_move(column, self.current_player)
        if success:#if true, then switch to th eother player.
            self.current_player = 2 if self.current_player == 1 else 1
        return success

    def is_winner(self, player): # Did player x win?
        '''
        check if the specified player has won.
        Delegates to the Board's win-checking logic. 
        
        Parameters:
        player- can be player 1 or 2
        
        
        Returns 
        true if the specified player has 
        '''
        return self.board.check_winner() == player

    def is_terminal(self):# Has the game ended?
        '''
        Check if the game is in a terminal state (win or draw).
        
        Returns:
        -true if the game is over, false otherwise. 
        '''
        return self.board.check_winner() != 0 or self.board.is_draw()

    def copy(self):
        '''
        Returns a deep copy of the Frame object, for use in MCTS simulations.
        Ensures original state is preserved during rollouts. 
        '''
        return Frame(board=self.board, current_player=self.current_player)
    def get_winner(self):
        return self.board.get_winner()

