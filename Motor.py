import pygame
from GameStage import *
from Text import *
from Player import *
from TextInput import *

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

        # professor oak's dialogue counter -----  oPC stands for oakPhrasesCounter
        oPC = 0

        # Boolean that sets the player's gender
        isMale = None

        # Object that allows the user to input the player's name
        txtInput = textInput(window,300,380,180,40,trainer.name)


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
            nonlocal isMale
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
                    if trainer.name != "":
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

            if oPC == 2:
                if len(txtInput.text) < 13:
                    txtInput.text = txtInput.inputLetters(trainer.name)
                    timeDelay(6,11)
                if keys[pygame.K_BACKSPACE]:
                    txtInput.text = txtInput.text[:-1]
                txtInput.draw()

            # player's name is set to what was inputted in the txtInpt
            trainer.name = txtInput.text

            if oPC == 4:

                boy = button(window, red, 260, 380, 80, 30, "")
                girl = button(window, red, 450, 380, 80, 30, "")
                window.blit(pygame.transform.scale(pygame.image.load('images/trainerSprites/male/maleTrainer.png'),(200,270)),(210,80))
                window.blit(pygame.transform.scale(pygame.image.load('images/trainerSprites/female/femaleTrainer.png'),(140,270)),(420,80))


                if isMale:
                    boy.color = green
                    girl.color = red
                elif isMale is False:
                    boy.color = red
                    girl.color = green

                boy.draw()
                girl.draw()

                if boy.hover(mouse):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        trainer.gender = "male"
                        isMale = True
                if girl.hover(mouse):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        trainer.gender = "female"
                        isMale = False

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
