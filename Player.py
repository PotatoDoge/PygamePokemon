import pygame

maleStandingSprites = [pygame.image.load('images/trainerSprites/male/StandingFront.png'),
                       pygame.image.load('images/trainerSprites/male/StandingBack.png'),
                       pygame.image.load('images/trainerSprites/male/StandingRight.png'),
                       pygame.image.load('images/trainerSprites/male/StandingLeft.png')]

# male Walking Sprites
mWR = pygame.image.load('images/trainerSprites/male/WalkingRight1.png')
mWL = pygame.image.load('images/trainerSprites/male/WalkingLeft1.png')
mWF = [pygame.image.load('images/trainerSprites/male/WalkingFront1.png'),
       pygame.image.load('images/trainerSprites/male/WalkingFront2.png')]
mWB = [pygame.image.load('images/trainerSprites/male/WalkingBack1.png'),
       pygame.image.load('images/trainerSprites/male/WalkingBack2.png')]

class player:
    def __init__(self,gender,name, starterPokemon)

    # player's screen attributes   x = (windowWidth/2) - 20    y = (windowHeight/2) - 230
    self.x = 280
    self.y = 270
    self.height = 30
    self.width = 30

    # POSITIONAL ATTRIBUTES
    self.Xpos = self.x
    self.Ypos = self.y

    # PLAYER'S ATTRIBUTES
    self.gender = gender
    self.name =  name
    self.starterPokemon = starterPokemon

    # PLAYER'S DIRECTION
    self.standing = True
    self.front = True
    self.back = False
    self.left = False
    self.right = False

    # Walking
    self.walkFront = True
    self.walkBack = True
    self.walkLeft = True
    self.walkRight = True

    # List where Pokemon will be stored so the player can access the anytime
    self.pokeList = []

    # List where medals that the player wins will be stored
    self.medals = []

    # List where extra Pokemon will be stored
    self.pokeBank = []

    # how many pixels the player moves when a key is pressed
    self.vel = 3
    self.walkCount = 0

    # MISSING THE REST OF THIS CLASS AND ITS FUNCTIONS. FINISH LATER
