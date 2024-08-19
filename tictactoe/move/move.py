from game.game import TicTacToe
import random

from typing import Union, List


class ComputerMove:
    """Class for generating optimal adverserial move"""

    def __init__(self, game: TicTacToe):
        self.game = game
        self.MIN_PLAYER = 0
        self.MAX_PLAYER = 1

    def compare(self, num0: Union[int, None], num1: Union[int, None], comparator) -> Union[int, None]:
        """Function to compare value with None value. 
        Returns the value that result in `True` when `comparator` function is applied
        """
        if num0 == None and num1 != None:
            return num1
        elif num0 != None and num1 == None:
            return num0
        elif num0 != None and num1 != None:
            return num1 if comparator(num0, num1) else num0
        else:
            return None

    def get_min_max_move(self) -> dict:
        """Generate optimal move based on minimax algorithm"""

        cur_state = self.game.copy_2d_arr(arr=self.game.curState)
        bv, b_action = self.min_max(cur_state, player=self.game.curPlayer)

        return b_action

    def min_max(self, state: list[list[int]], player: int) -> tuple[int, Union[dict, None]]:
        """Return the best action using minimax
        """
        # Base case
        if self.game.terminal(state=state):
            return self.game.utility_fn(state=state), None

        v, v_action = None, None
        nv = None
        np = (player + 1) % self.game.playerNum

        for a_row, a_col in self.game.actions(state=state):
            action = {"player": player, "row": a_row, "col": a_col}
            ns = self.game.result(action, state)

            if player == self.MAX_PLAYER:
                nv = self.compare(v, self.min_max(
                    state=ns, player=np)[0], lambda x, y: x < y)
            else:
                nv = self.compare(v, self.min_max(
                    state=ns, player=np)[0], lambda x, y: x > y)
            if v != nv:
                v = nv
                v_action = action

            ns = self.game.undo_move(action=action, state=ns)
        return v, v_action

    def get_alpha_beta(self) -> dict:
        """Generate optimal move based on alpha beta prunning algorithm"""
        cur_state = self.game.copy_2d_arr(arr=self.game.curState)
        bv, b_action = self.alpha_beta(
            state=cur_state, player=self.game.curPlayer)

        return b_action

    def alpha_beta(
        self,
        state: list[list[int]],
        player: int,
        a: Union[int, float] = float('-inf'),
        b: Union[int, float] = float('+inf')
    ) -> tuple[int, Union[dict, None]]:
        """Return the best action using alpha beta prunning"""
        # Base Case
        if self.game.terminal(state=state):
            return self.game.utility_fn(state=state), None

        v, v_action = None, None
        nv = None
        np = (player + 1) % self.game.playerNum

        for a_row, a_col in self.game.actions(state=state):
            action = {"player": player, "row": a_row, "col": a_col}
            ns = self.game.result(action, state)

            if player == self.MAX_PLAYER:
                nv = self.compare(v, self.alpha_beta(
                    state=ns, player=np, a=a, b=b)[0], lambda x, y: x < y)
                a = a if nv == None else max(a, nv)
            else:
                nv = self.compare(v, self.alpha_beta(
                    state=ns, player=np, a=a, b=b)[0], lambda x, y:  x > y)
                b = b if nv == None else min(b, nv)

            ns = self.game.undo_move(action=action, state=ns)
            if v != nv:
                v = nv
                v_action = action
            # Prune Condition: a >= b
            # if not(a == None and b == None) and a >= b:
            if a >= b:
                break
        return v, v_action

    def get_fast_move(self) -> dict:
        """"Return best move based on custom util function"""

        c_state = self.game.copy_2d_arr(self.game.curState)
        score = 0
        action = None
        for a_row, a_col in self.game.actions(c_state):
            actionI = {"player": self.game.curPlayer,
                       "row": a_row, "col": a_col}
            ns = self.game.result(actionI, c_state)
            scoreI = 0
            util_score = self.game.custom_util_fn(ns)

            if self.game.curPlayer == self.MAX_PLAYER:
                scoreI = max(scoreI, util_score)
            else:
                scoreI = min(scoreI, util_score)
            self.game.undo_move(actionI, ns)

            if action == None or score != scoreI:
                score = scoreI
                action = actionI

        return action

    def get_random_move(self) -> dict:
        """Return a valid random move"""
        rand_move = random.choice(self.game.actions(state=self.game.curState))
        return {
            "player": self.game.curPlayer,
            "row": rand_move[0],
            "col": rand_move[1]
        }
