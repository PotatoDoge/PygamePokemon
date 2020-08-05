import pygame

class text:
    def __init__(self,window,text):
        self.window = window
        self.text = text
        self.x = 50
        self.y = 500
        self.width = 500
        self.height = 80

    def draw(self):
        pygame.draw.rect(self.window,[255,255,255],(self.x,self.y,self.width,self.height))
        font = pygame.font.SysFont("tlwgtypewriter",18,True)
        font2 = pygame.font.SysFont("tlwgtypewriter",14,True)
        text = font.render(self.text,True,(0,0,0))
        next = font2.render("SPACEBAR -->", True, (0,0,0))
        self.window.blit(text,(self.x+15,self.y+10))
        self.window.blit(next,(self.x+400,self.y + 50))
