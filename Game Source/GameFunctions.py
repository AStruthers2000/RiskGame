class GameFunctions:
    def __init__(self):
        self.curX = 1000
        self.curY = 0

    def initGame(self, frame, canvas):
        from PIL import Image
        from PIL import ImageTk
        from tkinter import Label
        from tkinter import Entry
        import GraphicsMain

        """def get_info(self, entry):
            print(entry.get())

        Label(canvas, text = "Amount of players: ").grid(row=0)
        entry = Entry(frame)
        entry.grid(row=0, column=1)"""

        players = []
        playerNum = int(input("Amount of players: "))
        colors = ["red2", "yellow", "blue2", "lime green", "gray2", "saddle brown"]
        inputColors = {
            "red": colors[0],
            "yellow": colors[1],
            "blue": colors[2],
            "green": colors[3],
            "black": colors[4],
            "brown":colors[5]
        }
        takenColors = []

        for i in range(playerNum):
            playerName = input("Whats your name: ")
            print("Hello " + playerName + ". What color?")
            for name,real in inputColors.items():
                if not name in takenColors:
                    print("\t" + name)
            color = input("")
            takenColors += [color]
            playerColor = inputColors[color]
            players += [(playerName, playerColor)]

        print(players)
        totalArmies = 35 - (playerNum-3)*5
        """for j in range(totalArmies):
            for k in players:
                print(k[0] + " pick a country: ")
                print(GraphicsMain.GraphicsMain().currentClickedCountry)"""              
        
        print("Game inited")

    def printOnScreen(self, canvas, text):
        canvas.delete("printText")
        canvas.create_text(self.curX,
                           self.curY,
                           anchor="nw",
                           fill="ghost white",
                           font="Times",
                           text=text,
                           tag="printText")
