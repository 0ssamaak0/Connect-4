def check_win(board, row, col, num_rows, num_cols):
        """
        Checks if the game has been won by the player who just made a move.

        Args:
        - row (int): The row in which the current player's piece was placed.
        - col (int): The column in which the current player's piece was placed.

        Returns:
        - bool: True if the game has been won by the current player, False otherwise.
        """
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
            
def check_tie(board, num_cols):
    """
    Checks if the game has ended in a tie.

    Returns:
    - bool: True if the game has ended in a tie, False otherwise.
    """
    
    for col in range(num_cols):
        if board[0][col] == 0:
            return False
    return True