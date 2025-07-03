import pygame 
import math

pygame.init()

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
        for i in range(len(self.b_list)):
            self.b_list[i].move()
            self.b_list[i].draw(screen,5,5)
            for j in range(len(inv_list)):
                if self.b_list[i].hit(inv_list[j]):
                    inv_list[j].y += 100000
                    self.b_list[i].y+= 100000
    def game_over(self,list_inv):
        for inv in list_inv:
            if math.sqrt((self.x - inv.x)**2 + (self.y - inv.y)**2) == 10:
                return True
            elif inv.y == HIGHT :
                return True


        

class inv(game_ob):
    def __init__(self, x, y):
        super().__init__(x, y)
    def move(self, speed):
        self.x += speed
    
left,right = False,True

invader = []
for i in range(100,700,40):
    for j in range (40,300,30):
      invader.append(inv(i,j))

font = pygame.font.Font(None, 36)

text_2 = font.render("GAME OVER !!", True, (255, 0, 0)) 

screen = pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("space invader")
clock = pygame.time.Clock()
running = True
player = player_class(WIDTH/2-40,HIGHT-40)
while running :
    SCORE = []
    for i in invader:
        if i.y >= 100000:
            SCORE.append(i)

    screen.fill("black")
    text_surface = font.render(f"Remaining invaders: {len(invader) - len(SCORE)}", True, (255, 255, 255))
    screen.blit(text_surface, (5, 5))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    player.b_list.append(bolit(player.x + 20,player.y))
    
 

    player.move(10)
    player.draw(screen,40,20)
    player.shot(screen , invader)



    if player.game_over(invader):
        running = False

    hit_right_edge = any(inv.x + 20 >= WIDTH for inv in invader)
    hit_left_edge = any(inv.x <= 0 for inv in invader)

    if hit_right_edge:
        left, right = True, False
        for inv in invader:
            inv.y += 10
    elif hit_left_edge:
        left, right = False, True
        for inv in invader:
            inv.y += 10

    for inv in invader:
        if right:
            inv.move(5)
        elif left:
            inv.move(-5)
        inv.draw(screen, 20, 20)
    
    pygame.display.flip()
    clock.tick(30)
while not running:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = True
        screen.blit(text_2, (300, 300))
        pygame.display.flip()

pygame.quit()