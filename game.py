from board import Board
import AI

def playerMove(board):
    done = False
    while not done:
        move = input("Enter your move: ")
        try:
            move = int(move)
            move = move - 1
            if move > 8 or move < 0:
                print("Enter a number from 1 to 9\n")
            elif board[move] != " ":
                print("Square already taken!")
                continue
            else:
                done = True
        except ValueError as e:
            print("Enter a number from 1 to 9\n")
    return move
        
    
def main():
    print("Tic-tac-toe\n\n") 
    playing = True 
    while playing:
        print("New match\n\n")
        result = False
        board = Board()
        print(board)
        while not result:
            player_move = playerMove(board.board)
            board.insert("x", player_move)
            print("You played:", player_move+1)
            print("\n")
            print(board)
            print("\n")
            comp_move = AI.move(board.board)
            board.insert("o", comp_move)
            print(board)
            print("AI played: ", comp_move+1)
            result = board.check_result()
            print("\n")
        if result == "x":
            print("You won")
        elif result == "o":
            print("The AI won")
        else:
            print("Draw")
        
        play_again = input("Do you want to play again? (Y/N)").strip().upper()
        if play_again == "Y" or play_again == "YES":
            continue
        else:
            print("Thanks for playing!")
            playing = False     