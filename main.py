import pygame 

pygame.init()

# screaan settings
WIDTH = 800
HIGHT = 600

class game_ob():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw (self,screen,w,h):
        pygame.draw.rect(screen,'red',(self.x,self.y,w,h))


class player_class(game_ob):
    def __init__(self, x, y):
        super().__init__(x, y)
    def move(self, speed):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += speed
        if keys[pygame.K_LEFT]:
            self.x -= speed

class inv(game_ob):
    def __init__(self, x, y):
        super().__init__(x, y)
    def move(self, speed):
        if self.x ==500:
            self.x += speed
            pass
        self.x -= speed


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

    for i in invader :
        i.move(5)
        i.draw(screen,20,20)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()