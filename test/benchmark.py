
import time
from game.game import TicTacToe
from move.move import ComputerMove


class TestBenchmarkGame(object):
    @staticmethod
    def test_cc():
        """Simulate game using 2 agents that used alpha beta policy"""
        game = TicTacToe()
        player1 = ComputerMove(game)
        player2 = ComputerMove(game)

        game.print_board()
        print("Terminal: ", game.terminal(), game.winner())
        while not game.terminal():
            # Get computer move
            print(f"Player - {game.curPlayer} turn")
            # ai_move1 = player1.get_min_max_move()
            ai_move1 = player1.get_alpha_beta()
            print("P1: ", ai_move1)
            print(
                f"player{ai_move1['player']} move: row: {ai_move1['row']}, col: {ai_move1['col']}")
            # Update Game State
            game.move(ai_move1)
            game.print_board()

            # Check winner
            if game.terminal():
                break

            # Get computer move
            print(f"Player - {game.curPlayer} turn")
            # ai_move2 = player2.get_min_max_move()
            ai_move2 = player2.get_alpha_beta()
            print(
                f"player{ai_move2['player']} move: row: {ai_move2['row']}, col: {ai_move2['col']}")
            # Update Game State
            game.move(ai_move2)
            game.print_board()

            # Check winner
            if game.terminal():
                break

        win_res, win_player, win_strip = game.winner()
        if win_res == 0:
            print("Draw")
        elif win_res == 1:
            print(f"Winner: {win_player}, winStrip: {win_strip}")

    @staticmethod
    def test_aa():
        """Simulate game using 2 agents that used alpha beta policy"""
        game = TicTacToe()
        player = ComputerMove(game)

        game.print_board()
        print("Terminal: ", game.terminal(), game.winner())
        while not game.terminal():
            # Get computer move
            print(f"Player - {game.curPlayer} turn")
            # ai_move1 = player1.get_min_max_move()
            ai_move1 = player.get_alpha_beta()
            print("P1: ", ai_move1)
            print(
                f"player{ai_move1['player']} move: row: {ai_move1['row']}, col: {ai_move1['col']}")
            # Update Game State
            game.move(ai_move1)
            game.print_board()

            # Check winner
            if game.terminal():
                break

            # Get computer move
            print(f"Player - {game.curPlayer} turn")
            # ai_move2 = player2.get_min_max_move()
            ai_move2 = player.get_alpha_beta()
            print(
                f"player{ai_move2['player']} move: row: {ai_move2['row']}, col: {ai_move2['col']}")
            # Update Game State
            game.move(ai_move2)
            game.print_board()

            # Check winner
            if game.terminal():
                break

        win_res, win_player, win_strip = game.winner()
        if win_res == 0:
            print("Draw")
        elif win_res == 1:
            print(f"Winner: {win_player}, winStrip: {win_strip}")

    @staticmethod
    def test_ar():
        """Simulate game using 2 agents that used alpha beta and random policy"""
        game = TicTacToe()
        player = ComputerMove(game)

        game.print_board()
        while not game.terminal():
            # Get computer move
            print(f"Player - {game.curPlayer} turn")
            # ai_move1 = player1.get_min_max_move()
            ai_move1 = player.get_alpha_beta()
            print("P1: ", ai_move1)
            print(
                f"player{ai_move1['player']} move: row: {ai_move1['row']}, col: {ai_move1['col']}")
            # Update Game State
            game.move(ai_move1)
            game.print_board()

            # Check winner
            if game.terminal():
                break

            # Get computer move
            print(f"Player - {game.curPlayer} turn")
            # ai_move2 = player2.get_min_max_move()
            ai_move2 = player.get_random_move()
            print(
                f"player{ai_move2['player']} move: row: {ai_move2['row']}, col: {ai_move2['col']}")
            # Update Game State
            game.move(ai_move2)
            game.print_board()

            # Check winner
            if game.terminal():
                break

        win_res, win_player, win_strip = game.winner()
        if win_res == 0:
            print("Draw")
        elif win_res == 1:
            print(f"Winner: {win_player}, winStrip: {win_strip}")

    @staticmethod
    def test_mm():
        """Simulate game using 2 agents that used minimax policy"""
        game = TicTacToe()
        player = ComputerMove(game)

        game.print_board()
        print("Terminal: ", game.terminal(), game.winner())
        while not game.terminal():
            # Get computer move
            print(f"Player - {game.curPlayer} turn")
            ai_move1 = player.get_min_max_move()
            print("P1: ", ai_move1)
            print(
                f"player{ai_move1['player']} move: row: {ai_move1['row']}, col: {ai_move1['col']}")
            # Update Game State
            game.move(ai_move1)
            game.print_board()

            # Check winner
            if game.terminal():
                break

            # Get computer move
            print(f"Player - {game.curPlayer} turn")
            # ai_move2 = player2.get_min_max_move()
            ai_move2 = player.get_min_max_move()
            print(
                f"player{ai_move2['player']} move: row: {ai_move2['row']}, col: {ai_move2['col']}")
            # Update Game State
            game.move(ai_move2)
            game.print_board()

            # Check winner
            if game.terminal():
                break

        win_res, win_player, win_strip = game.winner()
        if win_res == 0:
            print("Draw")
        elif win_res == 1:
            print(f"Winner: {win_player}, winStrip: {win_strip}")


def benchmark(fn, *args, **kwargs):
    start_time = time.time()
    fn(*args, **kwargs)
    end_time = time.time()
    elapse = end_time - start_time
    print(f"{fn.__name__}: elapsed time: {elapse:.6f}")


if __name__ == "__main__":
    print("AB vs AB")

    benchmark(TestBenchmarkGame.test_aa)
    print("AB vs AB")
    print()

    print("AB vs random")
    benchmark(TestBenchmarkGame.test_ar)
    print("AB vs random")
    print()

    print("minimax vs minimax")
    benchmark(TestBenchmarkGame.test_mm)
    print("minimax vs minimax")
    print()
