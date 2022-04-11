import pygame
import sys
import src.Flag as Flag
import src.Mine as Mine
from src.Sweeper import *
# from screeninfo import get_monitors
# import os

class Visualize:

    def __init__(self):


        pygame.init()
        self.mines = []
        self.flags = []
        self.questions = []
        self.squares = []
        self.clickedSquares = []
        self.font = None
        self.width = None
        self.height = None
        self.squareSize = 30
        self.surface = None
        self.minesweeper = None
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.surfaceColor = (111,111,111)
        self.squareColor = (177,177,177)
        self.surface = pygame.display.set_mode((500, 500))
        self.MenuFont = pygame.font.SysFont("comicsansms", 40)
        pygame.display.set_caption("Minesweeper")
        self.font = pygame.font.SysFont("comicsansms", 20)

    def initialize(self, minesweeper):
        self.minesweeper = minesweeper
        size = len(self.minesweeper.grid[0])
        self.width = size*self.squareSize
        self.height = size*self.squareSize + 50
        pygame.display.set_mode((self.width, self.height))

    def gameLoop(self):
        menu = True
        gameplay = False
        losescreen = False
        winscreen = False
        clicked = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stopGame()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if gameplay:
                        end = self.minesweeper.checkClicked(pygame.mouse.get_pos(), self.squareSize)
                        if end is False:
                            losescreen = True
                            gameplay = False


                    elif menu or losescreen or winscreen:
                        clicked = True
                        x,y = pygame.mouse.get_pos()
                        difficulty = None
                        if 350<= y <= 400:
                            if 12.5 <= x <= 162.5:
                                difficulty = 0

                            elif 175 <= x <= 325:
                                difficulty = 1

                            elif 337.5 <= x <= 478.5:
                                difficulty = 2

                        if difficulty is not None:
                            menu = False
                            losescreen = False
                            gameplay = True
                            clicked = False
                            mineSweeper = Sweeper()
                            mineSweeper.start(difficulty)
                            self.initialize(mineSweeper)

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    self.minesweeper.checkFlagged(pygame.mouse.get_pos(), self.squareSize)

            if menu:
                self.menu()

            elif gameplay:
                self.startGame()
                if self.minesweeper.checkWin():
                    gameplay = False
                    winscreen = True

            elif losescreen:
                self.loseScreen(clicked)

            elif winscreen:
                self.winScreen()

            pygame.display.flip()

    def startGame(self):

        self.surface.fill(self.surfaceColor)
        self.checkSpecials()
        self.drawFlags()
        self.drawQuestions()
        self.drawSquares()
        self.drawClickedSquares()
        self.drawMines()
        self.drawGrid()
        self.drawNumberOfFlags()

    def menu(self):
        self.surface.fill(self.surfaceColor)
        text = self.MenuFont.render('MINESWEEPER', True, self.black)
        text2 = self.MenuFont.render('Click difficulty to start', True, self.black)

        textRect = text.get_rect()
        textRect2 = text2.get_rect()
        textRect.center = (250, 200)
        textRect2.center = (250, 250)

        self.surface.blit(text, textRect)
        self.surface.blit(text2, textRect2)

        pygame.draw.rect(self.surface, self.red, pygame.Rect(12.5, 350, 150, 50))
        pygame.draw.rect(self.surface, self.green, pygame.Rect(175, 350, 150, 50))
        pygame.draw.rect(self.surface, self.blue, pygame.Rect(337.5, 350, 150, 50))

        easy = self.MenuFont.render("Easy", True, self.black)
        medium = self.MenuFont.render("Medium", True, self.black)
        hard = self.MenuFont.render("Hard", True, self.black)

        easyRect = easy.get_rect()
        mediumRect = medium.get_rect()
        hardRect = hard.get_rect()

        easyRect.center = (87.5, 370)
        mediumRect.center = (250, 370)
        hardRect.center = (412.5, 370)

        self.surface.blit(easy, easyRect)
        self.surface.blit(medium, mediumRect)
        self.surface.blit(hard, hardRect)

    def winScreen(self):
        pygame.display.set_mode((500, 500))
        self.surface.fill(self.surfaceColor)
        text = self.MenuFont.render('You won!', True, self.black)
        text2 = self.MenuFont.render('Click difficulty to replay', True, self.black)

        textRect = text.get_rect()
        textRect2 = text2.get_rect()
        textRect.center = (250, 200)
        textRect2.center = (250, 250)

        self.surface.blit(text, textRect)
        self.surface.blit(text2, textRect2)

        pygame.draw.rect(self.surface, self.red, pygame.Rect(12.5, 350, 150, 50))
        pygame.draw.rect(self.surface, self.green, pygame.Rect(175, 350, 150, 50))
        pygame.draw.rect(self.surface, self.blue, pygame.Rect(337.5, 350, 150, 50))

        easy = self.MenuFont.render("Easy", True, self.black)
        medium = self.MenuFont.render("Medium", True, self.black)
        hard = self.MenuFont.render("Hard", True, self.black)

        easyRect = easy.get_rect()
        mediumRect = medium.get_rect()
        hardRect = hard.get_rect()

        easyRect.center = (87.5, 370)
        mediumRect.center = (250, 370)
        hardRect.center = (412.5, 370)

        self.surface.blit(easy, easyRect)
        self.surface.blit(medium, mediumRect)
        self.surface.blit(hard, hardRect)


    def loseScreen(self,clicked):

        if clicked:
            pygame.display.set_mode((500, 500))
            self.surface.fill(self.surfaceColor)
            text = self.MenuFont.render('You died!', True, self.black)
            text2 = self.MenuFont.render('Click difficulty to restart', True, self.black)

            textRect = text.get_rect()
            textRect2 = text2.get_rect()
            textRect.center = (250, 200)
            textRect2.center = (250, 250)

            self.surface.blit(text, textRect)
            self.surface.blit(text2, textRect2)

            pygame.draw.rect(self.surface, self.red, pygame.Rect(12.5, 350, 150, 50))
            pygame.draw.rect(self.surface, self.green, pygame.Rect(175, 350, 150, 50))
            pygame.draw.rect(self.surface, self.blue, pygame.Rect(337.5, 350, 150, 50))

            easy = self.MenuFont.render("Easy", True, self.black)
            medium = self.MenuFont.render("Medium", True, self.black)
            hard = self.MenuFont.render("Hard", True, self.black)

            easyRect = easy.get_rect()
            mediumRect = medium.get_rect()
            hardRect = hard.get_rect()

            easyRect.center = (87.5, 370)
            mediumRect.center = (250, 370)
            hardRect.center = (412.5, 370)

            self.surface.blit(easy, easyRect)
            self.surface.blit(medium, mediumRect)
            self.surface.blit(hard, hardRect)

        else:
            self.drawAll()

    def stopGame(self):
        pygame.quit()
        sys.exit()


    def drawNumberOfFlags(self):
        stri = "FLAGS: " + str(self.minesweeper.numberFlags)
        text = self.MenuFont.render(stri, True, self.red)
        textRect = text.get_rect()
        textRect.center = (self.width/2, self.height-25)
        self.surface.blit(text, textRect)

    def drawAll(self):
        self.mines.clear()
        self.questions.clear()
        self.squares.clear()
        self.flags.clear()
        self.clickedSquares.clear()

        for i in range(len(self.minesweeper.grid)):
            for j in range(len(self.minesweeper.grid[i])):
                if self.minesweeper.grid[i][j].isMine:
                    mine = Mine.Mine(self.surfaceColor, self.squareSize, self.squareSize)
                    mine.rect.x = self.squareSize * j
                    mine.rect.y = self.squareSize * i
                    self.mines.append(mine)
                elif self.minesweeper.grid[i][j].isFlagged:
                    flag = Flag.Flag(self.surfaceColor, self.squareSize, self.squareSize)
                    flag.rect.x = self.squareSize * j
                    flag.rect.y = self.squareSize * i
                    self.flags.append(flag)
                elif self.minesweeper.grid[i][j].isQuestioned:
                    self.questions.append((i,j))

                else:
                    square = pygame.Rect(j * self.squareSize, i * self.squareSize, self.squareSize, self.squareSize)
                    self.clickedSquares.append((square, (i, j)))

        self.drawMines()
        self.drawFlags()
        self.drawGrid()
        self.drawQuestions()
        self.drawClickedSquares()
        self.drawNumberOfFlags()

    def drawGrid(self):
        for i in range(len(self.minesweeper.grid)):
            for j in range(len(self.minesweeper.grid[i])):
                pygame.draw.rect(self.surface, self.black, pygame.Rect(i*self.squareSize, j*self.squareSize, self.squareSize, self.squareSize), 1)

    def checkSpecials(self):
        self.mines.clear()
        self.questions.clear()
        self.squares.clear()
        self.flags.clear()
        self.clickedSquares.clear()

        for i in range(len(self.minesweeper.grid)):
            for j in range(len(self.minesweeper.grid[i])):
                if self.minesweeper.grid[i][j].isClicked:
                    if self.minesweeper.grid[i][j].isMine:
                        mine = Mine.Mine(self.surfaceColor, self.squareSize, self.squareSize)
                        mine.rect.x = self.squareSize * j
                        mine.rect.y = self.squareSize * i
                        self.mines.append(mine)

                    else:
                        square = pygame.Rect(j*self.squareSize, i*self.squareSize, self.squareSize, self.squareSize)
                        self.clickedSquares.append((square, (i,j)))

                elif self.minesweeper.grid[i][j].isFlagged:
                    flag = Flag.Flag(self.surfaceColor, self.squareSize, self.squareSize)
                    flag.rect.x = self.squareSize * j
                    flag.rect.y = self.squareSize * i
                    self.flags.append(flag)

                elif self.minesweeper.grid[i][j].isQuestioned:
                    self.questions.append((i,j))

                else:
                    square = pygame.Rect(j*self.squareSize, i*self.squareSize, self.squareSize, self.squareSize)
                    self.squares.append(square)

    def drawQuestions(self):
        for question in self.questions:
            y,x = question
            text = self.font.render('?', True, self.black)
            textRect = text.get_rect()
            textRect.center = (x * 30 + 15, y * 30 + 15)
            self.surface.blit(text, textRect)

    def drawMines(self):
        all_mines = pygame.sprite.Group()
        for mine in self.mines:
            all_mines.add(mine)

        all_mines.update()
        all_mines.draw(self.surface)

    def drawFlags(self):
        all_flags = pygame.sprite.Group()
        for flag in self.flags:
            all_flags.add(flag)

        all_flags.update()
        all_flags.draw(self.surface)

    def drawSquares(self):
        for square in self.squares:
            pygame.draw.rect(self.surface, self.squareColor, square)


    def drawClickedSquares(self):
        for square in self.clickedSquares:
            i,j = square[1]
            # print(i,j)
            number = self.minesweeper.grid[i][j].neighbourMines
            text = self.font.render('', True, self.green)

            if number == 0:
                pass
            elif number == 1:
                text = self.font.render('1', True, self.green)
            elif number == 2:
                text = self.font.render('2', True, self.blue)
            elif number == 3:
                text = self.font.render('3', True, self.red)
            elif number == 4:
                text = self.font.render('4', True, self.green)
            elif number == 5:
                text = self.font.render('5', True, self.blue)
            elif number == 6:
                text = self.font.render('6', True, self.red)

            textRect = text.get_rect()
            textRect.center = (j*30 + 15, i*30 + 15)

            self.surface.blit(text, textRect)