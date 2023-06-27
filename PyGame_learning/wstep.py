import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))

x = 0
y = 0
player = pygame.rect.Rect(x, y, 80, 100)

run = True
while run:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += 1
    if keys[pygame.K_LEFT]:
        x -= 1
    if keys[pygame.K_UP]:
        y -= 1
    if keys[pygame.K_DOWN]:
        y += 1
    if keys[pygame.K_RIGHT]:
        x += 1

    player = pygame.rect.Rect(x, y, 80, 100)


    window.fill((24, 164, 248))
    pygame.draw.rect(window,(20,200,20),player)
    pygame.display.update()