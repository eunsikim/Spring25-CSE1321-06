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
            
        pygame.draw.ellipse(screen, (255, 255, 255), pygame.Rect(150, 200, 200, 100))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()