import sys
import qdarktheme
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QLabel, QSpinBox, QMessageBox, QComboBox
from PyQt6.QtGui import QIcon, QPixmap, QPainter, QBrush, QPen
from PyQt6.QtCore import Qt
import random, time

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

    def play(self, board):
        time.sleep(0.5)
        available_cols = [col for col in range(len(board[0])) if board[0][col] == 0]
        if available_cols:
            return random.choice(available_cols)
        else:
            return None
class MiniMaxComputer(Player):
    def __init__(self, name, color):
        super().__init__(name, color)

    def play(self, board):
        #TODO
        pass
    

class Connect4(QMainWindow):
    def __init__(self, num_rows=6, num_cols=7, player1_type = "Human", player2_type = "RandomComputer"):
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
        self.players = [self.players_dict[player1_type](1, "red"), self.players_dict[player2_type](-1, "green")]
        self.current_player = self.players[0]
        self.create_board()
        self.create_turn_label()

        # render the window
        self.show()
        
        print("START")
        self.play()

    def create_board(self):
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
        self.turn_label = QLabel(f"Player {self.current_player.name}'s turn")
        self.turn_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.turn_label.setStyleSheet(f"color: {self.current_player.color};")
        # remove the old label if it exists
        if self.grid_layout.itemAtPosition(self.num_rows+2, 0) is not None:
            self.grid_layout.itemAtPosition(self.num_rows+2, 0).widget().setParent(None)
        self.grid_layout.addWidget(self.turn_label, self.num_rows+2, 0, 1, self.num_cols)
        
    def play(self, col = None):
        if not isinstance(self.current_player, Human):
            col = self.current_player.play(self.board)
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
        if check_win(self.board, row, col, self.num_rows, self.num_cols):
            self.show_result_dialog(f"Player {self.current_player.name} won!")
        elif check_tie(self.num_cols, self.board):
            self.show_result_dialog("Tie game!")
        else:
            self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
            self.create_turn_label()
        
        if not isinstance(self.current_player, Human):
            self.play()
        
            
    
            

    
    def show_result_dialog(self, message):
        dialog = QMessageBox()
        dialog.setWindowTitle("Game Over")
        dialog.setText(message)
        dialog.setStandardButtons(QMessageBox.StandardButton.Retry | QMessageBox.StandardButton.Close)

        button = dialog.button(QMessageBox.StandardButton.Close)
        button.setText("Quit")

        button = dialog.button(QMessageBox.StandardButton.Retry)
        button.setText("Play Again")

        
        dialog.setDefaultButton(QMessageBox.StandardButton.Retry)
        if dialog.exec() == QMessageBox.StandardButton.Retry:
            self.close()
            self.connect4_setup = Connect4Setup()
            self.connect4_setup.show()
        else:
            self.close()

def check_tie(num_cols, board):
    for col in range(num_cols):
        if board[0][col] == 0:
            return False
    return True

def check_win(board, row, col, num_rows, num_cols):
        player = board[row][col]
        # check horizontal
        count = 0
        for c in range(num_cols):
            if board[row][c] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        # check vertical
        count = 0
        for r in range(num_rows):
            if board[r][col] == player:
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
            if r < 0 or r >= num_rows or c < 0 or c >= num_cols:
                continue
            if board[r][c] == player:
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
            if r < 0 or r >= num_rows or c < 0 or c >= num_cols:
                continue
            if board[r][c] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        return False
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
        # set default to MiniMaxComputer
        self.player2_dropdown.setCurrentIndex(1)

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
        self.connect4.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qdarktheme.setup_theme(theme="auto")
    connect4_setup = Connect4Setup()
    connect4_setup.show()
    sys.exit(app.exec())