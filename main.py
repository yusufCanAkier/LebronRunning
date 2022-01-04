import pygame
import random

#DISPLAY CONFIGURE
pygame.init()
clock = pygame.time.Clock()
fps = 65
screen_height = 480
screen_width = 960
ekran = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("LebronRun")
bg = pygame.image.load("bg.png")

#COLOR INPUT
white = (255, 255, 255)

#IMAGE RECTANGLE DRAW
imagerect = bg.get_rect()
imagerect.x, imagerect.y = (0, 0)

#VARIABLES
gameOver = False
frequency = 1500
lastItem = pygame.time.get_ticks() - frequency
skor = 0
font = pygame.font.SysFont('Helvetica', 40)
font2 = pygame.font.SysFont('Helvetica', 60)
healthBar = 200
kingPriceItem = 0
x2 = False
x2time = 0
x2timeControl = 0
x2ofTime = 0
shield = False
shieldTime = 0
shieldTimeControl = 0
timeOfShield = 0
donma = False
freezeTime = 0
freezeTimeControl = 0
timeOfFreeze = 0
reverse = False
reverseTime = 0
reverseTimeControl = 0
timeOfReverse = 0

b_group = pygame.sprite.Group()
y_group = pygame.sprite.Group()

#GLOBAL VARIABLES
def replay():
    global gameOver
    gameOver = False
    global healthBar
    healthBar = 200
    global kingPriceItem
    kingPriceItem = 0
    global skor
    skor = 0
    global x2
    x2 = False
    global x2time
    x2time = 0
    global x2timeControl
    x2timeControl = 0
    global x2ofTime
    x2ofTime = 0
    global shield
    shield = False
    global shieldTime
    shieldTime = 0
    global shieldTimeControl
    shieldTimeControl = 0
    global timeOfShield
    timeOfShield = 0
    global donma
    donma = False
    global freezeTime
    freezeTime = 0
    global freezeTimeControl
    freezeTimeControl = 0
    global timeOfFreeze
    timeOfFreeze = 0
    global reverse
    reverse = False
    global reverseTime
    reverseTime = 0
    global reverseTimeControl
    reverseTimeControl = 0
    global timeOfReverse
    timeOfReverse = 0
    global y_group
    y_group.empty()

