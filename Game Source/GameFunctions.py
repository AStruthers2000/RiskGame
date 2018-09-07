class GameFunctions:
    def initGame(self, frame, canvas):
        from PIL import Image
        from PIL import ImageTk

        self.image = Image.open("TextBox.png")
        self.image = self.image.resize((282,183), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        canvas.create_image(155,240, image=self.photo, anchor="nw")
        
        print("Game inited")
