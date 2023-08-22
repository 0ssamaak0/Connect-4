import sys
import qdarktheme
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QLabel, QSpinBox, QMessageBox, QComboBox
from PyQt6.QtGui import QIcon, QPixmap, QPainter, QBrush, QPen
from PyQt6.QtCore import Qt
import random, time

import random, time, math, copy

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Human(Player):
    def __init__(self, name, color):
        super().__init__(name, color)

class RandomComputer(Player):
    def __init__(self, name, color):
        super().__init__(name, color)

    def play(self, game):
        board = game.board
        available_cols = [col for col in range(len(board[0])) if board[0][col] == 0]
        if available_cols:
            return random.choice(available_cols)
        else:
            return None
def get_valid_locations(self, board):
        """
        Gets all valid moves.

        Args:
        - board (list): The board state as a 2D list of integers.

        Returns:
        - list: A list of valid moves.
        """
        valid_locations = []
        for col in range(len(board[0])):
            if self.is_valid(board, col):
                valid_locations.append(col)
        return valid_locations

def is_valid(self, board, col):
        """
        Checks if a move is valid.

        Args:
        - board (list): The board state as a 2D list of integers.
        - col (int): The column in which to place the current player's piece.

        Returns:
        - bool: True if the move is valid, False otherwise.
        """
        return board[0][col] == 0
    
def is_terminal_node(self, board):
        """
        Checks if the game has ended.

        Args:
        - board (list): The board state as a 2D list of integers.

        Returns:
        - bool: True if the game has ended, False otherwise.
        """
        return self.check_win(board, self.name) or self.check_win(board, self.opp_name) or len(self.get_valid_locations(board)) == 0
def get_next_open_row(self, board, col):
        """
        Gets the next open row in a given column.

        Args:
        - board (list): The board state as a 2D list of integers.
        - col (int): The column in which to place the current player's piece.

        Returns:
        - int: The row in which to place the current player's piece.
        """
        for r in range(self.num_rows):
            if board[r][col] == 0:
                return r
def drop_piece(self, board, row, col, piece):
        """
        Drops a piece in a given position.

        Args:
        - board (list): The board state as a 2D list of integers.
        - row (int): The row in which to place the current player's piece.
        - col (int): The column in which to place the current player's piece.
        - piece (int): The current player's piece.

        Returns:
        - None
        """
        board[row][col] = piece

