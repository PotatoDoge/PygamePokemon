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

    def inputLetters(self,string):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            string += "A"
        if keys[pygame.K_b]:
            string += "B"
        if keys[pygame.K_c]:
            string += "C"
        if keys[pygame.K_d]:
            string += "D"
        if keys[pygame.K_e]:
            string += "E"
        if keys[pygame.K_f]:
            string += "F"
        if keys[pygame.K_g]:
            string += "G"
        if keys[pygame.K_h]:
            string += "H"
        if keys[pygame.K_i]:
            string += "I"
        if keys[pygame.K_j]:
            string += "J"
        if keys[pygame.K_k]:
            string += "K"
        if keys[pygame.K_l]:
            string += "L"
        if keys[pygame.K_m]:
            string += "M"
        if keys[pygame.K_n]:
            string += "N"
        if keys[pygame.K_o]:
            string += "O"
        if keys[pygame.K_p]:
            string += "P"
        if keys[pygame.K_q]:
            string += "Q"
        if keys[pygame.K_r]:
            string += "R"
        if keys[pygame.K_s]:
            string += "S"
        if keys[pygame.K_t]:
            string += "T"
        if keys[pygame.K_u]:
            string += "U"
        if keys[pygame.K_v]:
            string += "V"
        if keys[pygame.K_w]:
            string += "W"
        if keys[pygame.K_x]:
            string += "X"
        if keys[pygame.K_y]:
            string += "Y"
        if keys[pygame.K_z]:
            string += "Z"

        return string
