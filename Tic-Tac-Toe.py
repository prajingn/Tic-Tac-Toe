class Game:
    def __init__(self):
        self.board = [[' ', ' ', ' '] for i in range(3)]
        self.freeSpace = 9
        self.p1 = Player('X', self)
        self.p2 = Player('O', self)

    def printBoard(self):
        print()
        print(f" {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} ")
        print("---|---|---")
        print(f" {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} ")
        print("---|---|---")
        print(f" {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} ")

    def runGame(self):
        self.board = [[' ', ' ', ' '] for i in range(3)]
        self.freeSpace = 9
        status = None
        while(True):
            self.printBoard()
            status = self.p1.play()
            if status: 
                break
            self.printBoard()
            status = self.p2.play()
            if status:
                break
        
        if status == "X" or status == "O":
            playerName = self.p1.name if self.p1.symbol == status else self.p2.name
            self.printBoard()
            print(f"\nThe WINNER is: {playerName} ({status})")
        else:
            print("\nIt is a TIE")


class Player:
    playerNum = 1
    def __init__(self, symbol, gameObj):
        self.name = input(f"Enter name of player {Player.playerNum}: ").strip().title()
        self.symbol = symbol
        self.gameObj = gameObj
        Player.playerNum += 1

    def play(self):
        print(f"{self.name}'s turn ({self.symbol}):")
        while True:
            try:
                self.x = int(input("Enter row #(1 - 3): ")) - 1
                self.y = int(input("Enter column #(1 - 3): ")) - 1
            except ValueError:
                print("Enter an integer between 1 and 3!\n")
                continue

            try:
                if self.gameObj.board[self.x][self.y] == " ":
                    self.gameObj.board[self.x][self.y] = self.symbol
                    self.gameObj.freeSpace -= 1
                    break
                else:
                    print("Enter valid slot!\n")
            except IndexError:
                print("Enter value between 1 and 3!\n")
        return self.getStatus()
    
    def getStatus(self):
        for i in range(3):
            if self.gameObj.board[i][0] == self.gameObj.board[i][1] == self.gameObj.board[i][2] == self.symbol:
                return self.symbol
        for i in range(3):
            if self.gameObj.board[0][i] == self.gameObj.board[1][i] == self.gameObj.board[2][i] == self.symbol:
                return self.symbol
        if self.gameObj.board[0][0] == self.gameObj.board[1][1] == self.gameObj.board[2][2] == self.symbol:
            return self.symbol
        if self.gameObj.board[0][2] == self.gameObj.board[1][1] == self.gameObj.board[2][0] == self.symbol:
            return self.symbol
        
        if self.gameObj.freeSpace == 0: return "tie"



print(r"""
 _______ _        _______           _______         
|__   __(_)      |__   __|         |__   __|        
   | |   _  ___     | | __ _  ___     | | ___   ___ 
   | |  | |/ __|    | |/ _` |/ __|    | |/ _ \ / _ \
   | |  | | (__     | | (_| | (__     | | (_) |  __/
   |_|  |_|\___|    |_|\__,_|\___|    |_|\___/ \___|
                                                   
            Let's go...
    """)

g = Game()
while True:
    print()
    g.runGame()
    playAgain = input("\nPlay Again? (Y / n): ").strip().lower()
    if playAgain == 'n':
        break
