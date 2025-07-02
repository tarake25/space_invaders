import pygame 

pygame.init()
screen = pygame.display.set_mode((600,800))
clock = pygame.time.Clock()
running = True

while running :
    screen.fill("red")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()