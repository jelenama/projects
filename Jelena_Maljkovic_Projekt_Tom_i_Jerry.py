import pygame
import sys
import os
import random

#inicijalizacija pygame-a
pygame.init()

#naslov okvira igre
pygame.display.set_caption('TOM & JERRY')

class Enemy1(pygame.sprite.Sprite):

    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('tom.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

    def move(self):
        
        distance = 200
        speed = 5
        
        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance*2:
            self.rect.x -= speed
        else:
            self.counter = 0

        self.counter += 1

class Enemy2(pygame.sprite.Sprite):

    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('tom2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

    def move(self):
        
        distance = 200
        speed = 5
        
        if self.counter >= 0 and self.counter <= distance:
            self.rect.x -= speed
        elif self.counter >= distance and self.counter <= distance*2:
            self.rect.x += speed
        else:
            self.counter = 0

        self.counter += 1
        
class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.life = 5
        self.images = []
        self.bodovi=0
        
        
        img = pygame.image.load('jerry1.png')
        self.images.append(img)
        self.image = self.images[0]
        self.rect  = self.image.get_rect()
        

    def control(self,x,y):
        self.movex+=x
        self.movey+=y

        
    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        
        #kretanje lijevo
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0

        # kretanje desno
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0


        
        #u dodiru sa tomom gubi se život
        sudar1 = pygame.sprite.spritecollide(self, enemy_list, False)
        for enemy in sudar1:
            self.life -= 1
            player.rect.x = 0   
            player.rect.y = 600
            #print(self.life)

        sudar2= pygame.sprite.spritecollide(self, enemy2_list, False)
        for enemy2 in sudar2:
            self.life -= 1
            player.rect.x = 0   
            player.rect.y = 600
            #print(self.life)

        #kada se sir uhvati on se mice na novo random misto, i bodovi se povećaju za 1 
        uhvacen_sir = pygame.sprite.spritecollide(self, hrana_list, False)
        for h in uhvacen_sir:
            self.bodovi+=1
            hrana.rect.x = random.randrange(0,1330)
            hrana.rect.y = random.randrange(0,690)
            
           
            



class Hrana(pygame.sprite.Sprite):

    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sir.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,1200)
        self.rect.y = random.randrange(0,500)
        

    def updatefood(self):
        self.rect.x = random.randrange(0,1200)
        self.rect.y = random.randrange(0,500)
        


        
    
worldx = 0
worldy = 0



steps = 8

img = pygame.image.load('jerry1.png')

#postavljanje igrača
player = Player()   
player.rect.x = 0   
player.rect.y = 600
player_list = pygame.sprite.Group()
player_list.add(player)

#postavljanje neprijatelja
enemy= Enemy1(0,100,'tom.png')
enemy2=Enemy2(900,400,'tom2.png')
enemy_list=pygame.sprite.Group()
enemy2_list=pygame.sprite.Group()
enemy_list.add(enemy)
enemy2_list.add(enemy2)

#postavljanje hrane
hrana = Hrana('sir.png')   
hrana_list = pygame.sprite.Group()
hrana_list.add(hrana)



#postavljanje pozadine

world = pygame.display.set_mode([worldx,worldy])
backdrop = pygame.image.load('bcg.jpg')
startscreen= pygame.image.load('start.jpg')
backdropbox = world.get_rect()

#boje
RED = (255,0,0)
GREEN = (0,155,0)
BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)


smallfont = pygame.font.SysFont("Arial", 25)
medfont = pygame.font.SysFont("Arial", 50)
largefont = pygame.font.SysFont("Arial", 80)

display_width = 1333
display_height  = 700
gameDisplay = pygame.display.set_mode((display_width,display_height))



fps = 40
ani = 4
clock = pygame.time.Clock()




#start screen igre
def uvod():
    pocetak=True
   
    while pocetak:

        #ako se klikne esc, bez ovoga ne mozemo prekinit igru
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                
            #ako se klikne p igra pocinje
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pocetak=False
                    Igraj()
                    pygame.display.update()
                    
            #ako se klikne q otkazujemo igru
            
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

                
                    
        #uputeeee
        message_to_screen("TOM & JERRY",RED,-300,"large")
        message_to_screen("                     Pomozi Jerryju u skupljanju sireva,",GREEN,-250,"small")
        message_to_screen("                       pazi da te Tom ne ulovi jer gubiš živote!!",GREEN,-220,"small")        
        message_to_screen("                             Pritisni p za početak svoje avanture,",GREEN,-190,"small")
        message_to_screen("                                  a q ako nisi dorastao zadatku",GREEN,-170,"small")
        pygame.display.update()
        clock.tick(15)


#za ispis poruka 
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)

#font
def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    
    return textSurface, textSurface.get_rect()

#funkcija koja sluzi za prikaz bodova    
def score(x):
    text=smallfont.render("Score:"+str(x),True,WHITE)
    gameDisplay.blit(text,[0,0])
    
def krajigre():
    kraj_igre=True
    
    while kraj_igre:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        quit()
                
##            #ako se klikne p igra pocinje ispocetka, igracu se postavljaju zivoti
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            hrana.updatefood()
                            #sluzi kao vrsta reseta igraca nakon ponovnog pokretanja igre
                            player.__init__()
                            #namištamo ga na početne koordinate
                            player.rect.x = 0   
                            player.rect.y = 600
                            kraj_igre=False
                            Igraj()
                    
                        #ako se klikne q otkazujemo igru
                    #if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()
                            main = False
                        
                world.blit(backdrop, backdropbox)
                message_to_screen("GAME OVER",BLUE,-100,"large")
                message_to_screen("Za ponovnu igru kliknite p,",RED,-30,"small")
                message_to_screen("a za izlaz kliknite q",RED,10,"small")
                pygame.display.update()
                pygame.display.flip()
                clock.tick(fps)

                
#stavljamo True da se program nebi izvrsio u jednom milisekundi nego da traje
#MAIN funkcija igre
def Igraj():
    main=True

    while main:
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
                main = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.control(-steps,0)
                    
                if event.key == pygame.K_RIGHT:
                    player.control(steps,0)
                    
                if event.key == pygame.K_UP:
                    player.control(0,-steps)
                    
                if event.key == pygame.K_DOWN:
                    player.control(0,steps)
                    
            
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.control(steps,0)
                    
                if event.key == pygame.K_RIGHT:
                     player.control(-steps,0)
                     
                if event.key == pygame.K_UP:
                    player.control(0,steps)
                    
                if event.key == pygame.K_DOWN:
                    player.control(0,-steps)
                    
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()
                    main = False

        world.blit(backdrop, backdropbox)
        player_list.draw(world)
        hrana_list.draw(world)
        player.update()
        score(player.bodovi)
        
        enemy_list.draw(world)
        enemy2_list.draw(world)
        
        for e in enemy_list:
            e.move()

        for e2 in enemy2_list:
            e2.move()

        #ako igrac izgubi sve zivote dolazi do kraja igre
        if player.life<=0:
            main=False
            krajigre()
            
           
        
    #Kazemo Pythonu da osvjezi sve na ekranu
        pygame.display.flip()
       
    #Pomicemo sat
        clock.tick(fps)

world.blit(startscreen, backdropbox)
uvod()
