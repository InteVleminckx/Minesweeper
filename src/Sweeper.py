import random as ra
import math
"""
Beginner – 9 * 9 Board and 10 Mines
Intermediate – 16 * 16 Board and 40 Mines
Advanced – 24 * 24 Board and 99 Mines
"""


class Cell:

    def __init__(self, i, j):
        self.isMine = False
        self.isClicked = False
        self.isFlagged = False
        self.isQuestioned = False
        self.neighbourMines = 0
        self.positionX = i
        self.positionY = j

    def addNeighbourMine(self):
        if not self.isMine:
            self.neighbourMines += 1

    def setSurroundings(self, grid):

        surroundings = [grid[self.positionX-1][self.positionY] if self.positionX - 1 >= 0 else None,
                        grid[self.positionX-1][self.positionY-1] if (self.positionX - 1 >= 0 and self.positionY - 1 >= 0) else None,
                        grid[self.positionX][self.positionY-1] if self.positionY - 1 >= 0 else None,
                        grid[self.positionX+1][self.positionY-1] if (self.positionX + 1 <= 8 and self.positionY - 1 >= 0) else None,
                        grid[self.positionX+1][self.positionY] if self.positionX + 1 <= 8 else None,
                        grid[self.positionX+1][self.positionY+1] if (self.positionX + 1 <= 8 and self.positionY + 1 <= 8) else None,
                        grid[self.positionX][self.positionY+1] if self.positionY + 1 <= 8 else None,
                        grid[self.positionX-1][self.positionY+1] if (self.positionX - 1 >= 0 and self.positionY + 1 <= 8) else None,]

        for cell in surroundings:
            if cell is not None:
                if cell.isMine is False:
                    cell.addNeighbourMine()

class Sweeper:

    def __init__(self):
        self.grid = list()
        self.mines = None
        self.squares = None

    def start(self, difficulty):
        if difficulty == 0:
            self.createGrid(9,10)
            self.mines = 10
            self.squares = 9*9
        elif difficulty == 1:
            self.createGrid(16,40)
            self.mines = 40
            self.squares = 16 * 16
        elif difficulty == 2:
            self.createGrid(24,99)
            self.mines = 99
            self.squares = 24 * 24

    def createGrid(self, size, mines):

        #First creating the full grid
        for i in range(size):
            row = list()
            for j in range(size):
                cell = Cell(i,j)
                row.append(cell)
            self.grid.append(row)

        fields = size*size

        while mines > 0:
            for i in range(size):
                for j in range(size):
                    rand = ra.randint(0,100) / 100
                    chance = mines / fields
                    if rand < chance:
                        if not self.grid[i][j].isMine and self.grid[i][j].neighbourMines == 0:
                            self.grid[i][j].isMine = True
                            self.grid[i][j].setSurroundings(self.grid)
                            mines -= 1
                            fields -= 1


    def checkClicked(self, mousePos, squareSize):
        y,x = math.floor(mousePos[0]/squareSize), math.floor(mousePos[1]/squareSize)
        if not self.grid[x][y].isClicked and not self.grid[x][y].isFlagged and not self.grid[x][y].isQuestioned:

            if self.grid[x][y].isMine:
                return False

            else:
                self.grid[x][y].isClicked = True
                self.grid[x][y].isFlagged = False
                self.grid[x][y].isQuestioned = False
                self.checkNeighbours(x, y)
                return True

    def checkFlagged(self, mousePos, squareSize):
        y,x = math.floor(mousePos[0]/squareSize), math.floor(mousePos[1]/squareSize)
        if not self.grid[x][y].isClicked:
            if not self.grid[x][y].isFlagged and not self.grid[x][y].isQuestioned:
                self.grid[x][y].isFlagged = True

            elif self.grid[x][y].isFlagged and not self.grid[x][y].isQuestioned:
                self.grid[x][y].isFlagged = False
                self.grid[x][y].isQuestioned = True

            elif not self.grid[x][y].isFlagged and self.grid[x][y].isQuestioned:
                self.grid[x][y].isFlagged = False
                self.grid[x][y].isQuestioned = False


    def checkNeighbours(self, x, y):
        surroundings = [self.grid[x-1][y] if x - 1 >= 0 else None,
                        self.grid[x][y-1] if y - 1 >= 0 else None,
                        self.grid[x+1][y] if x + 1 <= 8 else None,
                        self.grid[x][y+1] if y + 1 <= 8 else None
                        ]

        for neighbour in surroundings:
            if neighbour is not None:
                if neighbour.neighbourMines == 0 and neighbour.isFlagged is False and \
                    neighbour.isQuestioned is False and neighbour.isClicked is False and \
                        neighbour.isMine is False:

                        neighbour.isClicked = True
                        self.checkNeighbours(neighbour.positionX, neighbour.positionY)

    def checkWin(self):
        counterFlags = 0
        counterChecked = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j].isMine:
                    if not self.grid[i][j].isFlagged:
                        return False
                    else:
                        counterFlags += 1
                elif self.grid[i][j].isClicked:
                    counterChecked += 1

        if counterFlags == self.mines and counterChecked == self.squares - self.mines:
            return True
        return False

    def printGrid(self):
        grid = "+---+---+---+---+---+---+---+---+---+\n"
        for i in range(len(self.grid)):
            grid += "|"
            for j in range(len(self.grid[i])):
                if self.grid[i][j].isMine:
                    grid += " * |"
                elif self.grid[i][j].neighbourMines > 0:
                    grid += " " + str(self.grid[i][j].neighbourMines) + " |"
                else:
                    grid += "   |"

            grid += "\n+---+---+---+---+---+---+---+---+---+\n"
        print(grid)