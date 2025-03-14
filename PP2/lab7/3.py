import pygame
pygame.init()

screen = pygame.display.set_mode((800, 800))
running = True

clock = pygame.time.Clock()
FPS = 60

radius = 25
speed = 20
screen_size = 800
x, y = 30, 30

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y - speed >= radius:
        y -= speed
    if pressed[pygame.K_DOWN] and y + speed <= screen_size - radius:
        y += speed
    if pressed[pygame.K_LEFT] and x - speed >= radius:
        x -= speed
    if pressed[pygame.K_RIGHT] and x + speed <= screen_size - radius:
        x += speed
    
    screen.fill("white")
    pygame.draw.circle(screen, "red", (x, y), radius)
    pygame.display.flip()
    clock.tick(FPS)