import pygame as pyg
import time as t
debug = False
pyg.init()
#constant and global variable
Dis_Title = "GameCharacterControl"
Dis_Size = Dis_Width,Dis_Height = 800,600
Dis_Fps = 60
Char_Size = Char_Width,Char_Height =60,60
Background_Img = pyg.transform.scale(pyg.image.load("Img/background_img.jpg"),Dis_Size)
User_Spaceship = "Img/user_spaceship_1.png"
Bullet_Img = "Img/bullet_img.png"
Enemy_Img = "Img/enemy_img.png"
#text
Text_Font = "Font/font.otf"
#display
dis_clock = pyg.time.Clock()
dis_clock.tick(Dis_Fps)
dis_surface = pyg.display.set_mode(Dis_Size)
pyg.display.set_caption(Dis_Title)
#function
def Button(text,pos,color,textsize = 30):
    pyg.draw.rect(dis_surface,color,pos)
    MsgBox(text,(pos[0]+pos[2]//2,pos[1]+pos[3]//2),textsize)
def MsgBox(text,textpos,textsize = 30,textcolor = "black"):
    text_font = pyg.font.Font(Text_Font,textsize)
    text_img = text_font.render(text,True,textcolor)
    text_surf = text_img.get_rect()
    text_surf.center = textpos
    dis_surface.blit(text_img,text_surf)
def CharacterCreat(char_img,char_size,char_pos):
    img = pyg.image.load(char_img)
    suf = pyg.transform.scale(img,char_size)
    dis_surface.blit(img,char_pos)
    return suf
def EnemyInit(num = 3):
    tlist = []
    if num > 3:
        num = 3
    elif num<1:
        num = 1
    for i in range(num):
        for c in range(10):
            tlist.append(ENEMY((c+1) * ( 10 + Char_Width),20 + 75 * i))
    return tlist
def GameFun():
    user_spaceship = SPACESHP(Dis_Width // 2, Dis_Height - Char_Height * 2.5, User_Spaceship)
    game_run = True
    bullet_list = []
    while game_run:
        dis_surface.blit(Background_Img, (0, 0))
        dis_surface.fill("white")
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                # GameEnd() add this outside the loop
                game_run = False
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    game_run = False
                if event.key == pyg.K_w:
                    user_spaceship.y_speed -= 10
                if event.key == pyg.K_s:
                    user_spaceship.y_speed += 10
                if event.key == pyg.K_a:
                    user_spaceship.x_speed -= 10
                if event.key == pyg.K_d:
                    user_spaceship.x_speed += 10
                if event.key == pyg.K_f:
                    bullet_list.append(BULLET(user_spaceship.x, user_spaceship.y))
        user_spaceship.x += user_spaceship.x_speed
        user_spaceship.y += user_spaceship.y_speed
        user_spaceship.x_speed *= 0.8
        user_spaceship.y_speed *= 0.8
        dis_surface.blit(user_spaceship.self, (user_spaceship.x, user_spaceship.y))
        for i in range(0, len(bullet_list)):
            if i < len(bullet_list):
                bullet_list[i].y -= 5
                dis_surface.blit(bullet_list[i].self, (bullet_list[i].x + 10, bullet_list[i].y))
                if bullet_list[i].y < 0:
                    bullet_list.remove(bullet_list[i])

        pyg.display.update()
        dis_clock.tick(Dis_Fps)
def GameEnd():
    MsgBox("=====GameEnd=====",(Dis_Width//2,Dis_Height//2))
    t.sleep(0.3)
    quit()
class ENEMY:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.self = Enemy_Img
class BULLET:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.self = CharacterCreat(Bullet_Img,(20,20),(self.x,self.y))
class SPACESHP:
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
        self.self = CharacterCreat(img,Char_Size,(self.x,self.y))
class BUTTON:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.press = False
        # self.pos = (self.x,self.y,self,w,self,h)
    def Creat(self,text,bcolor,mc,mp):
        if self.x < mp[0] < self.x+ self.w and self.y < mp[1] < self.y +self.h:
            pyg.draw.rect(dis_surface,bcolor[0],(self.x,self.y,self.w,self.h))
            if mc[0] == True:
                self.press = True
            else:
                self.press = False
        else:
            pyg.draw.rect(dis_surface,bcolor[1],(self.x,self.y,self.w,self.h))
            self.press = False

        MsgBox(text,(self.x+self.w//2,self.y+self.h//2))

        #using value "press" to detect if the button has been pressed
#init
if not(debug):
    game_run = True

    while game_run:
        GameFun()
        wait = True

        b_continue = BUTTON(100,400,100,50)
        b_quit = BUTTON(600,400,100,50)

    #wait for the next game or quit
        while wait:
            for event in pyg.event.get():
                mouse_press = pyg.mouse.get_pressed()
                mouse_pos = pyg.mouse.get_pos()
                if event.type == pyg.QUIT:
                    GameEnd()
                mouse_click = pyg.mouse.get_pressed()
                mouse_pos = pyg.mouse.get_pos()
                dis_surface.fill("white")

                b_continue.Creat("continue",("green","red"),mouse_press,mouse_pos)
                b_quit.Creat("quit",("green","red"),mouse_press,mouse_pos)
                if b_continue.press == True or b_quit.press == True:
                    wait = False
                pyg.display.update()
                dis_clock.tick(Dis_Fps)


        #detect
        if b_quit.press == True:
            game_run = False


    GameEnd()

########################################################################debug block
if debug:
    enemy_list = EnemyInit(6)
    for c in range(len(enemy_list)):
        enemy_list[c].self = CharacterCreat(Enemy_Img,Char_Size,(enemy_list[c].x,enemy_list[c].y))


    while True:
        for event in pyg.event.get():
            # dis_surface.fill("white")
            if event.type == pyg.QUIT:
                GameEnd()
            pyg.display.update()