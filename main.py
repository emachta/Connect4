#Connect 4
#Created by Ennis Machta 8/11/18

import tkinter

NONE = 0
RED = 1
BLACK = 2

class main():
    def __init__(self,turn):
        self.base = [[0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0]]
        self.turn = turn
        self.baseheight = len(self.base)
        self.count = 0
        
    def prettyprint(self):
        print("TURN: " + self.turn)
        for row in self.base:
            for item in row:
                print(self.convertNumtoLetter(item), end=' ')
            print()

    def convertNumtoLetter(self, num):
        if num == 0:
            return '.'
        elif num == 1:
            return 'R'
        elif num == 2:
            return 'B'

    def changeTurn(self):
        if self.turn == "B":
            self.turn = "R"
        elif self.turn == "R":
            self.turn = "B"
            
    def placeKey(self, key):
        while True:
            if key != 0:
                moveX = key
                key = 0
                if moveX < 1 or moveX > 7:
                    print("Out of bounds. Try again.")
                else:
                    break
                
        if self.turn == "R":
            for col in range(self.baseheight):
                if self.base[col][moveX-1] == 0:
                    self.checkWin(col-1,moveX-1)
                    pass
                elif self.base[col][moveX-1] == 1 or self.base[col][moveX-1] == 2:
                    if col - 1 < 0:
                        print("This column is full. Try again.")
                        self.changeTurn()
                    else:
                        self.base[col-1][moveX-1] = 1
                        self.count += 1
                        self.checkWin(col-1,moveX-1)
                        break
                    break
                if col == self.baseheight-1:
                    self.base[self.baseheight-1][moveX-1] = 1
                    self.count += 1
                    self.checkWin(col,moveX-1)
                    break

        elif self.turn == "B":
            for col in range(self.baseheight):
                if self.base[col][moveX-1] == 0:
                    self.checkWin(col-1,moveX-1)
                    pass
                elif self.base[col][moveX-1] == 1 or self.base[col][moveX-1] == 2:
                    if col - 1 < 0:
                        print("This column is full. Try again.")
                        self.changeTurn()
                    else:
                        self.base[col-1][moveX-1] = 2
                        self.count += 1
                        self.checkWin(col-1,moveX-1)
                        break
                    break
                if col == self.baseheight-1:
                    self.base[self.baseheight-1][moveX-1] = 2
                    self.count += 1
                    self.checkWin(col,moveX-1)
                    break
        mainGUI.updateCanvas()
        main.changeTurn()
                
    def checkWin(self,column,row):
        if self.count == 35:
            print("\n\n\n------------ No one wins..... \n\n Game Over.")
            self.prettyprint()
            quit()
        checklist = [[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[-1,1],[1,-1]]
        for coord in checklist:
            if self.checkCoord(column, row):
                if self.checkCoord(column+(coord[0]*1), row+(coord[1])*1):
                    if self.checkCoord(column+(coord[0]*2), row+(coord[1])*2):
                        if self.checkCoord(column+(coord[0]*3), row+(coord[1])*3):
                            print('\n\n-----------------\nWinner! ' + self.turn + "\n\n\n")
                            self.prettyprint()
                            mainGUI.endGamePopUp(self.turn)

    def checkCoord(self,col,row):
        if col >= 0 and col <= self.baseheight - 1 and row >= 0 and row <=6:
            if self.turn == "R":
                if self.base[col][row] == 1:
                    return True
                return False
            elif self.turn == "B":
                if self.base[col][row] == 2:
                    return True
                return False
            
    class GUI():
        def __init__(self, base):
            self.base = base
            self.number = 0
            self.canvas_height = 540
            self.canvas_width = 960
            self.mainwindow = tkinter.Tk()
            self.mainwindow.title("Connect 4")
            self.maincanvas = tkinter.Canvas(master=self.mainwindow, width=self.canvas_width,height=self.canvas_height, bd=0,bg="dark green",highlightthickness=0)
            self.maincanvas.create_rectangle(0,0,self.canvas_width,self.canvas_height, width = 0)
            self.maincanvas.grid()
            
            
            
            obj1ID = self.maincanvas.create_rectangle(0,0,137,540,fill="#2db3ad")
            obj2ID = self.maincanvas.create_rectangle(137,0,274,540,fill="#2db3ad")
            obj3ID = self.maincanvas.create_rectangle(274,0,411,540,fill="#2db3ad")
            obj4ID = self.maincanvas.create_rectangle(411,0,548,540,fill="#2db3ad")
            obj5ID = self.maincanvas.create_rectangle(548,0,685,540,fill="#2db3ad")
            obj6ID = self.maincanvas.create_rectangle(685,0,822,540,fill="#2db3ad")
            obj7ID = self.maincanvas.create_rectangle(822,0,960,540,fill="#2db3ad")
            
            self.maincanvas.create_rectangle(0,0,960,108)
            self.maincanvas.create_rectangle(0,108,960,216)
            self.maincanvas.create_rectangle(0,216,960,324)
            self.maincanvas.create_rectangle(0,324,960,432)
            self.maincanvas.create_rectangle(0,432,960,540)
            
            self.maincanvas.tag_bind(obj1ID,'<Button-1>',self.rect1)
            self.maincanvas.tag_bind(obj2ID,'<Button-1>',self.rect2)
            self.maincanvas.tag_bind(obj3ID,'<Button-1>',self.rect3)
            self.maincanvas.tag_bind(obj4ID,'<Button-1>',self.rect4)
            self.maincanvas.tag_bind(obj5ID,'<Button-1>',self.rect5)
            self.maincanvas.tag_bind(obj6ID,'<Button-1>',self.rect6)
            self.maincanvas.tag_bind(obj7ID,'<Button-1>',self.rect7)
            
        def rect1(self,point):
            main.placeKey(1)     
        def rect2(self,point):
            main.placeKey(2) 
        def rect3(self,point):
            main.placeKey(3) 
        def rect4(self,point):
            main.placeKey(4) 
        def rect5(self,point):
            main.placeKey(5) 
        def rect6(self,point):
            main.placeKey(6) 
        def rect7(self,point):
            main.placeKey(7) 
            
        def updateCanvas(self):
            for column in range(len(self.base)):
                for row in range(len(self.base[column])):
                    if self.base[column][row] == 1:
                        coords = self.convertCoordintoPixels(row,column)
                        self.maincanvas.create_oval(coords[0],coords[1],coords[2],coords[3],fill="red")
                    elif self.base[column][row] == 2:
                        coords = self.convertCoordintoPixels(row,column)
                        self.maincanvas.create_oval(coords[0],coords[1],coords[2],coords[3],fill="black")
                        
        def convertCoordintoPixels(self, x,y):
            newx = x * 137.14
            newy = y * 108
            return [int(newx),int(newy),int(newx+137.14),int(newy+108)]
        
        
        def endGamePopUp(self,turn):
            endwindow = tkinter.Tk()
            
            endwindow.title("Game Over")
            label = tkinter.Label(endwindow, text="Player: " + turn + " has won.")
            label.pack(side="top", padx = 20)
            okbutton = tkinter.Button(endwindow,text="OK", command=quit)
            okbutton.pack()
            
def turn():
    while True:
        turn = input("What turn starts? (Type R or B): ")
        if turn == "R" or turn == "B":
            return turn
        else:
            print("Error in input. Please try again.")


if __name__ == "__main__":
    main = main(turn())
    mainGUI = main.GUI(main.base)
    mainGUI.updateCanvas()
    mainGUI.mainwindow.mainloop()

    