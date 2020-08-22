import pygame
from Pokemon import *

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
    def __init__(self):

        # player's screen attributes   x = (windowWidth/2) - 20    y = (windowHeight/2) - 230
        self.x = 300
        self.y = 300
        self.height = 30
        self.width = 30

        # POSITIONAL ATTRIBUTES
        self.Xpos = 0
        self.Ypos = 0

        # PLAYER'S ATTRIBUTES
        self.gender = ""
        self.name =  ""
        self.starterPokemon = Pokemon()

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
        self.pace = 0

    # MISSING THE REST OF THIS CLASS AND ITS FUNCTIONS. FINISH LATER

    def createPokemon(self,pokemon):
        return Pokemon(pokemon.name,pokemon.type,pokemon.lvl,pokemon.ID,pokemon.evolution,
                       pokemon.frontSprite,pokemon.backSprite,pokemon.initialHealthPoints)

    def draw(self,wn):
        #self.hitbox = (self.x+5,self.y - 3, self.width -10, self.height + 2)
        if self.gender == 'male':
            if not self.standing:
                if self.right:
                    if self.walkCount == 0:
                        wn.blit(mWR,(self.x,self.y))
                    else:
                        wn.blit(maleStandingSprites[2],(self.x,self.y))
                elif self.left:
                    if self.walkCount == 0:
                        wn.blit(mWL,(self.x,self.y))
                    else:
                        wn.blit(maleStandingSprites[3],(self.x,self.y))

                elif self.front:
                    wn.blit(mWF[self.walkCount],(self.x,self.y))

                elif self.back:
                    wn.blit(mWB[self.walkCount],(self.x,self.y))

            else:
                if self.right:
                    wn.blit(maleStandingSprites[2],(self.x,self.y))
                elif self.left:
                    wn.blit(maleStandingSprites[3],(self.x,self.y))
                elif self.back:
                    wn.blit(maleStandingSprites[1],(self.x,self.y))
                elif self.front:
                    wn.blit(maleStandingSprites[0],(self.x,self.y))
