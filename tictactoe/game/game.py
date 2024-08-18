class TicTacToe:
    """Class for implementing Tictactoe game"""

    def __init__(self, initPlayer=0, initState: None | list[list[int | None]] = None) -> None:
        """Iniitialise Game with the given init player, state

        Args:
            initPlayer (_int_): initial player, should be 0 or 1
            initState (_list[list[int]] | None_): intial state of the board to start from,\
            pass _None_ if want to start from empty 3x3 board
        """
        self.initState = initState
        self.initPlayer = initPlayer
        if initState == None:
            self.boardRow = 3
            self.boardCol = 3
            self.curState: list[list[int | None]] = [
                [None for _ in range(self.boardCol)] for _ in range(self.boardRow)
            ]
        else:
            self.boardRow = len(initState)
            self.boardCol = len(initState[0])
            self.curState: list[list[int | None]] = initState
        self.playerNum = 2
        self.curPlayer = initPlayer
        self.histories = [list(self.curState)]

    def check_action(self, action: dict, state: None | list[list[int]] = None) -> bool:
        """Check wether _action_ is valid or not  
        if `state` arg is not `None`, then `check_action` 
        will not check player turn validity

        Args:
            action (_dict | None_): {row, col, player}, action to be check
            state (_None | list[list[int]]_):

        Returns:
            bool: True if valid, False if invalid
        """
        stateNone = False
        if state == None:
            stateNone = True
            state = self.curState

        row, col, player = action["row"], action["col"], action["player"]

        if not (0 <= row < self.boardRow):
            print("invalid row")
            return False
        if not (0 <= col < self.boardCol):
            print("invalid Col")
            return False
        # if not (0 <= player < self.playerNum):
        #     print("invalid player")
        #     return False

        if stateNone and not player == self.curPlayer:
            print("invalid Current player", self.curPlayer, player)
            return False

        if state[row][col] != None:
            print("invalid move, cell already filled")
            return False

        return True

    def result(self, action: dict, state: None | list[list[int]]) -> list[list[int]]:
        """Return the board state result after applying action to state  
        This function only return the new board state, and doesnot update the game state  
        To update game state with the action, use `TicTacToe.move()`
        """
        if state == None:
            state = self.curState

        if not self.check_action(action=action, state=state):
            raise Exception("invalid action")

        row, col, player = action["row"], action["col"], action["player"]
        new_state = self.copy_2d_arr(state)
        new_state[row][col] = player
        return new_state

    def actions(self, state: None | list[list[int]]) -> list[tuple[int, int]]:
        """Returns a list of valid actions that can be performed on the current board"""
        if state == None:
            state = self.curState

        avail_actions = []
        for rIndx, row in enumerate(state):
            for cIndx, elm in enumerate(row):
                if elm == None:
                    avail_actions.append((rIndx, cIndx))
        return avail_actions

    def move(self, action: dict, state: None | list[list[int]] = None) -> bool:
        """Perform action move to state  
        This function will update the game state with given action
        Returns:
            bool: False if action is invalid, True if move is sucessful
        """
        if state == None:
            state = self.curState
        # Check action validity
        if not self.check_action(action, state=state):
            return False

        # Update Game State
        row, col, player = action["row"], action["col"], action["player"]
        self.curState[row][col] = player
        self.curPlayer = (self.curPlayer + 1) % self.playerNum
        self.histories.append(self.copy_2d_arr(self.curState))
        return True

    def undo_move(self, action: dict, state: None | list[list[int]] = None) -> tuple[bool, list[list[int]]]:
        """This function will undo the given action to the state  
        If `state` is passes as None, then this function will update the game state and also return the current state   
        if `state` passed then this function will not update the game state, instead will just return the modified game state  

        Args:

        Returns:
            (_tuple[bool, list[list[int]]]_):
                if action is `invalid`: `[False, None]`  
                if action is `valid`: `[True, modified_state]`
        """
        state_update_flag = False
        if state == None:
            state = self.curPlayer
            state_update_flag = True

        row, col, player = action["row"], action["col"], action["player"]
        if not (0 <= row < len(state) and 0 <= col < len(state[0])):
            return False, None
        if 0 <= player < self.playerNum:
            return False, None
        if player == self.curPlayer:
            return False, None
        if state[row][col] != player:
            return False, None

        new_state = self.copy_2d_arr(state)
        new_state[row][col] = None
        if state_update_flag:
            self.curPlayer = (self.curPlayer + 1) % self.playerNum
            self.curState = new_state
            self.histories.pop()
            return True, new_state
        else:
            return True, new_state

    def winner(self, state: None | list[list[int]] = None) -> tuple[int, int, list[tuple[int, int]]]:
        """Return the winner player  

        Returns:
            (_tuple[int, int, list[tuple[int, int]]]_):     
                If `Winner`: `[0, player symbol, win strip]`  
                If `No Winner`: `[-1, None, None]`  
                if `Draw`: `[0, None, None]`
        """

        if state == None:
            state = self.curState

        # Check Row
        res, sym, win_strip = self.check_row(state=state)
        if res:
            return 1, sym, win_strip
        # Check Col
        res, sym, win_strip = self.check_col(state=state)
        if res:
            return 1, sym, win_strip
        # Check Diagonal
        res, sym, win_strip = self.check_diagonal(state=state)
        if res:
            return 1, sym, win_strip

        # Check Draw
        """Since, no winner is detected, check for draw"""
        if self.isDraw(state=state):
            return 0, None, None

        """No winner and draw is detected"""
        return -1, None, None

    def terminal(self, state: list[list[int]] | None = None) -> bool:
        """Check wether a state is terminal or not
        A state can be terminal if no move can be made (i.e. all cells are filled)
        or a winner is detected
        """
        if state == None:
            state = self.curState

        win, _, _ = self.winner(state=state)
        if win == 0 or win == 1:
            # If draw or winner exist on current state
            return True
        else:
            return False

    def copy_2d_arr(self, arr: list[list[int | None]]) -> list[list[int | None]]:
        """Return a copy of arr"""
        return [
            list(ar) for ar in arr
        ]

    def copy_state(self, src):
        """Copy game state from `src`
        Args:
            src (_TicTaCToe_): another TicTacToe class to copy game state from
        """
        self.playerNum = src.playerNum
        self.curState = src.curState
        self.boardCol = src.boardCol
        self.boardRow = src.boardRow
        self.curPlayer = src.curPlayer
        self.histories = [
            self.copy_2d_arr(state) for state in src.histories
        ]

    def check_row(self, state=None) -> tuple[bool, int, list[tuple[int, int]]]:
        """Check winner is detected on each row of board"""
        if state == None:
            state = self.curState

        for i in range(len(state)):
            mark = state[i][0]
            for j in range(len(state[i])):
                if state[i][j] == None:
                    # Empty cell
                    break
                elif state[i][j] != mark:
                    # If cell is mark differently
                    break
                if j == len(state[i]) - 1:
                    return True, mark, [(i, 0), (i, j)]
        return False, None, None

    def check_col(self, state=None) -> tuple[bool, int, list[tuple[int, int]]]:
        """Check Winner is detcted on each col of board"""
        if state == None:
            state = self.curState

        for i in range(len(state[0])):
            mark = state[0][i]
            for j in range(len(state)):
                if state[j][i] == None:
                    # Empty Cell
                    break
                elif state[j][i] != mark:
                    break
                if j == len(state) - 1:
                    return True, mark, [(0, i), (j, i)]
        return False, None, None

    def check_diagonal(self, state=None) -> tuple[bool, int, list[tuple[int, int]]]:
        """Check winner is detected on primary and secondary diagonal of the board"""
        if state == None:
            state = self.curState

        # Primary Diagonal
        mark = state[0][0]
        for i in range(len(state)):
            if state[i][i] == None:
                # Empty Cell
                break
            elif state[i][i] != mark:
                break
            if i == len(state) - 1:
                return True, mark, [(0, 0), (len(state) - 1, len(state[i]) - 1)]

        # Secondary Diagonal
        mark = state[0][len(state[0]) - 1]
        for i in range(len(state)):
            if state[i][len(state[i]) - 1 - i] == None:
                break
            elif state[i][len(state[i]) - 1 - i] != mark:
                break
            if i == len(state) - 1:
                return True, mark, [(0, len(state[0]) - 1), (i, 0)]
        return False, None, None

    def isDraw(self, state: list[list[int]] | None = None) -> bool:
        """Check wether a state is draw
        It checks only wether all the board cells are completely filled
        """
        if state == None:
            state = self.curState

        for row in state:
            for elm in row:
                if elm == None:
                    return False
        return True

    def reset(self):
        """Rest the current state of the game to the initial state  
        Call this when we want to restart the game from begining
        """
        self.curPlayer = self.initPlayer
        self.curState = self.initState

        if self.curState == None:
            self.curState: list[list[int | None]] = [
                [None for _ in range(self.boardCol)] for _ in range(self.boardRow)
            ]
        self.histories = [self.copy_2d_arr(self.curState)]

    def custom_util_fn(self, state=None) -> int:
        """Return the utility function of a state  
        Calculate util score before reaching the terminal state        
        """
        if state == None:
            state = self.curState

        p0_score, p1_score = 0, 0
        # Check row
        for row in state:
            p0, p1 = 0, 0
            for elm in row:
                if elm == 0:
                    p0 += 1
                elif elm == 1:
                    p1 += 1
            p0_score = max(p0, p1_score)
            p1_score = max(p1, p1_score)

        # Check col
        for i in range(len(state[0])):
            p0, p1 = 0, 0
            for j in range(len(state)):
                if state[j][i] == 0:
                    p0 += 1
                elif state[j][i] == 1:
                    p1 += 1
            p0_score = max(p0, p0_score)
            p1_score = max(p1, p1_score)

        # Check primary diagonal
        p0, p1 = 0, 0
        for i in range(len(state)):
            if state[i][i] == 0:
                p0 += 1
            elif state[i][i] == 1:
                p1 += 1
        p0_score = max(p0_score, p0)
        p1_score = max(p1_score, p1)

        # Check secondary diagonal
        p0, p1 = 0, 0
        for i in range(len(state)):
            if state[i][len(state) - 1 - i] == 0:
                p0 += 1
            elif state[i][len(state) - 1 - i] == 1:
                p1 += 1
        p0_score = max(p0_score, p0)
        p1_score = max(p1_score, p1)

        if p0_score == p1_score:
            return 0
        else:
            return p0_score if p0_score > p1_score else -1 * p1_score

    def utility_fn(self, state=None) -> int:
        """Return the utility score of a state
        player0 is MinPlayer  
        player1 is MaxPlayer  

        Returns:
            int: `0` if draw, `-1` if player0 win, `1` if player1 win
        """
        if state == None:
            state = self.curState

        if not self.terminal(state=state):
            # If the current state is not a terminal state
            return None

        win_res, win_player, _ = self.winner(state=state)
        if win_res == 0:
            return 0
        elif win_res == 1:
            return 1 if win_player == 1 else -1

    def print_board(self, state: None | list[list[int]] = None):
        """Print the board state on terminal"""
        if state == None:
            state = self.curState

        for row in state:
            for elm in row:
                if elm == None:
                    print("_", end=" ")
                else:
                    print(f"{'O' if elm == 0 else 'X'}", end=" ")
            print()
