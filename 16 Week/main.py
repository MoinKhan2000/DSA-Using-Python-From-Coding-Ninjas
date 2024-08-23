from tkinter import Frame, Label, CENTER

import Logics
import constant as c


class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title("2048 Game ")
        self.master.bind("<Key>", self.key_down)
        self.commands = {
            c.keyUp: Logics.upMove,
            c.keyDown: Logics.downMove,
            c.keyLeft: Logics.leftMove,
            c.keyRight: Logics.rightMove,
        }
        self.gridCell = []
        self.initGrid()
        self.initMatrix()
        self.updateGridCells()
        self.mainloop()

    def initGrid(self):
        background = Frame(self, bg=c.bgColorGame, width=c.size, height=c.size)
        background.grid()
        for i in range(c.gridLen):
            gridRow = []
            for j in range(c.gridLen):
                cell = Frame(
                    background,
                    bg=c.bgColorCellEmpty,
                    width=c.size / c.gridLen,
                    height=c.size / c.gridLen,
                )
                cell.grid(row=i, column=j, padx=c.gridPadding, pady=c.gridPadding)

                t = Label(
                    master=cell,
                    text="",
                    bg=c.bgColorCellEmpty,
                    justify=CENTER,
                    font=c.font,
                    width=5,
                    height=2,
                )
                t.grid()
                gridRow.append(t)
            self.gridCell.append(gridRow)

    def initMatrix(self):
        self.matrix = Logics.startGame()
        Logics.addNew2(self.matrix)
        Logics.addNew2(self.matrix)

    def updateGridCells(self):
        for i in range(c.gridLen):
            for j in range(c.gridLen):
                newNumber = self.matrix[i][j]
                if newNumber == 0:
                    self.gridCell[i][j].configure(text="", bg=c.bgColorCellEmpty)
                else:
                    self.gridCell[i][j].configure(
                        text=str(newNumber),
                        bg=c.backColorDict[newNumber],
                        fg=c.cellColorDict[newNumber],
                    )
        self.update_idletasks()

    def key_down(self, event):
        key = event.keysym
        if key in self.commands:
            self.matrix, changed = self.commands[event.keysym](self.matrix)
            if changed:
                Logics.addNew2(self.matrix)
                self.updateGridCells()
                changed = False
                if Logics.getCurrentStatus(self.matrix) == "WON":
                    self.gridCell[1][1].configure(text="You", bg=c.bgColorCellEmpty)
                    self.gridCell[1][2].configure(text="Win!", bg=c.bgColorCellEmpty)

                if Logics.getCurrentStatus(self.matrix) == "Game - Over":
                    self.gridCell[1][1].configure(text="You", bg=c.bgColorCellEmpty)
                    self.gridCell[1][2].configure(text="Lost!", bg=c.bgColorCellEmpty)


g = Game2048()
