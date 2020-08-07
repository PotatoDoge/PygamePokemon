import pygame

class textInput:
    def __init__(self,wn,x,y,width,height,text):
        self.wn = wn
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = [255,255,255]

    def draw(self):
        pygame.draw.rect(self.wn,self.color,(self.x,self.y,self.width,self.height))
        font = pygame.font.SysFont("tlwgtypewriter",18,True)
        text = font.render(self.text,True,(0,0,0))
        self.wn.blit(text,(self.x+15,self.y+10))
