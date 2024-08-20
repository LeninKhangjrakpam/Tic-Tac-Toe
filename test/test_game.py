from game.game import TicTacToe
from move.move import ComputerMove


def equal2dList(ar1, ar2):
    if len(ar1) != len(ar2):
        return False
    for i in range(len(ar1)):
        if ar1[i] != ar2[i]:
            return False
    return True


class TestGame:

    def test_one(self):
        g = TicTacToe()

        assert g.curPlayer == 0

    def test_two(self):
        state = [
            [None, 0, None],
            [0, 1, 1],
            [1, 0, 1]
        ]
        g = TicTacToe()

        moves = g.actions(state=state)
        assert equal2dList(moves, [(0, 0), (0, 2)])

    def test_result(self):
        g = TicTacToe()
        state = [
            [None, 0, None],
            [0, 1, 1],
            [1, 0, 1]
        ]

        res = g.result(action={"row": 0, "col": 2, "player": 1}, state=state)
        state[0][2] = 1
        assert equal2dList(res, state)

    def test_check_action1(self):
        g = TicTacToe()
        state = [
            [None, 0, None],
            [0, 1, 1],
            [1, 0, 1]
        ]

        res = g.check_action(
            action={"row": 2, "col": 2, "player": 1}, state=state)
        assert res == False

    def test_check_action2(self):
        g = TicTacToe()
        state = [
            [None, 0, None],
            [0, 1, 1],
            [1, 0, 1]
        ]

        res = g.check_action(
            action={"row": 0, "col": 2, "player": 1}, state=state)
        assert res
