import pygame
from GameStage import *
from Text import *
from Player import *

class motor:
    # Class Motor constructor
    def __init__(self):
        print("Initializing game")

    # When this function is called in the main class, the game intializes
    def run(self):

        # GLOBAL VARIABLE EVENT -> CHECKS FOR MOUSE CLICKS AND EXIT
        global event

        # INITIATES PYGAME
        pygame.init()

        #This initaliazes the window
        window = pygame.display.set_mode((600,600))

        # Title
        pygame.display.set_caption("Pokemon")

        #RGB COLORS
        white = [255, 255, 255]
        red = [255, 0, 0]
        green = [0, 255, 0]
        blue = [0, 0, 255]
        black = [0, 0, 0]
        paleLavander = [213, 204, 255]
        lightRed = [255, 51, 51]
        lightGray = [224, 224, 223]
        yellow = [215, 209, 43]
        lightBlue = [173, 216, 230]

        # Clock that regulates the game's framerate
        clock = pygame.time.Clock()

        # Boolean that controls the main loop
        gameRuns = True

        # Object that regulates in which gameStage the player is
        gameStage = gamestage(pygame.image.load('images/mainMenu/startMenuBG.png'),window,-40,0,"mainMenu")

        # PLAYER OBJECT
        trainer = player("","","")

        # professor oak's dialogue counter oPC stands for oakPhrasesCounter
        oPC = 0

        # Boolean that sets the player's gender
        isMale = None


        """
        Method that draws the window and keeps updating it
        """
        def drawWindow():
            window.blit(gameStage.bgImage,(gameStage.bgCoords))

        """
        Method that checks in which section of the game the player is
        """
        def checkGameStage():
            if(gameStage.stage == "mainMenu"):
                 gameStage.mainMenu(paleLavander, lightRed, green,event)

            elif gameStage.stage == "optionsMenu":
                gameStage.optionsMenu(paleLavander, lightRed, green, event)

            elif gameStage.stage == "controlsMenu":
                gameStage.controlsMenu(paleLavander, lightRed, green, event)

            elif gameStage.stage == "createPlayer":
                createPlayer()

        def timeDelay(x, td):
            j = 0
            while j < x:
                pygame.time.delay(td)
                j += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        j = x + 3
                        pygame.quit()

        """
        Method that manages the logic of creating the playerself.
        This method is not in the GameStage class because it manages an object
        instantiated in this class
        """
        def createPlayer():
            nonlocal oPC
            gameStage.bgImage = pygame.image.load('images/backgrounds/introBG.png')
            gameStage.bgCoords = [0,0]
            mouse = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed()
            oakPhrases = ['Welcome, I am professor Oak','I will guide you in this new experience',
                          'What is your name?','It is nice to meet you ' + trainer.name, "Which character do you want to be?",
                          'Perfect!','Now, choose your starter pokemon', 'Perfect! You are ready to go!']

            oakPhrasesTextBox = text(window,oakPhrases[oPC])
            oakPhrasesTextBox.draw()
            if keys[pygame.K_SPACE]:
                if oPC == 2:
                    if trainer.nameMethod != "":
                        oPC +=1
                        timeDelay(30,10)
                elif oPC == 4:
                    if isMale is not None:
                        oPC+=1
                        timeDelay(30,10)
                elif oPC == 6:
                    if trainer.starterPokemon is not "":
                        oPC +=1
                        timeDelay(30,10)
                else:
                    oPC +=1
                    timeDelay(30,10)

        while gameRuns:
            # 27 milliseconds -- framerate
            clock.tick(27)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameRuns = False

            drawWindow()
            checkGameStage()
            pygame.display.update()

        pygame.quit()
