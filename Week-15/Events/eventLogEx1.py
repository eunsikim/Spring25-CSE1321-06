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

            print("Event name: " + str(pygame.event.event_name(event.type)))
            print("Event dict: " + str(event.dict))


        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()