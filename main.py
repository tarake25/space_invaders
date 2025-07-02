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
invader = []
for i in range(100,700,20):
    for j in range (40,400,20):
      invader.append(game_ob(i,j))




screen = pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("space invader")
clock = pygame.time.Clock()
running = True

while running :
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player = game_ob(WIDTH/2-40,HIGHT-40)
    player.draw(screen,40,20)

    for i in invader :
        i.draw(screen,15,15)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()