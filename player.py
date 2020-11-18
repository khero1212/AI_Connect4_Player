#Author: Karthik Thatipalli

import random
import copy
from decimal import Decimal


class TeekoPlayer:
    """ An object representation for an AI game player for the game Teeko.
    """
    board = [[' ' for j in range(5)] for i in range(5)]
    pieces = ['b', 'r']

    def __init__(self):
        """ Initializes a TeekoPlayer object by randomly selecting red or black as its
        piece color.
        """
        self.my_piece = random.choice(self.pieces)
        self.opp = self.pieces[0] if self.my_piece == self.pieces[1] else self.pieces[1]
    
    def succ(self, state, player_piece):
        piece_count = 0
        succ_list = []
        
        for x in range(5):
            for y in range(5):
                if state[x][y] in self.pieces:
                    piece_count += 1
        #drop phase
        if piece_count < 8:
            for x in range(5):
                for y in range(5):
                    if state[x][y] == ' ':
                        temp_state = copy.deepcopy(state)
                        temp_state[x][y] = self.my_piece
                        succ_list.append(temp_state)
        else:
            for i in range(5):
                for j in range(5):
                    if state[i][j] != self.my_piece:
                        pass
                    else:
                        if i - 1 >= 0 and j - 1 >= 0 and state[i - 1][j - 1] == ' ':
                            temp_state = copy.deepcopy(state)
                            temp_state[i][j] = ' '
                            temp_state[i - 1][j - 1] = self.my_piece
                            succ_list.append(temp_state)
                        if i - 1 >= 0 and j + 1 <= 4 and state[i - 1][j + 1] == ' ':
                            temp_state = copy.deepcopy(state)
                            temp_state[i][j] = ' '
                            temp_state[i - 1][j + 1] = self.my_piece
                            succ_list.append(temp_state)
                        if i + 1 <= 4 and j - 1 >= 0 and state[i + 1][j - 1] == ' ':
                            temp_state = copy.deepcopy(state)
                            temp_state[i][j] = ' '
                            temp_state[i + 1][j - 1] = self.my_piece
                            succ_list.append(temp_state)
                        if i + 1 <= 4 and state[i + 1][j] == ' ':
                            temp_state = copy.deepcopy(state)
                            temp_state[i][j] = ' '
                            temp_state[i + 1][j] = self.my_piece
                            succ_list.append(temp_state)
                        if i + 1 <= 4 and j + 1 <= 4 and state[i + 1][j + 1] == ' ':
                            temp_state = copy.deepcopy(state)
                            temp_state[i][j] = ' '
                            temp_state[i + 1][j + 1] = self.my_piece
                            succ_list.append(temp_state)
                        if j - 1 >= 0 and state[i][j - 1] == ' ':
                            temp_state = copy.deepcopy(state)
                            temp_state[i][j] = ' '
                            temp_state[i][j - 1] = self.my_piece
                            succ_list.append(temp_state)
                        if j + 1 <= 4 and state[i][j + 1] == ' ':
                            temp_state = copy.deepcopy(state)
                            temp_state[i][j] = ' '
                            temp_state[i][j + 1] = self.my_piece
                            succ_list.append(temp_state)
                        if i - 1 >= 0 and state[i - 1][j] == ' ':
                            temp_state = copy.deepcopy(state)
                            temp_state[i][j] = ' '
                            temp_state[i - 1][j] = self.my_piece
                            succ_list.append(temp_state)
                                        
        return succ_list
    
    def heuristic_game_value(self, state):
        if self.game_value(state) != 0:
            return self.game_value(state)

        # to check for horizontal
        max_val = 0
        min_val = 0

        for row in state:
            self_val = 0
            opp_val = 0
            for i in range(4):
                if row[i] == self.my_piece and row[i + 1] != self.opp:
                    self_val += 20
                    opp_val = 0
                elif row[i] == self.opp and row[i + 1] != self.my_piece:
                    opp_val -= 20
                    self_val = 0
            if self_val <= max_val:
                pass
            else:
                max_val = self_val
            if opp_val >= min_val:
                pass
            else:
                min_val = opp_val

        for col in range(5):
            self_val = 0
            opp_val = 0
            for i in range(4):
                if state[i][col] == self.my_piece and state[i + 1][col] != self.opp:
                    self_val += 20
                    opp_val = 0
                if state[i][col] == self.opp and state[i + 1][col] != self.my_piece:
                    opp_val -= 20
                    self_val = 0
            if self_val <= max_val:
                pass
            else:
                max_val = self_val
            if opp_val >= min_val:
                pass
            else:
                min_val = opp_val

        for i in range(2):
            for j in range(2):
                self_val = 0
                opp_val = 0
                for a in range(3):
                    if state[i + a][j + a] == self.my_piece and state[i + a + 1][j + a + 1] != self.opp:
                        self_val += 20
                        opp_val = 0
                    if state[i + a][j + a] == self.opp and state[i + a + 1][j + a + 1] != self.my_piece:
                        opp_val -= 20
                        self_val= 0
        
                if self_val <= max_val:
                    pass
                else:
                    max_val = self_val
                if opp_val >= min_val:
                    pass
                else:
                    min_val = opp_val

        for i in range(3, 5):
            for j in range(2):
                self_val = 0
                opp_val = 0
                for a in range(3):
                    if state[i - a][j + a] == self.my_piece and state[i - (a + 1)][j + a + 1] != self.opp:
                        self_val += 20
                        opp_val = 0
                    if state[i - a][j + a] == self.opp and state[i - (a + 1)][j + a + 1] != self.my_piece:
                        opp_val -= 20
                        self_val = 0

                if self_val <= max_val:
                    pass
                else:
                    max_val = self_val
                if opp_val >= min_val:
                    pass
                else:
                    min_val = opp_val
        
        if max_val <= abs(min_val):
            pass
        else:
            return max_val/1000
        
        if max == abs(min_val):
            return min_val/1000
        else:
            if random.randint(0,1) == 0:
                return min_val
            return max_val/1000
        
    def Max_Value(self, state, depth):
        if self.game_value(state) != 1:
            pass
        else:
            return self.game_value(state), state
        if depth + 1 < 4:
            pass
        else:
            return self.heuristic_game_value(state), state
        
        alpha, child = Decimal('-Infinity'), state
        succ_num = 0
        for successor in self.succ(state, self.my_piece):
            succ_num += 1
            prev = alpha
            alpha = max(alpha, self.Min_Value(successor, depth + 1)[0])
            if alpha <= prev:
                pass
            else:
                child = successor
        return alpha, child

    def Min_Value(self, state, depth):
        if self.game_value(state) != -1:
            pass
        else:
            return self.game_value(state), state
        if depth + 1 < 4:
            pass
        else:
            return self.heuristic_game_value(state), state
        
        beta, child = Decimal('Infinity'), state
        succ_num = 0
        for successor in self.succ(state, self.opp):
            succ_num += 1
            prev = beta
            beta = min(beta, self.Max_Value(successor, depth + 1)[0])
            if beta >= prev:
                pass
            else:
                child = successor
        return beta, child
    
    def make_move(self, state):
        """ Selects a (row, col) space for the next move. You may assume that whenever
        this function is called, it is this player's turn to move.
            
        Args:
            state (list of lists): should be the current state of the game as saved in
                this TeekoPlayer object. Note that this is NOT assumed to be a copy of
                the game state and should NOT be modified within this method (use
                place_piece() instead). Any modifications (e.g. to generate successors)
                should be done on a deep copy of the state.
                
                In the "drop phase", the state will contain less than 8 elements which
                are not ' ' (a single space character).
        
        Return:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.

        Note that without drop phase behavior, the AI will just keep placing new markers
            and will eventually take over the board. This is not a valid strategy and
            will earn you no points.
        """
        
        drop_phase = True  
        piece_count = 0
        
        for x in range(5):
            for y in range(5):
                if state[x][y] in self.pieces:
                    piece_count += 1
    
        if piece_count >= 8:
            drop_phase = False

        move = []
        if drop_phase:
            # choose a piece to move and remove it from the board
            # Until this part is implemented and the move list is updated
            max_val, next_state = self.Max_Value(state, 0)
            for i in range(5):
                for j in range(5):  
                    if state[i][j] == ' ' and next_state[i][j] == self.my_piece:
                        move.insert(0, (i, j))
            return move
        
        max_val, next_state = self.Max_Value(state, 0)
        for i in range(5):
            for j in range(5):
                if state[i][j] == ' ' and next_state[i][j] == self.my_piece:
                    move.insert(0, (i, j))
                if state[i][j] == self.my_piece and next_state[i][j] == ' ':
                    move.insert(1, (i, j))
        return move
        
    def opponent_move(self, move):
        """ Validates the opponent's next move against the internal board representation.
        You don't need to touch this code.

        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.
        """
        # validate input
        if len(move) > 1:
            source_row = move[1][0]
            source_col = move[1][1]
            if source_row != None and self.board[source_row][source_col] != self.opp:
                raise Exception("You don't have a piece there!")
        if self.board[move[0][0]][move[0][1]] != ' ':
            raise Exception("Illegal move detected")
        # make move
        self.place_piece(move, self.opp)
        
    def place_piece(self, move, piece):
        """ Modifies the board representation using the specified move and piece
        
        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.
                
                This argument is assumed to have been validated before this method
                is called.
            piece (str): the piece ('b' or 'r') to place on the board
        """
        if len(move) > 1:
            self.board[move[1][0]][move[1][1]] = ' '
        self.board[move[0][0]][move[0][1]] = piece
        
    def print_board(self):
        """ Formatted printing for the board """
        for row in range(len(self.board)):
            line = str(row)+": "
            for cell in self.board[row]:
                line += cell + " "
            print(line)
        print("   A B C D E")
        
    def game_value(self, state):
        """ Checks the current board status for a win condition
        
        Args:
        state (list of lists): either the current state of the game as saved in
            this TeekoPlayer object, or a generated successor state.

        Returns:
            int: 1 if this TeekoPlayer wins, -1 if the opponent wins, 0 if no winner
        """
        # check horizontal wins
        for row in state:
            for i in range(2):
                if row[i] != ' ' and row[i] == row[i+1] == row[i+2] == row[i+3]:
                    return 1 if row[i]==self.my_piece else -1

        # check vertical wins
        for col in range(5):
            for i in range(2):
                if state[i][col] != ' ' and state[i][col] == state[i+1][col] == state[i+2][col] == state[i+3][col]:
                    return 1 if state[i][col]==self.my_piece else -1

        
        for i in range(2):
            if state[i][i] != ' ' and state[i][i] == state[i+1][i+1] == state[i+2][i+2] == state[i+3][i+3]:
                return 1 if state[i][i] == self.my_piece else -1
        if state[1][0] != ' ' and state[1][0] == state[2][1] == state[3][2] == state[4][3]:
            return 1 if state[1][0] == self.my_piece else -1
        if state[0][1] != ' ' and state[0][1] == state[1][2] == state[2][3] == state[3][4]:
            return 1 if state[0][1] == self.my_piece else -1
                        
        
        for i in range(2):
            if state[i][4-i] != ' ' and state[i][4-i] == state[i+1][4-i-1] == state[i+2][4-i-2] == state[i+3][4-i-3]:
                return 1 if state[i][4-i] == self.my_piece else -1
        if state[1][4] != ' ' and state[1][4] == state[2][3] == state[3][2] == state[4][1]:
            return 1 if state[1][4] == self.my_piece else -1
        if state[0][3] != ' ' and state[0][3] == state[1][2] == state[2][1] == state[3][0]:
            return 1 if state[0][3] == self.my_piece else -1
        
        for i in range(4):
            for j in range(4):
                if state[i][i]!=' ' and state[i][i]==state[i+1][i]==state[i][i+1]==state[i+1][i+1]:
                    return 1 if state[i][i] == self.my_piece else -1
        
        
        return 0 # no winner yet
      
    