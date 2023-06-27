import pygame

pygame.init()
window = pygame.display.set_mode((1200, 720))

image = pygame.image.load("obrazek.png")

def main():
    run = True
    while run:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill((24, 164, 248))
        window.blit(image, (0,0))
        pygame.display.update()

if __name__ == "__main__":
    main()
