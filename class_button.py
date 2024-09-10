import pygame as pyg
pyg.init()
dis_surface = pyg.display.set_mode((800,600))
def MsgBox(text,color,pos):
    font = pyg.font.Font("Font/font.otf",30)
    afont = font.render(text,True,color)
    tfont = afont.get_rect()
    tfont.center = pos
    dis_surface.blit(afont,tfont)
class BUTTON:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.press = False
        self.pos = (self.x,self.y,self,w,self,h)
    def Creat(self,color,text,mc = pyg.mouse.get_pressed(),mp = pyg.mouse.get_pos()):
        if self.x < mp[0] < self.x+ self.w and self.y < mp[1] < self.y +self.h:
            pyg.draw.rect(dis_surface,color[0],self.pos)
            if mc[0] == True:
                self.press = True
            else:
                self.press = False
        else:
            pyg.draw.rect(dis_surface,color[1],self.pos)
            self.press = False
        MsgBox(text,"black",(self.x + self.w//2,self.y + self.h//2))
