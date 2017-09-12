import pygame


class Game:
    def __init__(self):
        self.board = [[" ", " ", " "],[" "," "," "],[" "," "," "]]
        self.moves = {"x", "o" }
        self.turn = True
        self.movecounter = 0
        self.winner = "poop"
        print "X goes first!"

    def show(self):
        for row in self.board:
            print "|".join(row)
            
    def move(self, x, y):
    
        if self.turn == True:
            self.board[x][y] = "x"
            self.movecounter += 1
        else:
            self.board[x][y] = "o"
            self.movecounter += 1
                
    def isValid(self, x, y):
        
        if x > 2 or y > 2 or x < 0 or y < 0:
            return False
        else:
            if self.board[x][y] != ' ':
                return False
            else:
                return True
        
            
    def gameover(self):
        
        row = {"x": 0, "o": 0}
        for ro in self.board:
            for item in ro:
                if item != " ":
                    row[item] += 1
            for key in row:
                if row[key] == 3:
                    self.winner = key
                    return True
            row = {"x": 0, "o": 0}
        
        col = {"x":0, "o": 0}
        for i in range(3):
            for j in range(3):
                if self.board[j][i] != " ":
                    col[self.board[j][i]] += 1
                    
            for key in col:
                if col[key] == 3:
                    self.winner = key
                    return True
            col = {"x":0, "o":0}
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != " ":
            self.winner = self.board[0][0]
            return True
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[0][2] != " ":
            self.winner = self.board[0][2]
            return True
        if self.movecounter == 9:
            self.winner = "Tie"
            return True

        return False

    def play(self):
        self.show()
        while not self.gameover():
            if self.turn == True:

                try:
                    x= input("X goes, choose an x spot:")
                except:
                    print "Invalid X coordinate, try again"
                    continue
                try:
                    y = input("X goes, choose an y spot:")
                except:
                    print "Invalid Y coordinate, try again"
                    continue
                
                if self.isValid(x-1,y-1):
                    self.move(x-1,y-1)            
                    self.turn = False
                    print("Nice move!")
                    
                    self.show()
                else:
                    print("Invalid move, try again.")
                    continue
            else:
               
                try:
                    x= input("O goes, choose an x spot:")
                except:
                    print "Invalid X coordinate, try again"
                    continue
                try:
                    y = input("O goes, choose an y spot:")
                except:
                    print "Invalid Y coordinate, try again"
                    continue
               
                    
                if self.isValid(x-1,y-1):
                    self.move(x-1,y-1)            
                    self.turn = True
                    print("Nice move!")
                    self.show()
                else:
                    print("Invalid move, try again.")
                    continue
        
        print "Game Over!"
        if self.winner == "Tie":
            print "Tie!"
        else: 
            print "The winner was: " +str(self.winner) + "!"
        again = input("Play again? Press y for yes, n for no:")
        
        if again == "y":
            self.board = [[" ", " ", " "],[" "," "," "],[" "," "," "]]
            self.moves = {"x", "o" }
            self.turn = True
            self.movecounter = 0
            self.winner = None
            print "X goes first"
            self.play()
        else:
            print "Thanks for playing."
            
def main():
    First = Game()
    First.play()

if __name__ == "__main__":
    main()

    
    
