from board import Board
from frame_based_representation import Frame
from mcts_logic import MCTS

def print_board(board):
    print("\nCurrent board:")
    board.print_board()

def main():
    board = Board()
    frame = Frame(board=board, current_player=1)

    print("You are Player 1. Agent is Player 2.\n")

    while not frame.is_terminal():
        print_board(frame.board)

        # Your move
        legal = frame.get_legal_moves()
        print("Legal moves:", legal)
        move = int(input("Your move (0–6): "))
        while move not in legal:
            move = int(input("Invalid. Try again: "))
        frame.apply_move(move)

        if frame.is_terminal():
            break

        # Agent move
        print("\nAgent is thinking...\n")
        mcts = MCTS(frame.copy(), player=2)
        agent_move = mcts.run()
        frame.apply_move(agent_move)
        print(f"Agent plays in column {agent_move}")

    print_board(frame.board)
    winner = frame.get_winner()
    if winner == 1:
        print("🎉 You win!")
    elif winner == 2:
        print("🤖 Agent wins!")
    else:
        print("It's a draw.")

if __name__ == "__main__":
    main()
