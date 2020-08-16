import pygame
from GameStage import *
from Text import *
from Player import *
from TextInput import *
from Pokedex import *

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
        #trainer = player("","","")
        trainer = player()

        # professor oak's dialogue counter -----  oPC stands for oakPhrasesCounter
        oPC = 0

        # Boolean that sets the player's gender
        isMale = None

        # Object that allows the user to input the player's name
        txtInput = textInput(window,300,380,180,40,trainer.name)

        pkdx = pokedex.generatePokeList(self)

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

            elif gameStage.stage == "tutorial":
                gameStage.tutorial(event)

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
        Fade out screen effect
        """
        def fade(width, height):
            fade = pygame.Surface((width, height))
            fade.fill((0, 0, 0))
            for alpha in range(0, 300):
                fade.set_alpha(alpha)
                drawWindow()
                window.blit(fade, (0, 0))
                pygame.display.update()
                pygame.time.delay(2)

        """
        Method that manages the logic of creating the player itself.
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
                    if trainer.starterPokemon.name is not "":
                        oPC +=1
                        timeDelay(30,10)
                elif oPC == 7:
                    fade(600,600)
                    gameStage.bgImage = pygame.image.load('images/backgrounds/pokeMenuBG.png')
                    gameStage.stage = 'tutorial'

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
            if oPC == 6:
                newBulbasaur = pygame.transform.scale(pkdx[0].frontSprite,(150,150))
                newCharmander = pygame.transform.scale(pkdx[3].frontSprite,(150,150))
                newSquirtle = pygame.transform.scale(pkdx[6].frontSprite,(150,150))

                bulbasaurButton = button(window,red,275,260,40,18,"")
                charmanderButton = button(window,red,375,260,40,18,"")
                squirtleButton = button(window,red,475,260,40,18,"")

                window.blit(newBulbasaur,(220,140))
                window.blit(newCharmander,(320,140))
                window.blit(newSquirtle,(420,140))

                if trainer.starterPokemon.name == pkdx[0].name:
                    bulbasaurButton.color = green
                    charmanderButton.color = red
                    squirtleButton.color = red

                elif trainer.starterPokemon.name == pkdx[3].name:
                    bulbasaurButton.color = red
                    charmanderButton.color = green
                    squirtleButton.color = red

                elif trainer.starterPokemon.name == pkdx[6].name:
                    bulbasaurButton.color = red
                    charmanderButton.color = red
                    squirtleButton.color = green

                if bulbasaurButton.hover(mouse):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        trainer.starterPokemon = trainer.createPokemon(pkdx[0])

                if charmanderButton.hover(mouse):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        trainer.starterPokemon = trainer.createPokemon(pkdx[3])

                if squirtleButton.hover(mouse):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        trainer.starterPokemon = trainer.createPokemon(pkdx[6])

                bulbasaurButton.draw()
                charmanderButton.draw()
                squirtleButton.draw()

        while gameRuns:
            # 27 milliseconds -- framerate
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameRuns = False

            drawWindow()
            checkGameStage()

            pygame.display.update()

        pygame.quit()
