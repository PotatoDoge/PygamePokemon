class Pokemon:
    def __init__(self,name="",type="",lvl=0,ID=0,evolution=None,frontSprite=None,backSprite=None,initialHealthPoints=0):
        self.name = name
        self.type = type
        self.lvl = lvl
        self.ID = ID
        self.evolution = evolution
        self.frontSprite = frontSprite
        self.backSprite = backSprite
        self.initialHealthPoints = initialHealthPoints
        self.health = self.initialHealthPoints
        self.XP = 0
        self.XPlimit = self.initialHealthPoints * 3

        # This attributes are for knowing pokemon positions inside an area
        # The are none because they do not have an actual value
        # When the random pokemon is created, a random value is assigned
        self.x = None
        self.y = None

        self.alive = True
        self.caught = False

    def evolving(self):
        if self.lvl == self.evolution.lvl:
            self.name = self.evolution.name
            self.ID = self.evolution.ID
            self.evolution = self.evolution.evolution
            self.frontSprite = self.evolution.frontSprite
            self.backSprite = self.evolution.backSprite
            self.initialHealthPoints = self.evolution.initialHealthPoints
            self.caught = True

    def attack(self):
        return int(round(self.initialHealthPoints/4))

    def addXP(self,enemy):
        if self.XP + enemy.initialHealthPoints >= self.XPlimit:
            self.XP = 0
            pokemon.levelUp(self)
        else:
            self.XP = self.XP + enemy.initialHealthPoints

    def levelUp(self):
        self.lvl +=1
        self.initialHealthPoints+=2
        if self.evolution is not None:
            if self.lvl == self.evolution.lvl:
                pokemon.evolving(self)
