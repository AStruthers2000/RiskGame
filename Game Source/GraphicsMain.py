class GraphicsMain:
    
    def updateBoard(self, frame, canvas, continents):#more stuff probably
        from tkinter import W
        
        for continentName, countryGroup in continents.items():
            for countryName, country in continents[continentName].items():
                canvas.create_text(country.textPos[0],
                                   country.textPos[1],
                                   anchor=W,
                                   fill=country.textColor,
                                   font="Times",
                                   text=country.curPeople)
                
    def mainThread(self, threadName):
        import tkinter as tk
        from tkinter import Canvas
        from PIL import Image
        from PIL import ImageTk
        import _thread as thread

        from GameFunctions import GameFunctions
        import Rectangle
        import allCountries

        def key(event):
            print("Pressed: " + repr(event.char))

        def on_click(event):
            print("Clicked at: " + str(event.x) + ", " + str(event.y))
            CountryInfo = allCountries.CountryInfo()
            clickedOnCountry = CountryInfo.GetCountryNameByClick([event.x, event.y])
            print(clickedOnCountry + ", bordered by: ")
            for i in CountryInfo.GetBorderingCountries(clickedOnCountry):
                print("\t\t" + i)
            print("\tOccupied by: " + CountryInfo.GetCurrentOccupent(clickedOnCountry))
            print("\t\tWith: " + str(CountryInfo.GetCurrentSoliderCount(clickedOnCountry)) + " soliders")
            
        frame = tk.Tk()

        frame.state("zoomed")
        frame.title(threadName)

        #creating the canvas
        canvas = Canvas(width=1000, height = 664, bg="black")
        canvas.pack()

        #adding image
        image = Image.open("RiskBoard.jpg")
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0,0, image=photo, anchor="nw")

        """image = Image.open("TextBox.jpg")
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(100,100, image=photo, anchor="nw")"""

        #binding click event
        canvas.bind("<Button-1>", on_click)

        #test: drawing rectangles   
        """country = [930,440, 1000,440, 1000,550, 930,550]
        canvas.create_polygon(country, fill='red', outline='black')
        """

        #uncomment for collider debugging
        """
        continents = allCountries.continents
        for continentName, countryGroup in continents.items():
            for countryName, country in continents[continentName].items():
                canvas.create_polygon(country.colliderPoints, fill='red', outline='black')
        """

    
        #init game
        thread.start_new_thread(GraphicsMain().updateBoard, (frame, canvas, allCountries.continents, ))
        #thread.start_new_thread(GameFunctions.initGame, (frame, canvas, canvas))
        
        #starting frame loop
        frame.mainloop()

        
