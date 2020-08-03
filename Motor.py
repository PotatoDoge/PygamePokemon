import pygame
from GameStage import *

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
        player = player(None,None,None)


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

        """
        Method that manages the logic of creating the playerself.
        This method is not in the GameStage class because it manages an object
        instantiated in this class
        """
        def createPlayer():
            gameStage.bgImage = pygame.image.load('images/backgrounds/introBG.png')
            gameStage.bgCoords = [0,0]
            mouse = pygame.mouse.get_pos()
            oakPhrases = ['Welcome, I am professor Oak','I will guide you in this new experience',
                          'What is your name?','It is nice to meet you ' + player.name, "Which character do you want to be?",
                          'Perfect!','Now, choose your starter pokemon', 'Perfect! You are ready to go!']



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