class MiniMaxComputer(Player):
    def __init__(self, name, color, depth=10):
        super().__init__(name, color)
        self.depth = depth
        self.opp_name = 2 if self.name == 1 else 1

    def play(self, game,board):

        best_score = -math.inf
        valid_locations = get_valid_locations(board)
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, self.name)
            score = self.minimax(b_copy, self.depth, -math.inf, math.inf, False, game)
            if score > best_score:
                best_score = score
                best_col = col
        return best_col
    
    
   
    
    def minimax(self, board, depth, alpha, beta, is_maximizing, game, row, col):
        """
        Evaluates a board state using the minimax algorithm with a given depth and alpha-beta pruning.

        Args:
        - board (list): The board state as a 2D list of integers.
        - depth (int): The depth of the search tree.
        - alpha (float): The best score for the maximizing player.
        - beta (float): The best score for the minimizing player.
        - is_maximizing (bool): True if the current player is maximizing, False otherwise.

        Returns:
        - float: The score of the board state.
        
        # check if the game is over or the depth is zero
        print(f"depth = {depth}")
        if game.check_win(row, col) or game.check_tie() or depth == 0:
            # return a heuristic score based on the board state
            return self.evaluate(board, game)
        
        # check if the current player is maximizing
        if is_maximizing:
            # set the initial best score to negative infinity
            best_score = -math.inf
            # loop through all possible moves
            for col in range(game.num_cols):
                # check if the move is valid
                if board[0][col] == 0:
                    # make a copy of the board
                    board_copy = copy.deepcopy(board)
                    # simulate the move on the board copy
                    row = game.num_rows - 1
                    while row >= 0 and board_copy[row][col] != 0:
                        row -= 1
                    board_copy[row][col] = self.name
                    # recursively evaluate the move using the minimax function with a reduced depth and alpha-beta pruning
                    score = self.minimax(board_copy, depth-1, alpha, beta, False, game, row, col)
                    # update the best score and alpha if the score is higher than the current best score
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    # break out of the loop if alpha is greater than or equal to beta (pruning)
                    if alpha >= beta:
                        break
            # return the best score
            print(f"best_score = {best_score}")
            return best_score
        
        else: # if the current player is minimizing
            # set the initial best score to positive infinity
            best_score = math.inf
            # loop through all possible moves
            for col in range(game.num_cols):
                # check if the move is valid
                if board[0][col] == 0:
                    # make a copy of the board
                    board_copy = copy.deepcopy(board)
                    # simulate the move on the board copy
                    row = game.num_rows - 1
                    while row >= 0 and board_copy[row][col] != 0:
                        row -= 1
                    board_copy[row][col] = self.opp_name
                    # recursively evaluate the move using the minimax function with a reduced depth and alpha-beta pruning
                    score = self.minimax(board_copy, depth-1, alpha, beta, True, game, row, col)
                    # update the best score and beta if the score is lower than the current best score
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    # break out of the loop if alpha is greater than or equal to beta (pruning)
                    if alpha >= beta:
                        break
            # return the best score
            print(f"best_score = {best_score}")
            return best_score
            """
        valid_locations=get_valid_locations(board)
        is_terminal_node=is_terminal_node(board)
        if depth==0 or is_terminal_node:
            if is_terminal_node:
                if self.check_win(board, self.name):
                    return (None,100000000000000)
                elif self.check_win(board, self.opp_name):
                    return (None,-10000000000000)
                else:
                    return (None,0)
            else:
                return (None,self.evaluate(board,game))
        if is_maximizing:
            value=-math.inf
            column=random.choice(valid_locations)
            for col in valid_locations:
                row=get_next_open_row(board,col)
                b_copy=board.copy()
                drop_piece(b_copy,row,col,self.name)
                new_score=self.minimax(b_copy,depth-1,alpha,beta,False,game)
                if new_score>value:
                    value=new_score
                    column=col
                alpha=max(alpha,value)
                if alpha>=beta:
                    break
            return column,value
        else:#minimizing player
            value=math.inf
            column=random.choice(valid_locations)
            for col in valid_locations:
                row=get_next_open_row(board,col)
                b_copy=board.copy()
                drop_piece(b_copy,row,col,self.opp_name)
                new_score=self.minimax(b_copy,depth-1,alpha,beta,True,game)
                if new_score<value:
                    value=new_score
                    column=col
                beta=min(beta,value)
                if alpha>=beta:
                    break
            return column,value

    def evaluate(self, board, game):
        """
        Evaluates a board state using a heuristic function.

        Args:
        - board (list): The board state as a 2D list of integers.

        Returns:
        - float: The heuristic score of the board state.
        
        # set the initial score to zero
        score = 0
        # loop through all possible directions (horizontal, vertical, diagonal, anti-diagonal)
        for dr, dc in [(0, 1), (1, 0), (1, 1), (1, -1)]:
            # loop through all possible starting positions
            for r in range(game.num_rows):
                for c in range(game.num_cols):
                    # count the number of pieces for each player in a window of size 4
                    count = {self.name: 0, self.opp_name: 0, 0: 0}
                    for i in range(4):
                        nr = r + dr * i
                        nc = c + dc * i
                        # check if the position is valid
                        if nr >= 0 and nr < game.num_rows and nc >= 0 and nc < game.num_cols:
                            # update the count for the player at that position
                            if board[nr][nc] in count:
                                count[board[nr][nc]] += 1
                    # update the score based on the count
                    # if the window has 4 pieces for the current player, add a large positive value
                    if count[self.name] == 4:
                        score += 1000000
                    # if the window has 3 pieces for the current player and one empty space, add a smaller positive value
                    elif count[self.name] == 3 and count[0] == 1:
                        score += 100
                    # if the window has 2 pieces for the current player and two empty spaces, add an even smaller positive value
                    elif count[self.name] == 2 and count[0] == 2:
                        score += 10
                    # if the window has 4 pieces for the opponent player, subtract a large negative value
                    elif count[self.opp_name] == 4:
                        score -= 1000000
                    # if the window has 3 pieces for the opponent player and one empty space, subtract a smaller negative value
                    elif count[self.opp_name] == 3 and count[0] == 1:
                        score -= 100
                    # if the window has 2 pieces for the opponent player and two empty spaces, subtract an even smaller negative value
                    elif count[self.opp_name] == 2 and count[0] == 2:
                        score -= 10
        
        # return the final score
        print(f"best_score = {score}")
        return score
        """
        score=0
        center_array=[int(i) for i in list(board[:,game.num_cols//2])]
        center_count=center_array.count(self.name)
        score+=center_count*6
        for r in range(game.num_rows):
            row_array=[int(i) for i in list(board[r,:])]
            for c in range(game.num_cols-3):
                window=row_array[c:c+4]
                score+=self.evaluate_window(window,game)
        for c in range(game.num_cols):
            col_array=[int(i) for i in list(board[:,c])]
            for r in range(game.num_rows-3):
                window=col_array[r:r+4]
                score+=self.evaluate_window(window,game)
        for r in range(game.num_rows-3):
            for c in range(game.num_cols-3):
                window=[board[r+i][c+i] for i in range(4)]
                score+=self.evaluate_window(window,game)
        for r in range(game.num_rows-3):
            for c in range(game.num_cols-3):
                window=[board[r+3-i][c+i] for i in range(4)]
                score+=self.evaluate_window(window,game)
        return score
    def evaluate_window(self,window,game):
        score=0
        opp_name=2 if self.name==1 else 1
        if window.count(self.name)==4:
            score+=100
        elif window.count(self.name)==3 and window.count(0)==1:
            score+=5
        elif window.count(self.name)==2 and window.count(0)==2:
            score+=2
        if window.count(opp_name)==3 and window.count(0)==1:
            score-=4
        return score
    
class Connect4(QMainWindow):
    def __init__(self, num_rows=6, num_cols=7, player1_type = "Human", player2_type = "RandomComputer"):
        """
        Initializes the Connect4 game window with the specified number of rows and columns, and the types of players.

        Args:
        - num_rows (int): The number of rows in the game board. Default is 6.
        - num_cols (int): The number of columns in the game board. Default is 7.
        - player1_type (str): The type of player 1. Can be "Human" or "RandomComputer". Default is "Human".
        - player2_type (str): The type of player 2. Can be "Human" or "RandomComputer". Default is "RandomComputer".
        """
        super().__init__()
        self.setWindowTitle("Connect 4")
        self.setGeometry(100, 100, 700, 600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.board = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        self.players_dict = {"Human": Human, "RandomComputer": RandomComputer, "MiniMaxComputer": MiniMaxComputer}
        self.players = [self.players_dict[player1_type](1, "red"), self.players_dict[player2_type](2, "green")]
        self.current_player = self.players[0]
        self.create_board()
        self.create_turn_label()

        # render the window
        self.show()
        self.play()

    def create_board(self):
        """
        Creates the Connect4 game board with buttons and labels.

        Returns:
        - None
        """
        # add an empty row at the top
        self.grid_layout.addWidget(QLabel(), 0, 0, 1, self.num_cols)
        # add the buttons to the empty row
        for col in range(self.num_cols):
            button = QPushButton(str(col+1))
            button.clicked.connect(lambda _, col=col: self.play(col))
            self.grid_layout.addWidget(button, 1, col)
        # add the labels to the rest of the grid
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                label = QLabel()
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                label.setStyleSheet("background-color: blue; border: 1px solid black; border-radius: 20%;")
                self.grid_layout.addWidget(label, row+2, col)

        # set minimum size of widget containing the board
        widget = self.grid_layout.parentWidget()
        min_dimension = min(widget.width(), widget.height())
        cell_size = min_dimension // max(self.num_rows, self.num_cols)
        widget.setMinimumSize(cell_size * self.num_cols, cell_size * self.num_rows)
            
    def create_turn_label(self):
        """
        Creates the label indicating whose turn it is.

        Returns:
        - None
        """
        self.turn_label = QLabel(f"Player {self.current_player.name} turn")
        self.turn_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.turn_label.setStyleSheet(f"color: {self.current_player.color};")
        
        # remove the old label if it exists
        if self.grid_layout.itemAtPosition(self.num_rows+2, 0) is not None:
            self.grid_layout.itemAtPosition(self.num_rows+2, 0).widget().setParent(None)
        self.grid_layout.addWidget(self.turn_label, self.num_rows+2, 0, 1, self.num_cols)
        
    def play(self, col = None):
        """
        Plays a turn of the game, either by a human player or a computer player.

        Args:
        - col (int): The column in which to place the current player's piece. If None, the function will determine the move for a computer player.

        Returns:
        - None
        """
        QApplication.processEvents()
        if not isinstance(self.current_player, Human):
            col = self.current_player.play(self,board=self.board)
        if col is None:
            return
        row = self.num_rows - 1
        while row >= 0 and self.board[row][col] != 0:
            row -= 1
        if row < 0:
            return
        self.board[row][col] = self.current_player.name
        label = self.grid_layout.itemAtPosition(row+2, col).widget()
        label.setStyleSheet(f"background-color: {self.current_player.color}; border: 1px solid black; border-radius: 20%;")
        QApplication.processEvents()
        if self.check_win(row, col):
            self.show_result_dialog(f"Player {self.current_player.name} won!")
        elif self.check_tie():
            self.show_result_dialog("Tie game!")
        else:
            self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
            self.create_turn_label()
        
        if not isinstance(self.current_player, Human):
            self.play()
        
            
    def check_win(self, row, col):
        """
        Checks if the game has been won by the player who just made a move.

        Args:
        - row (int): The row in which the current player's piece was placed.
        - col (int): The column in which the current player's piece was placed.

        Returns:
        - bool: True if the game has been won by the current player, False otherwise.
        """
        player = self.board[row][col]
        # check horizontal
        count = 0
        for c in range(self.num_cols):
            if self.board[row][c] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        # check vertical
        count = 0
        for r in range(self.num_rows):
            if self.board[r][col] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        # check diagonal
        count = 0
        for i in range(-3, 4):
            r = row + i
            c = col + i
            if r < 0 or r >= self.num_rows or c < 0 or c >= self.num_cols:
                continue
            if self.board[r][c] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        # check anti-diagonal
        count = 0
        for i in range(-3, 4):
            r = row + i
            c = col - i
            if r < 0 or r >= self.num_rows or c < 0 or c >= self.num_cols:
                continue
            if self.board[r][c] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        return False
            
    def check_tie(self):
        """
        Checks if the game has ended in a tie.

        Returns:
        - bool: True if the game has ended in a tie, False otherwise.
        """
        
        for col in range(self.num_cols):
            if self.board[0][col] == 0:
                return False
        return True
    
    def show_result_dialog(self, message):
        """
        Shows a dialog indicating the result of the game.

        Args:
        - message (str): The message to display in the dialog.

        Returns:
        - None
        """
        dialog = QMessageBox()
        dialog.setWindowTitle("Game Over")
        dialog.setText(message)
        # dialog.setStandardButtons(QMessageBox.StandardButton.Retry | QMessageBox.StandardButton.Close)
        dialog.setStandardButtons(QMessageBox.StandardButton.Close)

        button = dialog.button(QMessageBox.StandardButton.Close)
        button.setText("Quit")

        # button = dialog.button(QMessageBox.StandardButton.Retry)
        # button.setText("Play Again")

        
        # dialog.setDefaultButton(QMessageBox.StandardButton.Retry)
        if dialog.exec() == QMessageBox.StandardButton.Close:
        #     # close all windows
        #     for widget in QApplication.topLevelWidgets():
        #         widget.close()
        #     # open the setup window
        #     self.connect4_setup = Connect4Setup()
        #     self.connect4_setup.show()
        # else:
            for widget in QApplication.topLevelWidgets():
                widget.close()
            QApplication.processEvents()


class Connect4Setup(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connect 4 Setup")
        self.setGeometry(600, 300, 300, 200)
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.num_rows_spinbox = QSpinBox()
        self.num_rows_spinbox.setMinimum(4)
        self.num_rows_spinbox.setMaximum(100)
        self.num_rows_spinbox.setValue(6)
        self.grid_layout.addWidget(QLabel("Number of rows:"), 0, 0)
        self.grid_layout.addWidget(self.num_rows_spinbox, 0, 1)
        self.num_cols_spinbox = QSpinBox()
        self.num_cols_spinbox.setMinimum(4)
        self.num_cols_spinbox.setMaximum(100)
        self.num_cols_spinbox.setValue(7)
        self.grid_layout.addWidget(QLabel("Number of columns:"), 0, 2)
        self.grid_layout.addWidget(self.num_cols_spinbox, 0, 3)

        self.player1_dropdown = QComboBox()
        self.player1_dropdown.addItem("Human")
        # self.player1_dropdown.addItem("RandomComputer")
        # self.player1_dropdown.addItem("MiniMaxComputer")

        self.player2_dropdown = QComboBox()
        self.player2_dropdown.addItem("Human")
        self.player2_dropdown.addItem("RandomComputer")
        self.player2_dropdown.addItem("MiniMaxComputer")
        self.player2_dropdown.setCurrentIndex(2)

        self.grid_layout.addWidget(QLabel("Player 1:"), 2, 0)
        self.grid_layout.addWidget(self.player1_dropdown, 2, 1)
        self.grid_layout.addWidget(QLabel("Player 2:"), 2, 2)
        self.grid_layout.addWidget(self.player2_dropdown, 2, 3)

        self.start_button = QPushButton("Start game")
        self.start_button.clicked.connect(self.start_game)
        self.grid_layout.addWidget(self.start_button, 3, 0, 1, 4)
        
        
    def start_game(self):
        num_rows = self.num_rows_spinbox.value()
        num_cols = self.num_cols_spinbox.value()
        player1 = self.player1_dropdown.currentText()
        player2 = self.player2_dropdown.currentText()
        self.connect4 = Connect4(num_rows, num_cols, player1, player2)
        self.connect4.showMaximized()
        self.connect4.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qdarktheme.setup_theme(theme="auto")
    connect4_setup = Connect4Setup()
    connect4_setup.show()
    sys.exit(app.exec())