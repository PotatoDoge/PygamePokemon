import pygame

class motor:
    # Class Motor constructor
    def __init__(self):
        print("Initializing game")

    # When this function is called in the main, the game intializes
    def run(self):
        print("run")
        # INITIATES PYGAME
        pygame.init()

        #This initaliazes the window
        window = pygame.display.set_mode((600,600))

        # Title
        pygame.display.set_caption("PokeCetys")

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

        clock = pygame.time.Clock()

        gameRuns = True



        def drawWindow():
            window.fill(blue)

        while gameRuns:
            # 27 milliseconds -- framerate
            clock.tick(27)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # CHANGE THIS FOR SOME BOOLEANS TO FALSE
                    gameRuns = False
            drawWindow()
            pygame.display.update()

        pygame.quit()
