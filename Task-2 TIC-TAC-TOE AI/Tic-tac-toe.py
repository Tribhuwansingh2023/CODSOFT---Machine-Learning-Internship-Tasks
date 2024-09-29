import numpy as np  
 
PLAYER_X = "X"  
PLAYER_O = "O"  
EMPTY = "."  

class TicTacToe:  
    def __init__(self):  
        self.board = np.full((3, 3), EMPTY)  
        self.current_player = PLAYER_X   

    def print_board(self):  
        print("\n".join(" ".join(row) for row in self.board))  
        print()  

    def is_winner(self, player): 
        for i in range(3):  
            if all(self.board[i, j] == player for j in range(3)) or \
               all(self.board[j, i] == player for j in range(3)):  
                return True  
        if all(self.board[i, i] == player for i in range(3)) or \
           all(self.board[i, 2 - i] == player for i in range(3)):  
            return True  
        return False  

    def is_draw(self):  
        return np.all(self.board != EMPTY)  

    def available_moves(self):  
        return [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == EMPTY]  

    def make_move(self, i, j, player):  
        self.board[i, j] = player  

    def minimax(self, is_maximizing):  
        if self.is_winner(PLAYER_O):  
            return 1   
        elif self.is_winner(PLAYER_X):  
            return -1    
        elif self.is_draw():  
            return 0  

        if is_maximizing:  
            best_value = -np.inf  
            for i, j in self.available_moves():  
                self.make_move(i, j, PLAYER_O)  
                score = self.minimax(False)  
                self.make_move(i, j, EMPTY)  
                best_value = max(best_value, score)  
            return best_value  
        else:  
            best_value = np.inf  
            for i, j in self.available_moves():  
                self.make_move(i, j, PLAYER_X)  
                score = self.minimax(True)  
                self.make_move(i, j, EMPTY)  
                best_value = min(best_value, score)  
            return best_value  

    def best_move(self):  
        best_value = -np.inf  
        move = (-1, -1)  
        for i, j in self.available_moves():  
            self.make_move(i, j, PLAYER_O) 
            move_value = self.minimax(False)  
            self.make_move(i, j, EMPTY)  
            if move_value > best_value:  
                best_value = move_value  
                move = (i, j)  
        return move  

    def play_game(self):  
        while True:  
            self.print_board()  
            
            if self.current_player == PLAYER_X:  
                print("Human's turn (X). Enter row and column (0, 1, or 2):")  
                try:  
                    row, col = map(int, input("Row and Column: ").strip().split())  
                    if self.board[row, col] != EMPTY:  
                        print("Invalid move! Try again.")  
                        continue  
                    self.make_move(row, col, PLAYER_X)  
                except (ValueError, IndexError):  
                    print("Invalid input, please enter row and column from 0 to 2.")  
                    continue  
            else:  
                print("AI's turn (O).")  
                row, col = self.best_move()  
                self.make_move(row, col, PLAYER_O)  
                print(f"AI chose: {row} {col}")  

            if self.is_winner(PLAYER_X):  
                self.print_board()  
                print("Human X wins!")  
                break  
            elif self.is_winner(PLAYER_O):  
                self.print_board()  
                print("AI O wins!")  
                break  
            elif self.is_draw():  
                self.print_board()  
                print("It's a draw!")  
                break
            self.current_player = PLAYER_X if self.current_player == PLAYER_O else PLAYER_O  
game = TicTacToe()  
game.play_game()