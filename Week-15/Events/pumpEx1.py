import pygame

def main():
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((500, 500))

    running = True

    cutscene = True

    while running:
        # User can exit the game only if the cutscene is finished.
        if not cutscene:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        keys = pygame.key.get_pressed()

        # Skip the cutscene by pressing F
        if keys[pygame.K_f]:
            cutscene = False
        

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()