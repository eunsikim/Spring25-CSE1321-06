import pygame

def main():
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((500, 500))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()


        if keys[pygame.K_SPACE]:
            print("User pressed the Space Bar")
        if keys[pygame.K_h]:
            print("Hello World")

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()