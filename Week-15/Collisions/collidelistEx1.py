import pygame

def main():
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((500, 500))

    redRect = pygame.Rect(0, 0, 200, 200)
    redSurf = pygame.Surface((redRect.w, redRect.h))
    redSurf.fill((255, 0, 0))

    greenRect = pygame.Rect(190, 190, 200, 200)
    greenSurf = pygame.Surface((greenRect.w, greenRect.h))
    greenSurf.fill((0, 255, 0))

    blueRect = pygame.Rect(0, 300, 200, 200)
    blueSurf = pygame.Surface((blueRect.w, blueRect.h))
    blueSurf.fill((0, 0, 255))

    yellowRect = pygame.Rect(300, 300, 200, 200)
    yellowSurf = pygame.Surface((yellowRect.w, yellowRect.h))
    yellowSurf.fill((255, 255, 0))

    list1 = [greenRect, blueRect]
    list2 = [redRect, blueRect]
    list3 = [redRect, greenRect, blueRect]

    print(redRect.collidelist(list1))
    print(yellowRect.collidelist(list3))
    print(yellowRect.collidelist(list2))
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(color=(0, 0, 0))
        
        screen.blit(redSurf, (redRect.x, redRect.y))
        screen.blit(greenSurf, (greenRect.x, greenRect.y))
        screen.blit(blueSurf, (blueRect.x, blueRect.y))
        screen.blit(yellowSurf, (yellowRect.x, yellowRect.y))

        pygame.display.flip()


        clock.tick(60)

if __name__ == "__main__":
    main()