#CHARACTER DEFINITION FUNCTIONS
class LebronJames(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('fatboy.png')
        self.image = pygame.transform.scale(
            self.image, (100, 150))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        
#CHARACHTER REVERSE MOVEMENT
    def update(self):

        if pygame.key.get_pressed()[97] == 1 and donma == False and reverse == False:
            self.rect.x -= 7

        if pygame.key.get_pressed()[100] == 1 and donma == False and reverse == False:
            self.rect.x += 7

        if pygame.key.get_pressed()[97] == 1 and donma == False and reverse == True:
            self.rect.x += 7

        if pygame.key.get_pressed()[100] == 1 and donma == False and reverse == True:
            self.rect.x -= 7

        if self.rect.x < 0:
            self.rect.x = 0

        if self.rect.x > 880:
            self.rect.x = 880

#CHARACTER COLLECT ITEMS
class Items(pygame.sprite.Sprite):
    i = 0
    def __init__(self, x, y, i):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Adsız'+str(i)+'.png')
        self.i = i
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def update(self):

        self.rect.y += 1
#SHOW REPLAY BUTTON END OF THE GAME
class Button(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('replay1.png')
        self.image = pygame.transform.scale(
            self.image, (200, 150))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1:
               replay()

# DEFINE OUR CHARACHTER WITH POSITON ON WINDOW
King = LebronJames(300, 8 * screen_height / 10)

b_group.add(King)
# WHILE GAME STARTING THIS SCOPE WILL BE TRUE AND RUNNING
run = True
while run:
    clock.tick(fps)
    ekran.fill(white)
    ekran.blit(bg, imagerect)

    if gameOver != True:
        timenow = pygame.time.get_ticks()
        altbar = pygame.draw.rect(ekran, (255, 0, 0), (750, 15, 200, 30), 1)
        bar = pygame.draw.rect(ekran, (0, 255, 0), (750, 15, healthBar, 30), 1)
        pygame.Surface.fill(ekran, (255, 0, 0), altbar)
        pygame.Surface.fill(ekran, (0, 255, 0), bar)
        b_group.draw(ekran)
        b_group.update()
        y_group.draw(ekran)
        y_group.update()
        healthBar -= .1
        skorekle = random.randint(0,1)
        if x2 == True:
            skorekle *= 2
        skor += skorekle
        skoryazi = font.render(str(skor), 2, (255, 0, 0))
        ekran.blit(skoryazi, (10, 10))
        if healthBar <= 0:
            gameOver = True
        if timenow - lastItem > frequency:
            kingPriceItem += 1
            i = 13
            while i == 13:
                i = random.randint(1, 28)
            if kingPriceItem == 26:
                i = 13
                kingPriceItem = 0
            CollectibleItems = Items(random.randint(0, 600), 100, i)
            y_group.add(CollectibleItems)
            lastItem = timenow
        for CollectibleItems in y_group:
            if x2 and x2timeControl == 0:
                x2time = pygame.time.get_ticks()
                x2timeControl = 1
            if shield and shieldTimeControl == 0:
                shieldTime = pygame.time.get_ticks()
                shieldTimeControl = 1
            if donma and freezeTimeControl == 0:
                freezeTime = pygame.time.get_ticks()
                freezeTimeControl = 1
            if reverse and reverseTimeControl == 0:
                reverseTime = pygame.time.get_ticks()
                reverseTimeControl = 1
            if CollectibleItems.rect.x+37 >= King.rect.x + 20 and CollectibleItems.rect.x + 37 <= King.rect.x + 120 and CollectibleItems.rect.y == King.rect.y:
                y_group.remove(CollectibleItems)
                if CollectibleItems.i < 13:
                    skor += 1
                    if healthBar < 189:
                        healthBar += 12
                        skor += 100
                    else:
                        healthBar = 200
                if CollectibleItems.i < 20 and CollectibleItems.i > 13:
                    skor -= 2
                    if healthBar < 6:
                        healthBar = 0
                    else:
                        healthBar -= 6
                if CollectibleItems.i == 13:
                    skor += 10
                    healthBar = 200
                if CollectibleItems.i > 19 and CollectibleItems.i < 25 and shield == False:
                    gameOver = True
                if CollectibleItems.i == 25:
                    x2 = True
                    x2ofTime += 15000
                    healthBar += 6
                if CollectibleItems.i == 26:
                    shield = True
                    timeOfShield += 20000
                    healthBar += 6
                if CollectibleItems.i == 27:
                    donma = True
                    timeOfFreeze += 8000
                    healthBar += 6
                if CollectibleItems.i == 28:
                    reverse = True
                    timeOfReverse += 10000
                    healthBar += 6
            if x2:
                x2yazi = font.render(str(int((x2ofTime - (timenow - x2time)) / 1000)), 2, (0, 0, 0), (255, 255, 255))
                x2yazisi = font.render("x2 : ", 2, (0, 0, 0), (255, 255, 255))
                ekran.blit(x2yazisi, (45, 900))
                ekran.blit(x2yazi, (100, 900))
            if timenow - x2time > x2ofTime and x2timeControl == 1:
                x2 = False
                x2timeControl = 0
                x2ofTime = 0
            if shield:
                kalkanyazi = font.render(str(int((timeOfShield - (timenow - shieldTime)) / 1000)), 2, (0, 0, 0), (255, 255, 255))
                kalkanyazisi = font.render("Kalkan : ", 2, (0, 0, 0), (255, 255, 255))
                ekran.blit(kalkanyazisi, (165, 900))
                ekran.blit(kalkanyazi, (280, 900))
            if timenow - shieldTime > timeOfShield and shieldTimeControl == 1:
                shield = False
                shieldTimeControl = 0
                timeOfShield = 0
            if donma:
                donmayazi = font.render(str(int((timeOfFreeze - (timenow - freezeTime)) / 1000)), 2, (0, 0, 0), (255, 255, 255))
                donmayazisi = font.render("Donma : ", 2, (0, 0, 0), (255, 255, 255))
                ekran.blit(donmayazisi, (340, 900))
                ekran.blit(donmayazi, (470, 900))
            if timenow - freezeTime > timeOfFreeze and freezeTimeControl == 1:
                donma = False
                freezeTimeControl = 0
                timeOfFreeze = 0
            if reverse:
                tersyazi = font.render(str(int((timeOfReverse - (timenow - reverseTime)) / 1000)), 2, (0, 0, 0), (255, 255, 255))
                tersyazisi = font.render("Ters : ", 2, (0, 0, 0), (255, 255, 255))
                ekran.blit(tersyazisi, (520, 900))
                ekran.blit(tersyazi, (610, 900))
            if timenow - reverseTime > timeOfReverse and reverseTimeControl == 1:
                reverse = False
                reverseTimeControl = 0
                timeOfReverse = 0
            if CollectibleItems.rect.y > 1000:
                y_group.remove(CollectibleItems)
    else:
       # gameoveryazisi = font2.render("GAMEOVER", 2, (255, 64, 64))
       # ekran.blit(gameoveryazisi, (350, 150))

        gameoverskoryazi = font.render("SKOR :", 2, (255, 64, 64))
        ekran.blit(gameoverskoryazi, (350, 300))
        gameoverskor = font.render(str(skor), 2, (0, 0, 0))
        ekran.blit(gameoverskor, (470, 300))
        gameOverImage = pygame.image.load('gameOverImage.png')
        gameOverImage = pygame.transform.scale(gameOverImage, (350, 150))
        ekran.blit(gameOverImage, (305, 50))
        b_play = Button(500, 250)
        button_group = pygame.sprite.Group()
        button_group.add(b_play)
        button_group.draw(ekran)
        button_group.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.QUIT

    pygame.display.update()