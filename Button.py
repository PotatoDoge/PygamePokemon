import pygame

class button:
    def __init__(self,wn,color,x,y,width,height,text):
        self.wn = wn
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self):
        pygame.draw.rect(self.wn,self.color,(self.x,self.y,self.width,self.height))
        font = pygame.font.SysFont("tlwgtypewriter",20,True)
        text = font.render(self.text,True,(0,0,0))
        self.wn.blit(text,(self.x+15,self.y+10))
