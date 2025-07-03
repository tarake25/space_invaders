import pygame 

pygame.init()
import math
# screaan settings
WIDTH = 800
HIGHT = 600

class game_ob():
    WIDTH = 800
    HIGHT = 600
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw (self,screen,w,h):
        pygame.draw.rect(screen,'red',(self.x,self.y,w,h))

class bolit(game_ob):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.s = 10
    def move(self):
        self.y -= self.s
    def hit(self,inv):
        if math.sqrt((self.x - inv.x)**2 + (self.y - inv.y)**2) == 10:
            return True

            

class player_class(game_ob):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.b_list = []
    def move(self, speed):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += speed
        if keys[pygame.K_LEFT]:
            self.x -= speed
    def shot(self,screen,inv_list):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.b_list.append(bolit(self.x,self.y))
        for i in range(len(self.b_list)):
            self.b_list[i].move()
            self.b_list[i].draw(screen,5,5)
            for j in range(len(inv_list)):
                if self.b_list[i].hit(inv_list[j]):
                    inv_list[j].x += 100000
                    self.b_list[i].x+= 100000
                    
        

class inv(game_ob):
    def __init__(self, x, y):
        super().__init__(x, y)
    def move(self, speed):
        pass



invader = []
for i in range(100,700,40):
    for j in range (40,300,30):
      invader.append(inv(i,j))




screen = pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("space invader")
clock = pygame.time.Clock()
running = True
player = player_class(WIDTH/2-40,HIGHT-40)
while running :
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    player.move(10)
    player.draw(screen,40,20)
    player.shot(screen,invader)

    for i in invader :
        i.move(5)
        i.draw(screen,20,20)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()