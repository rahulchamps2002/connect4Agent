import random
import math
class MCTS:
    """
    Monte Carlo Tree Search agent for Connect 4.
    tracks basic visit and win statistics per move.
    """
    def __init__(self, game_frame, player, max_iterations=1000):
        # [New code] Initialize with a Frame object, player, and simulation count
        self.root_frame = game_frame # instead of: self.game_board = game_board
        self.player = player
        self.max_iterations = max_iterations
        self.tree = {}  # {move_column: {'visits': int, 'wins': int}}
    def run(self):
        # [Modified] loop over multiple simulations and select best move
        for _ in range(self.max_iterations):
            self.simulate()
        if not self.tree:
            # [Added] fallback in case no moves were simulated
            return random.choice(self.root_frame.get_legal_moves())
        # [Modified] Return the move with the highest number of visits
        best_move = max(self.tree.items(), key=lambda item: item[1]['visits'])[0]
        return best_move
    def simulate(self):
        # [New code] Create a new simulation copy of the frame
        frame = self.root_frame.copy()
        simulation_player = self.player
        legal_moves = frame.get_legal_moves()
        if not legal_moves:
            return
        # [New code] Choose and apply a first move
        first_move = random.choice(legal_moves)
        if not frame.apply_move(first_move):
            return
        # [New code] simulate rest of game randomly until terminal state
        while not frame.is_terminal():
            next_moves = frame.get_legal_moves()
            if not next_moves:
                break
            frame.apply_move(random.choice(next_moves))
        winner = frame.get_winner()
        # [New code] Record simulation outcome stats
        if first_move not in self.tree:
            self.tree[first_move] = {'visits': 0, 'wins': 0}
        self.tree[first_move]['visits'] += 1
        if winner == self.player:
            self.tree[first_move]['wins'] += 1
